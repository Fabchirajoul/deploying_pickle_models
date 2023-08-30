
import numpy as np
from flask import Flask, request, render_template
import pickle


# Create an app object using the Flask class.
app = Flask(__name__)


# loading the models
model_Jn = pickle.load(open('models/ababoost_Jn.pkl', 'rb'))
model_Ja = pickle.load(open('models/gradient_boosting_Ja.pkl', 'rb'))
model_Jr = pickle.load(open('models/Decision_tree_regressor_Jr.pkl', 'rb'))
model_Jw = pickle.load(open('models/gradient_boosting_Jw.pkl', 'rb'))
model_us = pickle.load(open('models/ababoost_us.pkl', 'rb'))
model_q = pickle.load(open('models/extra_tree_q.pkl', 'rb'))
model_srf = pickle.load(open('models/extra_tree_srf.pkl', 'rb'))
model_rqd = pickle.load(open('models/knn_regressor_rqd.pkl', 'rb'))
model_esr = pickle.load(open('models/model_LR_esr.pkl', 'rb'))
model_rmr = pickle.load(open('models/Random_Forest_regresor_rmr.pkl', 'rb'))
model_ucsvsr = pickle.load(open('models/gradient_boosting_ucsvsr.pkl', 'rb'))


# use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')


# Jn model
@app.route('/predict_Jn', methods=['POST'])
def predict_Jn():

    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]

    prediction_Jn = model_Jn.predict(features)

    output = round(prediction_Jn[0], 2)

    return render_template('index.html', prediction_text_Jn='Based on your input, the Jn value is {}'.format(output))

# Jn ends here

# Ja starts here 

@app.route('/predict_Ja', methods=['POST'])
def predict_Ja():

    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]

    prediction_Ja = model_Ja.predict(features)

    output = round(prediction_Ja[0], 2)

    return render_template('index.html', prediction_text_Ja='Based on your input, the Ja value is {}'.format(output))


# Ja ends here 





# if so, execute it here.
# If we import this file (module) to another file then __name__ == app (which is the name of this python file).
if __name__ == "__main__":
    app.run()
