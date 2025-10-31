from models import sessionLocal, User  # Import the session and User model

# Create a session instance
session = sessionLocal()

# Clear existing data before inserting new users
session.query(User).delete()
session.commit()

#single insert
new_user = User(name = "Krishna", email = "krishna@gmail.com")
session.add(new_user)
session.commit()

#multiple insert
more_users = [
    User(name = "Ram", email = "ram@gmail.com"),
    User(name = "Sai", email = "sai@gmail.com"), 
    User(name="Shalini", email="shalini@example.com"),
    User(name="Ravi", email="ravi@example.com"),
    User(name="Satya", email="satya@example.com"),
    User(name="Ravi", email="ravi2.0@example.com"),
]

session.add_all(more_users)
session.commit()
