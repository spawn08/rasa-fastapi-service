from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Interpreter
from rasa.nlu import train
from rasa.utils.tensorflow.constants import (
    EPOCHS,
)
from rasa.nlu.convert import convert_training_data
from ml_app.config.config import *


def load_model(model_name):
    interpreter = Interpreter.load(model_name)
    return interpreter


async def train_model(model_name, lang):
    _config = RasaNLUModelConfig({"pipeline": PIPELINE_INTENT_WITHOUT_SPLIT, "language": "en"})
    (trainer, trained, persisted_path) = await train(
        _config,
        path=MODEL_PATH,
        data=DATA_PATH + model_name + '_' + lang,
        fixed_model_name='spawnai_en'
    )
    return {'model': model_name, 'message': 'Model Trained Successfully'}
