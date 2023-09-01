import pickle

def predict_rqd():
    with open('models/knn_regressor_rqd.pkl','rb') as f:
        rqd_model = pickle.load(f)
        print(rqd_model.predict([[38]]))

# rqd ends here
predict_rqd()