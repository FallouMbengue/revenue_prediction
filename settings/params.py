"""Project Params"""

# random seed
SEED = 50

MODEL_PARAMS = {
    "TRAIN_PATH": "../data/train.csv",
    "PREDICTION_PATH":"../data/prediction.csv",
    "DATA_PREPROCESSED_PATH":"../data/preprocessed.csv",
    "TEST_PATH" : "../data/test.csv",
    "TARGET_NAME": "revenue",
    "MIN_COMPLETION_RATE": 0.80,
    "MIN_PPS":0,
    "TEST_SIZE": 0.2,
    "DEFAULT_FEATURE_NAMES":[
       'city', 'city group', 'type', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6',
       'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16',
       'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26',
       'p27', 'p28', 'p29', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36',
       'p37', 'day', 'day_name', 'month', 'years'
    ]
    
}

