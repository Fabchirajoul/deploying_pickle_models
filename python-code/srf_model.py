import pickle

def predict_srf():
    with open('models/extra_tree_srf.pkl','rb') as f:
        srf_model = pickle.load(f)
        # print(srf_model.predict([[38]]))

# srf ends here
predict_srf()
