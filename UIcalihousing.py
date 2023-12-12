# Panel App application is designed and created to predict the targeted variable.

import panel as pn
import numpy as np
import pickle

# Load the model
with open('Decision_Tree_Regressor_model.pkl', 'rb') as file:
    loaded_decision_tree_regressor_model = pickle.load(file)

# Define the features
features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude']

# Create input widgets for each feature
input_widgets = {feature: pn.widgets.FloatInput(value=0) for feature in features}

# Create a button to trigger prediction
predict_button = pn.widgets.Button(name="Predict", button_type="primary")

# Output widget for displaying the prediction result
result_output = pn.widgets.StaticText(name="Prediction Result", value="", style={"color": "black"})

# Function to make prediction
def make_prediction(event):
    input_values = [input_widgets[feature].value for feature in features]
    adjusted_sample_input = np.array([input_values])
    decision_tree_prediction = loaded_decision_tree_regressor_model.predict(adjusted_sample_input)
    result_output.value = f"Decision Tree Regressor Prediction: {decision_tree_prediction[0]}"

    # Explicitly update the result in the Panel app
    layout[-1] = result_output

# Attach the function to the button click event
predict_button.on_click(make_prediction)

# Create a layout for the app
layout = pn.Column(
    *[
        pn.Column(pn.panel(feature), input_widgets[feature]) for feature in features
    ],
    predict_button,
    result_output
)

# Show the app
layout.servable()


