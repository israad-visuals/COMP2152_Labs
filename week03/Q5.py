contacts = { "alice": "555-1234555-5678", "bob": "555-9999", "charlie": "43434-21323"}

print("Alice's number" , contacts["alice"])
print("Bo's number" , contacts["bob"])
contacts["diana"] = "3434-34355"
print(f"Contacts after adding diana : {contacts}")
contacts["bob"] = "3434-32727"
print(f"Contacts after updating bob : {contacts}")
del contacts["charlie"]
print(f"Contacts after deleting charlie : {contacts}")
print("All contacts ;" , contacts)
