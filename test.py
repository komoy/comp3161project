from app import db
from app.models import UserProfile

user = UserProfile("Komoy", "Haye", "admin", "password")

db.session.add(user)
db.session.commit()

print("Check db")