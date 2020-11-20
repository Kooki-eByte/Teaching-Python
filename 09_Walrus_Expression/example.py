#  The Walrus operator :=

request = {
    "form": {
        "username": "Cristian",
        "password": "iLovePython"
    }
}

db = []


def process_form(req):
    # password = req["form"].get("password")

    if len(password := req["form"].get("password")) > 5:
        db.append(password)
        return "User Added!"
    else:
        return "Password is too short!"


print(process_form(request))
print(db)
