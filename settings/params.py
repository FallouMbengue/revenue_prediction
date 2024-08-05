"""Project Params"""

# random seed
SEED = 50

MODEL_PARAMS = {
    "TRAIN_PATH": "../data/train.csv",
    "DATA_PATH": "../data/restaurant_data.csv",
    "DATA_PREPROCESSED_PATH":"../data/preprocessed.csv",
    "TEST_PATH" : "../data/test.csv",
    "TARGET_NAME": "revenue",
    "MIN_COMPLETION_RATE": 0.80,
    "MIN_PPS":0.01,
    "DEFAULT_FEATURE_NAMES":[
       'location', 'cuisine', 'rating', 'seating capacity',
       'average meal price', 'marketing budget', 'social media followers',
       'chef experience years', 'number of reviews', 'avg review length',
       'ambience score', 'service quality score', 'parking availability',
       'weekend reservations', 'weekday reservations', 
    ]
    
}

