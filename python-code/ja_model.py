import pickle

def predict_Ja():
    print("it's working")
    with open('models/gradient_boosting_Ja.pkl','rb') as f:
        Ja_model = pickle.load(f)
        print(Ja_model.predict([[3]]))

# Ja ends here
predict_Ja()
