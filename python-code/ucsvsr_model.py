import pickle

def predict_ucsvsr():
    with open('models/gradient_boosting_ucsvsr.pkl','rb') as f:
        ucsvsr_model = pickle.load(f)
        # print(ucsvsr_model.predict([[38]]))

# ucsvsr ends here
predict_ucsvsr()