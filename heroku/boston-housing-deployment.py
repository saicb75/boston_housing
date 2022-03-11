#!/usr/bin/env python
# coding: utf-8

# # Auto mpg  Model Deployment
# After analysing the given dataset, we have built and saved  model.
# 
# This Flask application is written to deploy the model in production so that users can supply automobile parameters and obtain an estimated mpg prediction.
# 
# There are two deployment models supported:
# 
# 1. Deployment to local machine
#     1. Just run this notebook in your local machine
#     
# 2. Deployment to Heroku, which needs
#     1. Procfile
#     2. requirements.txt
# 
# (search for and follow the steps to deploy the complete `deployment` folder, subfolders and contents to Heroku)

# In[ ]:


import pandas as pd
from flask import Flask, request, render_template, redirect
import pickle


# ### Load the Linear Regression  Auto mpg Model

# In[ ]:


print(f'Creating a flask app for {__name__}')
app = Flask(__name__)


# In[ ]:


def load_model(filename):
    pklfile = open(filename, 'rb')
    lr_model = pickle.load(pklfile)
    pklfile.close()
    return lr_model


# In[ ]:


lr_model_boston_housing = load_model("models/boston_housing_model.pkl")


# ### Create a flask app

# ### Establish Routes for Auto mpg Prediction

# In[ ]:


#Establish default route
@app.route('/')
def default():
    return redirect('/boston_housing_input')


# In[ ]:


# Establish auto mpg routes
@app.route('/boston_housing_input')
def boston_housing_input():
    return render_template('boston_housing_input.html')

@app.route('/boston_housing_predict', methods = ['GET'])
def boston_housing_predict():
    if request.method == 'GET':
        rm = request.args.get('rm')
        ptratio = request.args.get('ptratio')
        lstat = request.args.get('lstat')
               
              
        data_boston_housing = pd.DataFrame([[rm,ptratio,lstat]])
        arr_boston_housing_predict = lr_model_boston_housing.predict(data_boston_housing)[0]
        arr_boston_housing_predict = int(round(arr_boston_housing_predict,0))
        
        return render_template('boston_housing_predict.html',rm = rm, ptratio = ptratio,
                               lstat = lstat, 
                               arr_boston_housing_predict=arr_boston_housing_predict)
    
    return "Unsupported request method,{}".format(request.method),400


# ### Run the Flask Web Server

# In[ ]:


if __name__ == '__main__':
    app.run()

