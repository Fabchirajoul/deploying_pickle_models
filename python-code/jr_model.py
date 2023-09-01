import pickle

def predict_Jr():
    with open('models/Decision_tree_regressor_Jr.pkl','rb') as f:
        Jr_model = pickle.load(f)
        print(Jr_model.predict([[38]]))

# Jr ends here
predict_Jr()
