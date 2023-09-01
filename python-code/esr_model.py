import pickle

def predict_esr():
    with open('models/model_LR_esr.pkl','rb') as f:
        esr_model = pickle.load(f)
        # print(esr_model.predict([[38]]))

# esr ends here
predict_esr()