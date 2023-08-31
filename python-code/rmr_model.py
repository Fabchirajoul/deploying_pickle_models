import pickle

def predict_rmr():
    print("it's working")
    with open('models/Random_Forest_regresor_rmr.pkl','rb') as f:
        rmr_model = pickle.load(f)
        print(rmr_model.predict([[0.000564, 1.0]]))

# rmr ends here
predict_rmr()
