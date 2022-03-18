from flask_app import Bcrypt, app

print(app)

bcrypt = Bcrypt(app)

my_hash = bcrypt.generate_password_hash("stinky")

print(my_hash)

check = bcrypt.check_password_hash(my_hash, "stinky")
check2 = bcrypt.check_password_hash(b'$2b$12$3K/bAxM42VptuEKh7pBEh./EP9bQMm0Of7NRv/iA2FNeBNa7M4IIi', "stinky")

print(check, check2)