


import json

base_url = "http://localhost:5000"

resources = [
    "users",
    "nations",
    "villages",
    "shinobi",
    "threat_profiles",
    "jutsu",
    "missions",
    "teams",
    "team_members",
    "shinobi_jutsu"
]

def create_crud_items(resource):
    label = resource.replace("_", " ").title()
    singular = label[:-1] if label.endswith("s") else label
    return [
        {
            "name": f"Get All {label}",
            "request": {"method": "GET", "url": {"raw": f"{base_url}/{resource}"}}
        },
        {
            "name": f"Get {singular} by ID",
            "request": {"method": "GET", "url": {"raw": f"{base_url}/{resource}/:id"}}
        },
        {
            "name": f"Create {singular}",
            "request": {
                "method": "POST",
                "header": [{"key": "Content-Type", "value": "application/json"}],
                "body": {"mode": "raw", "raw": "{}"},
                "url": {"raw": f"{base_url}/{resource}"}
            }
        },
        {
            "name": f"Update {singular}",
            "request": {
                "method": "PUT",
                "header": [{"key": "Content-Type", "value": "application/json"}],
                "body": {"mode": "raw", "raw": "{}"},
                "url": {"raw": f"{base_url}/{resource}/:id"}
            }
        },
        {
            "name": f"Delete {singular}",
            "request": {"method": "DELETE", "url": {"raw": f"{base_url}/{resource}/:id"}}
        }
    ]

postman_collection = {
    "info": {
        "name": "Shinobi API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": []
}

postman_collection["item"].append({
    "name": "Login User",
    "request": {
        "method": "POST",
        "header": [{"key": "Content-Type", "value": "application/json"}],
        "body": {
            "mode": "raw",
            "raw": json.dumps({
                "email": "example@example.com",
                "password": "yourpassword"
            }, indent=4)
        },
        "url": {"raw": f"{base_url}/login"}
    }
})

for res in resources:
    postman_collection["item"].append({
        "name": res.replace("_", " ").title(),
        "item": create_crud_items(res)
    })

with open("shinobi_api_postman_collection.json", "w") as f:
    json.dump(postman_collection, f, indent=4)

print("✅ Collection saved as shinobi_api_postman_collection.json")
