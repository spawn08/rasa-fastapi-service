from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

from ml_app.utils.model_utils import *

app = FastAPI()
security = HTTPBasic()
loaded_model: Interpreter = None
model_cache: dict = {}


async def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"})
    return True


@app.on_event('startup')
async def start_up():
    global loaded_model
    global model_cache
    model_name = MODEL_PATH + DEFAULT_MODEL
    loaded_model = load_model(model_name)
    model_cache[model_name] = loaded_model
    pass


@app.get('/train')
async def train_model(model_name: str, lang: str,
                      dependencies=Depends(get_current_username)):
    global model_cache
    formatted_model_name = model_name + '_' + lang
    model_cache[formatted_model_name] = None
    return await train_rasa_model(model_name, lang)


@app.get('/predict')
async def predict(q: str,
                  model_name: str,
                  lang: str,
                  dependencies=Depends(get_current_username)
                  ):
    global model_cache
    global loaded_model
    model_name = model_name + '_' + lang
    model_path = MODEL_PATH + '\\' + model_name
    if model_cache.get(model_name) == None:
        model_cache[model_name] = load_model(model_path)

    loaded_model = model_cache[model_name]
    response = loaded_model.parse(q)
    return response
