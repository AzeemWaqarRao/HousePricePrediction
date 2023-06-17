# Boston House Pricing ML Project
This is a machine learning project that uses a linear regression model to predict the prices of houses in Boston, Massachusetts. The project includes a Jupyter notebook where the model is trained and a Flask web application where the model is deployed and used to make predictions.

## Requirements
To run the project, you will need the following software installed on your system:<br>

Python 3.7 or higher<br>
Jupyter Notebook<br>
Flask<br>
You can install Flask and other required libraries by running the following command:

```
pip install -r requirements.txt
```
## Usage
To use the project, follow these steps:

Open the Jupyter notebook (boston-house-pricing.ipynb) and run all cells to train the linear regression model on the Boston Housing dataset.
Once the model is trained, it will be saved as model.pkl<br>

Start the Flask web application by running the following command in cmd opened in working directory:
```
python app.py
```
This will start the web application on http://localhost:5000/.

Open your web browser and go to http://localhost:5000/ to access the web application.

Enter the values of the features for the house you want to predict the price for and click the "Predict" button. The application will use the trained model to make a prediction and display the result.

## Files
The project includes the following files:

* model_training.ipynb: a Jupyter notebook where the linear regression model is trained on the Boston Housing dataset.
* model.py: a Python script to save the trained model to a file.
* app.py: a Flask web application that uses the trained model to make predictions.
<<<<<<< HEAD
* templates/home.html: an HTML template for the web application.
=======
* templates/home.html: an HTML template for the web application.
>>>>>>> 188644fe6aba9e9f85740f6e49af8f99d80edeb5
