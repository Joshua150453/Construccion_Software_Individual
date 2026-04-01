# App Anaconda/Postman

# Nombre: Joshua David Ortiz Rosas

# 🚀 Task & User Manager API (Flask + Vanilla JS)

Este proyecto es una aplicación web educativa que implementa dos CRUDs completos (Tareas y Usuarios) utilizando un backend en **Flask** y un frontend de una sola página en **HTML/JS puro**.

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto en entorno local (usando **Anaconda Prompt** o terminal estándar):

1. **Clonar o descargar**
-- los archivos `app.py` e `index.html` en una misma carpeta.
-- Instalar las dependencias necesarias:Bashpip install flask flask-cors
-- Iniciar el servidor:Bashpython app.py
-- El servidor estará disponible en: http://127.0.0.1:5000 

### 📂 Estructura de Datos (User Model)
Siguiendo los requerimientos, cada usuario cuenta con los siguientes atributos:

-- AtributoTipoDescripción
-- idIntegerIdentificador único autoincremental.
-- nameStringNombre del usuario.
-- lastnameStringApellido del usuario.
-- addressObjectObjeto anidado que contiene city, country y postal_code.

### 🧪 Pruebas del CRUD en Postman

Para probar las funcionalidades de la API de Usuarios, utilizar los siguientes parámetros:

#### 1. Listar Usuarios (List/Read All)
-- Método: GET
-- URL: http://127.0.0.1:5000/users

#### 2. Crear Usuario (Create)
-- Método: POST
-- URL: http://127.0.0.1:5000/users
-- Body (JSON):

{
    "name": "Juan",
    "lastname": "Pérez",
    "address": {
        "city": "Arequipa",
        "country": "Perú",
        "postal_code": "04001"
    }
}

#### 3. Actualizar Usuario (Update)
-- Método: PUT
-- URL: http://127.0.0.1:5000/users/1
-- Body (JSON):

{
    "name": "Juan Alberto",
    "address": {
        "city": "Lima"
    }
}

#### 4. Eliminar Usuario (Delete)
-- Método: DELETE
-- URL: http://127.0.0.1:5000/users/1

### 🖥️ Uso del Frontend
El frontend ha sido desarrollado con Vanilla JavaScript (sin frameworks) para visualizar la conexión con la API en tiempo real.

-- Asegurese de que el servidor Flask esté corriendo.
-- Abre el archivo index.html en el navegador.
-- El formulario permite registrar usuarios y la tabla inferior se actualiza automáticamente realizando peticiones fetch() al backend.
