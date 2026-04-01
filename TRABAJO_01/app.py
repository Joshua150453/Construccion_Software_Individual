from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base de datos en memoria
users = []

# =========================
# CRUD DE USUARIOS
# =========================

# 1. LIST (Obtener todos)
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# 2. GET (Obtener uno por ID)
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "Usuario no encontrado"}), 404

# 3. CREATE (Crear nuevo)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    
    # Validación básica
    if not data.get("name") or not data.get("lastname"):
        return jsonify({"error": "Nombre y apellido son obligatorios"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "lastname": data.get("lastname"),
        "address": {
            "city": data.get("address", {}).get("city", "N/A"),
            "country": data.get("address", {}).get("country", "N/A"),
            "postal_code": data.get("address", {}).get("postal_code", "N/A")
        }
    }
    users.append(new_user)
    return jsonify(new_user), 201

# 4. UPDATE (Actualizar)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.json
    user["name"] = data.get("name", user["name"])
    user["lastname"] = data.get("lastname", user["lastname"])
    
    if "address" in data:
        user["address"].update(data["address"])

    return jsonify({"message": "Usuario actualizado", "user": user})

# 5. DELETE (Eliminar)
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Usuario eliminado correctamente"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)