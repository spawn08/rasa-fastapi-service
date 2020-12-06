import asyncio

from rasa.nlu import train
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.convert import convert_training_data
from rasa.nlu.model import Interpreter
from rasa.utils.tensorflow.constants import (
    EPOCHS,
)

pipeline = [
    {
        "name": "WhitespaceTokenizer",
        "intent_tokenization_flag": True,
        "intent_split_symbol": "+",
    },
    {"name": "RegexFeaturizer"},
    {"name": "LexicalSyntacticFeaturizer"},
    {"name": "CountVectorsFeaturizer"},
    {"name": "CountVectorsFeaturizer", 'analyzer': 'char_wb', 'min_ngram': 1, 'max_ngram': 4},
    {"name": "DIETClassifier", EPOCHS: 50},
    {'name': 'EntitySynonymMapper'},
    {'name': 'ResponseSelector', EPOCHS: 'epochs'}
]
#


async def train_model():
    _config = RasaNLUModelConfig({"pipeline": pipeline, "language": "en"})

    (trainer, trained, persisted_path) = await train(
        _config,
        path='C:\\Users\\Amar\\PycharmProjects\\rasa_test\\',
        data="C:\\Users\\Amar\\PycharmProjects\\rasa_test\\spawnai_en.md",
        fixed_model_name='spawnai_en'
    )
    print(persisted_path)

    pass


async def predict(query):
    loaded = Interpreter.load('C:\\Users\\Amar\\PycharmProjects\\rasa_test\\nlu_20201206-143222')
    results = loaded.parse(query)
    print(results)
    pass


async def convert_json_to_md():
    convert_training_data(
        'demo-rasa.json', 'demo.md', 'md', 'en'
    )
    pass


loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(train_model())
loop.close()
