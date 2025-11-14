from flasgger import Swagger

def init_swagger(app):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Healthcare API",
            "description": "API para gestión de profesionales y unidades médicas",
            "version": "1.0.0"
        },
        "schemes": ["http"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header usando el esquema Bearer. Ejemplo: 'Bearer {token}'"
            }
        }
    }

    app.config["SWAGGER"] = {
        "title": "Healthcare API",
        "uiversion": 3,
    }

    Swagger(app, template=template)
