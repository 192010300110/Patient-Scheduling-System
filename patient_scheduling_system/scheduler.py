## scheduler.py
from typing import List
from models import Appointment, Patient


class Scheduler:
    def __init__(self, appointments: List[Appointment]):
        self.appointments = appointments

    def get_available_slots(self) -> List[Appointment]:
        """
        Returns a list of available appointment slots.

        Returns:
            List[Appointment]: A list of available appointment slots.
        """
        return [appointment for appointment in self.appointments if not appointment.confirmed and not appointment.declined and not appointment.rescheduled]

    def update_slot_availability(self, appointment: Appointment, available: bool) -> None:
        """
        Updates the availability of an appointment slot.

        Args:
            appointment (Appointment): The appointment to update.
            available (bool): The availability status of the appointment slot.
        """
        appointment.confirmed = False
        appointment.declined = False
        appointment.rescheduled = False

        if not available:
            appointment.declined = True

    def update_patient_priority(self, patient: Patient, priority: int) -> None:
        """
        Updates the priority of a patient.

        Args:
            patient (Patient): The patient to update.
            priority (int): The new priority value.
        """
        patient.priority = priority

    def prioritize_appointments(self) -> List[Appointment]:
        """
        Prioritizes the appointments based on patient priority.

        Returns:
            List[Appointment]: A list of prioritized appointments.
        """
        return sorted(self.appointments, key=lambda appointment: appointment.patient.priority, reverse=True)

    def suggest_off_peak_slots(self, patient: Patient) -> List[Appointment]:
        """
        Suggests off-peak appointment slots for a patient.

        Args:
            patient (Patient): The patient to suggest off-peak slots for.

        Returns:
            List[Appointment]: A list of suggested off-peak appointment slots.
        """
        off_peak_slots = [appointment for appointment in self.appointments if appointment.datetime.hour < 9 or appointment.datetime.hour > 17]
        return sorted(off_peak_slots, key=lambda appointment: abs(appointment.datetime.hour - 12))
