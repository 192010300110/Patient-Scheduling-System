## routes.py
from flask import Blueprint, jsonify, request
from database import (
    get_all_patients,
    get_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
)
from models import Patient

patient_routes = Blueprint("patients", __name__, url_prefix="/patients")

@patient_routes.route("", methods=["GET"])
def get_all_patients_route():
    """
    Get all patients.

    Returns:
        List[Patient]: A list of all patients.
    """
    patients = get_all_patients()
    return jsonify(patients)

@patient_routes.route("/<int:patient_id>", methods=["GET"])
def get_patient_by_id_route(patient_id):
    """
    Get a patient by ID.

    Args:
        patient_id (int): The ID of the patient.

    Returns:
        Patient: The patient with the specified ID.
    """
    patient = get_patient_by_id(patient_id)
    if patient:
        return jsonify(patient)
    else:
        return jsonify({"error": "Patient not found"}), 404

@patient_routes.route("", methods=["POST"])
def create_patient_route():
    """
    Create a new patient.

    Returns:
        Patient: The created patient.
    """
    data = request.get_json()
    patient = Patient(
        id=data.get("id"),
        name=data.get("name"),
        phone_number=data.get("phone_number"),
        email=data.get("email"),
        appointments=data.get("appointments"),
    )
    created_patient = create_patient(patient)
    return jsonify(created_patient), 201

@patient_routes.route("/<int:patient_id>", methods=["PUT"])
def update_patient_route(patient_id):
    """
    Update a patient by ID.

    Args:
        patient_id (int): The ID of the patient.

    Returns:
        Patient: The updated patient.
    """
    data = request.get_json()
    patient = Patient(
        id=patient_id,
        name=data.get("name"),
        phone_number=data.get("phone_number"),
        email=data.get("email"),
        appointments=data.get("appointments"),
    )
    updated_patient = update_patient(patient)
    if updated_patient:
        return jsonify(updated_patient)
    else:
        return jsonify({"error": "Patient not found"}), 404

@patient_routes.route("/<int:patient_id>", methods=["DELETE"])
def delete_patient_route(patient_id):
    """
    Delete a patient by ID.

    Args:
        patient_id (int): The ID of the patient.
    """
    delete_patient(patient_id)
    return "", 204
