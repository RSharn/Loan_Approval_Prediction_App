
# Loan Approval Prediction App

This Streamlit web application is designed for predicting loan approval status based on input features. The underlying model is a Random Forest classifier trained on relevant data. Users can input various features related to financial history and behavior to obtain a prediction on whether a loan application is likely to be approved or not.


## Usage/Examples

1. Install the required dependencies by running the following command

```
pip install streamlit pandas joblib scikit-learn

```

2. Ensure that the trained model file (random_forest_model_1.joblib) is in the same directory as the script.

3. Run the application using the following command:

```
streamlit run your_script_name.py
```
4. The web application will open in your default web browser, allowing you to input values for various financial features.

## Input Features

The application provides input fields for the following features:

* Age
* Annual Income
* Monthly Inhand Salary
* Number of Bank Accounts
* Number of Credit Cards
* Interest Rate
* Number of Loans
* Delay from Due Date
* Number of Delayed Payments
* Changed Credit Limit
* Number of Credit Inquiries
* Credit Mix (Bad, Standard, Good)
* Outstanding Debt
* Credit Utilization Ratio
* Credit History Age (in years)
* Payment of Minimum Amount (Yes/No)
* Total EMI per Month
* Amount Invested Monthly
* Payment Behavior (High, Medium, Low, None)
* Monthly Balance
* Month of Application

Default values are provided for each feature, and users can modify these values based on their scenario.
## Making Predictions

Once the input values are set, clicking the "Predict Loan Approval Status" button will trigger the model to make a prediction. The predicted result, whether the loan is approved or not, will be displayed on the screen.

Please note that this application is intended for demonstration purposes, and the accuracy of predictions depends on the quality and relevance of the input data.

Feel free to customize the application or integrate it into your projects as needed.