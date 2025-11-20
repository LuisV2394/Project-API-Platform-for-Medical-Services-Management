from flask import Blueprint, jsonify, request
from app.models.unit import Unit
from app import db
from app.utils.middleware import role_required
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
import os

units_bp = Blueprint("units", __name__, url_prefix="/units")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "units")
)
print("BASE_DOCS:", BASE_DOCS)

# Obtener todas las unidades
@units_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_units():
    units = Unit.query.all()
    return jsonify([u.to_dict() for u in units]), 200

# Obtener unidad por ID
@units_bp.route("/<int:unit_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_unit_by_id(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404
    return jsonify(unit.to_dict()), 200

# Crear nueva unidad
@units_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_unit():
    data = request.get_json()
    required_fields = ["name", "type"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_unit = Unit(
        name=data["name"],
        type=data["type"],
        description=data.get("description"),
        phone=data.get("phone"),
        is_active=data.get("is_active", True)
    )

    db.session.add(new_unit)
    db.session.commit()

    return jsonify({
        "message": "Unit created successfully",
        "unit": new_unit.to_dict()
    }), 201

# Actualizar unidad
@units_bp.route("/<int:unit_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_unit(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if hasattr(unit, key):
            setattr(unit, key, value)

    db.session.commit()

    return jsonify({
        "message": "Unit updated successfully",
        "unit": unit.to_dict()
    }), 200

# Desactivar unidad
@units_bp.route("/<int:unit_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_unit(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    unit.is_active = False
    db.session.commit()

    return jsonify({"message": "Unit deactivated successfully"}), 200