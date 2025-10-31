from models import User, sessionLocal

session = sessionLocal()

#get all
users = session.query(User).all()
print(users)

for user in users:
    print(user.id, user.name, user.email)


#get by primary id
user1 = session.query(User).get(1)
if user1:
    print(user1.id, user1.name, "- by using get()")
else:
    print("user not found")


#or using filter_by
user2 = session.query(User).filter_by(id = 2).first()
if user2:
    print(user2.id, user2.name, "- by using filter_by()")
else:
    print("user not found")


#get the duplicates
ravi_users = session.query(User).filter_by(name = "Ravi").all()
if ravi_users:
    for r in ravi_users:
        print(r.id, r.name, r.email, "- by using filter_by()")
else:
    print("user not found")


# Read users whose name starts with 'R'
userR = session.query(User).filter(User.name.like("R%")).all()
print("Details of the users whose name starts with 'R'")
for user in userR:
    print(user.id, user.name)


# Read users with name starting with 'R' and email ending with 'example.com'
print("Details of the users whose name starts with 'R' and email ending with 'example.com'")
userR_example = session.query(User).filter(
    User.name.like("R%"),
    User.email.like("%example.com")
)

for user in userR_example:
    print(user.id, user.name)