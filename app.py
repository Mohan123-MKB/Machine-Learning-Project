import numpy as np
from flask import Flask, render_template,request
import math
import pickle
app=Flask(__name__)

# load our trained model
model2=pickle.load(open('model.pkl','rb'))

@app.route('/',methods=["GET"]) #home file
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict(): #total prediction ithula run pandrom
    input_features=[int(i) for i in request.form.values()] #[1,2,3,4]
    final_input_features=np.array(input_features).reshape(1,-1) #[[1,2,3,4]] shape is [0,1]
    prediction_output=model2.predict(final_input_features)
    output=round(prediction_output[0],2)

    return render_template('index.html',prediction="Number of weekly rides {}".format(math.floor(output))) #frontend send pananum output

if __name__ == '__main__':
    app.run(debug=True) #automatic refresh agidum
