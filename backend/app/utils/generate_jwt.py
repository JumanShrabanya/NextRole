
import secrets

# Generate a strong secret key (you can save this securely)
SECRET_KEY = secrets.token_urlsafe(32)


print("🔐 JWT Token:")
print(SECRET_KEY)
# print("\n🔑 Secret Key (store securely):")
# print(SECRET_KEY)
