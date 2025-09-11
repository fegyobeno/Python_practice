import requests

url = "http://127.0.0.1:10000/adat_fogadása/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 10.99,
    "tax": 1.99
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

# Update request
update_url = "http://127.0.0.1:10000/items/1"  # Assuming the item ID to update is 1
update_data = {
    "name": "Updated Sample Item",
    "description": "This is an updated sample item",
    "price": 12.99,
    "tax": 2.49
}

update_response = requests.put(update_url, headers=headers, json=update_data)

print(update_response.status_code)
print(update_response.json())

# Delete request
delete_url = "http://127.0.0.1:10000/items/2"  # Assuming the item ID to delete is 1
delete_response = requests.delete(delete_url)
print(delete_response.status_code)
