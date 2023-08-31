import pickle

def predict_Jn():
    with open('models/ababoost_Jn.pkl','rb') as f:
        Jn_model = pickle.load(f)
        print(Jn_model.predict([[38]]))

# Jn ends here
predict_Jn()
