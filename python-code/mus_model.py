import pickle

def predict_mus():
    print("it's working")
    with open('models/ababoost_us.pkl','rb') as f:
        mus_model = pickle.load(f)
        print(mus_model.predict([[0.069333,	1.6]]))

# mus ends here
predict_mus()
