import passlib
from passlib.hash import bcrypt

print("Passlib version:", passlib.__version__)
print("Bcrypt hash test:", bcrypt.hash("Secret123"))