import pickle

def predict_Jw():
    with open('models/gradient_boosting_Jw.pkl','rb') as f:
        Jw_model = pickle.load(f)
        print(Jw_model.predict([[38]]))

# Jw ends here
predict_Jw()
