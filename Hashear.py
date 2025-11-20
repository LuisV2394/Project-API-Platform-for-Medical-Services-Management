import passlib
from passlib.hash import bcrypt
#Esto solamente se uso para verificar la versión de passlib y que bcrypt funciona correctamente
# Se usó para crear la contraseña hasheada inicial en la base de datos porque aún no tenía implementada la funcionalidad de registro de usuarios
print("Passlib version:", passlib.__version__)
print("Bcrypt hash test:", bcrypt.hash("Secret123"))