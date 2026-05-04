import json

name=str(input("What is your name? "))
age=int(input("What is your age? "))
adress=str(input("What is your address? "))

data = {
    "name": name,
    "age": age,
    "adress": adress
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Data has been saved to data.json")