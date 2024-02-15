
import streamlit as st
import joblib
import pandas as pd
import sklearn

# Load the trained model
model = joblib.load('random_forest_model_1.joblib')




# Streamlit app layout
st.title('Loan Approval Prediction App')

# Define default values for each input feature
default_values = {
    "Age": 25,
    "Annual_Income": 60000,
    "Monthly_Inhand_Salary": 5000,
    "Num_Bank_Accounts": 2,
    "Num_Credit_Card": 3,
    "Interest_Rate": 20,
    "Num_of_Loan": 1,
    "Delay_from_due_date": 3,
    "Num_of_Delayed_Payment": 2,
    "Changed_Credit_Limit": 30,
    "Num_Credit_Inquiries": 10,
    "Credit_Mix": 2,
    "Outstanding_Debt": 15000,
    "Credit_Utilization_Ratio": 45,
    "Credit_History_Age": 8,  # Assuming input as numeric (years)
    "Payment_of_Min_Amount": "Yes",  # Assuming binary choice: Yes/No
    "Total_EMI_per_month": 250,
    "Amount_invested_monthly": 200,
    "Payment_Behaviour": "High",
    "Monthly_Balance": 3000,
    "Num_Month": "January"
    }

# Create input fields for each feature
input_data = {}
for feature, default in default_values.items():
    if feature == "is_train":
        continue
    if feature in ["Payment_of_Min_Amount"]:
        # For binary choice features, using Yes/No options
        input_data[feature] = st.selectbox(feature, ["Yes", "No"], index=["Yes", "No"].index(str(default)))
    elif isinstance(default, int) or isinstance(default, float):
        # For numerical features
        input_data[feature] = st.number_input(feature, value=default)
    else:
        # This condition is for any other types of inputs that may require special handling
        input_data[feature] = st.text_input(feature, value=str(default))

# Convert certain inputs to the model's expected format
input_data["Payment_of_Min_Amount"] = 1 if input_data["Payment_of_Min_Amount"] == "Yes" else 0
input_data["Credit_Mix"] = 1 if input_data["Credit_Mix"] == "Bad" else (2 if input_data["Credit_Mix"] == "Standard" else (3 if input_data["Credit_Mix"] == "Good" else 0))
input_data["Payment_Behaviour"] = 3 if input_data["Payment_Behaviour"] == "High" else (2 if input_data["Payment_Behaviour"] == "Medium" else (1 if input_data["Payment_Behaviour"] == "Low" else (0 if input_data["Payment_Behaviour"] == "None" else -1)))
input_data["is_train"] = False
input_data["Num_Month"] = (
    1 if input_data["Num_Month"] == "January" else
    (2 if input_data["Num_Month"] == "February" else
     (3 if input_data["Num_Month"] == "March" else
      (4 if input_data["Num_Month"] == "April" else
       (5 if input_data["Num_Month"] == "May" else
        (6 if input_data["Num_Month"] == "June" else
         (7 if input_data["Num_Month"] == "July" else
          (8 if input_data["Num_Month"] == "August" else 0)
         )
        )
       )
      )
     )
    )
)



# Button to make prediction
if st.button('Predict Loan Approval Status'):
    # Convert input_data to DataFrame
    df_predict = pd.DataFrame([input_data])
    # Example list of column names in the order expected by the model
    model_columns = ['Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
                     'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Delay_from_due_date',
                     'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries',
                     'Credit_Mix', 'Outstanding_Debt', 'Credit_Utilization_Ratio',
                     'Credit_History_Age', 'Payment_of_Min_Amount', 'Total_EMI_per_month',
                     'Amount_invested_monthly', 'Payment_Behaviour', 'Monthly_Balance',
                     'is_train', 'Num_Month']
    df_predict = df_predict[model_columns]



    # Make a prediction
    prediction = model.predict(df_predict)

    # Display the prediction
    result = "Approved" if prediction[0] == 1 else "Not Approved"
    st.write(f'Loan Approval Status: {result}')


