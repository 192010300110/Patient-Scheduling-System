"""
models.py
Contains the Patient and Appointment classes.
"""

from datetime import datetime
from typing import List

class Patient:
    def __init__(self, id: int, name: str, phone_number: str, email: str, appointments: List['Appointment']):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.appointments = appointments

class Appointment:
    def __init__(self, id: int, datetime: datetime, confirmed: bool, declined: bool, rescheduled: bool, patient: Patient):
        self.id = id
        self.datetime = datetime
        self.confirmed = confirmed
        self.declined = declined
        self.rescheduled = rescheduled
        self.patient = patient
