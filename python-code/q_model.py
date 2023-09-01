import pickle

def predict_q():
    with open('models/extra_tree_q.pkl','rb') as f:
        q_model = pickle.load(f)
        # print(q_model.predict([[38]]))

# q ends here
predict_q()
