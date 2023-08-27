"""
machine_learning.py
Contains the MachineLearning class for training and predicting patient behavior.
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class MachineLearning:
    def __init__(self):
        self.model = None

    def train_model(self):
        """
        Trains the machine learning model.
        """
        # Load the iris dataset
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the model
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(X_train, y_train)

    def predict_patient_behavior(self, patient):
        """
        Predicts the behavior of a patient.

        Args:
            patient: The patient data.

        Returns:
            str: The predicted behavior of the patient.
        """
        # Convert patient data to features
        features = [patient.age, patient.gender, patient.blood_pressure]

        # Predict the behavior using the trained model
        behavior = self.model.predict([features])[0]

        return behavior

    def update_model(self, appointment, response):
        """
        Updates the machine learning model based on the patient's response to an appointment.

        Args:
            appointment: The appointment data.
            response: The patient's response to the appointment.
        """
        # Convert appointment data and response to features and target
        features = [appointment.datetime, appointment.duration, appointment.location]
        target = response

        # Update the model with the new data
        self.model.fit([features], [target])
