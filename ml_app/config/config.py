USERNAME = 'onebotsolution'
PASSWORD = 'OneBotFinancialServices'
DEFAULT_MODEL = 'spawnai_en'
MODEL_PATH = './models/'
DATA_PATH = './data/'
EPOCHS = 'epochs'
PIPELINE_INTENT_SPLIT = [
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
PIPELINE_INTENT_WITHOUT_SPLIT = [
    {
        "name": "WhitespaceTokenizer",
        "intent_tokenization_flag": False
    },
    {"name": "RegexFeaturizer"},
    {"name": "LexicalSyntacticFeaturizer"},
    {"name": "CountVectorsFeaturizer"},
    {"name": "CountVectorsFeaturizer", 'analyzer': 'char_wb', 'min_ngram': 1, 'max_ngram': 4},
    {"name": "DIETClassifier", EPOCHS: 50},
    {'name': 'EntitySynonymMapper'},
    {'name': 'ResponseSelector', EPOCHS: 'epochs'}
]
