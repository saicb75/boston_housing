# Boston Housing Price Prediction Data Set

The dataset used in this project comes from the UCI Machine Learning Repository. 
This data was collected in 1978 and each of the 506 entries represents aggregate information about 14 features of homes from various suburbs located in Boston.

#### Attribute Information:

The features can be summarized as follows:

1.CRIM - per capita crime rate by town

2.ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

3.INDUS - proportion of non-retail business acres per town.

4.CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)

5.NOX - nitric oxides concentration (parts per 10 million)

6.RM - average number of rooms per dwelling

7.AGE - proportion of owner-occupied units built prior to 1940

8.DIS - weighted distances to five Boston employment centres

9.RAD - index of accessibility to radial highways

10.TAX - full-value property-tax rate per $10,000

11.PTRATIO - pupil-teacher ratio by town
B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

12.LSTAT - % lower status of the population

13.MEDV - Median value of owner-occupied homes in $1000's
  

#### Data Set Information:

For the purpose of the project the dataset has been preprocessed as follows:\n",
    "The essential features for the project are: ‘RM’, ‘LSTAT’, ‘PTRATIO’ and ‘MEDV’. The remaining features have been excluded.\n",
    "16 data points with a ‘MEDV’ value of 50.0 have been removed. As they likely contain censored or missing values.\n",
    "1 data point with a ‘RM’ value of 8.78 it is considered an outlier and has been removed for the optimal performance of the model.\n",
    "As this data is out of date, the ‘MEDV’ value has been scaled multiplicatively to account for 35 years of markt inflation.

## Approach for Boston Housing Price Prediction Model Development

Project Setup:

Our project adopts a folder structure as follows:

<pre>
    Boston Housing Price Prediction,
       |________ ml-models",
           |________ datasets",
           |________ models",
      |________ deployment",
           |________ models",
           |________ templates",
</pre>
   

### Develop an ML Model

Developing an ML model involves a number of steps. Let us adopt the following Machine Learning Pipeline:

1. Sanity Check 

2. EDA/Preprocessing

3. Feature Engineering

4. Model Building

5. Model Saving

6. Model Deployment
    
    
Once the model is deployed, the pipeline extends to include the below steps:
    
7. Model in Production

8. Observe model behaviour
    
9. Obtain updated datasets
    
10. Redo steps 1..9 if required

Note: these extended steps are not covered in this exercise

#### Boston Housing Price Prediction

### Result obtained
Model Accuracy 73.52%

### Deployment

The saved model will be deployed in production and made accessible to users for determining house price prediction . A Flask application is developed for this purpose.

Two approaches are covered:

1. Deployment on local machine
2. Deployment on Heroku

### Way Forward

The model developed here show an accuracy of about 73.52%. Further improvement can be attempted using other ML techniques like Deep Learning.