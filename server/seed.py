from app import app, db
from models import Foods  ,Driver
import json

def seed_foods():
    with app.app_context():
        # Open the JSON file containing the food data
        with open('db.json', 'r') as file:
            foods_data = json.load(file)

        # Iterate over the food data and add each item to the database
        for food in foods_data['foods']:
            new_food = Foods(
                name=food['name'],
                description=food['description'],
                category=food['category'],
                price=food['price']
            )
            db.session.add(new_food)

        # Commit the changes to the database
        db.session.commit()
print("food seeded successfully")


drivers_data = [
    {
        'name': 'John Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'address': '123 Main St, Anytown, USA'
    },
    {
        'name': 'Jane Smith',
        'contact': '234-567-8901',
        'email': 'jane.smith@example.com',
        'address': '456 Oak Ave, Othercity, USA'
    },
    {
        'name': 'Jim Brown',
        'contact': '345-678-9012',
        'email': 'jim.brown@example.com',
        'address': '789 Pine Dr, Someville, USA'
    },
    {
        'name': 'Jake White',
        'contact': '456-789-0123',
        'email': 'jake.white@example.com',
        'address': '101 Elm Blvd, Everytown, USA'
    },
    {
        'name': 'Jess Black',
        'contact': '567-890-1234',
        'email': 'jess.black@example.com',
        'address': '111 Maple Ln, Somecity, USA'
    },
    {
        'name': 'Jill Green',
        'contact': '678-901-2345',
        'email': 'jill.green@example.com',
        'address': '222 Birch Rd, Othertown, USA'
    },
    {
        'name': 'Jamie Blue',
        'contact': '789-012-3456',
        'email': 'jamie.blue@example.com',
        'address': '333 Walnut Way, Anysuburb, USA'
    },
    {
        'name': 'Joy Red',
        'contact': '890-123-4567',
        'email': 'joy.red@example.com',
        'address': '444 Cedar Ct, Otherville, USA'
    },
    {
        'name': 'Jack Purple',
        'contact': '901-234-5678',
        'email': 'jack.purple@example.com',
        'address': '555 Willow Way, Somesuburb, USA'
    },
    {
        'name': 'Jade Orange',
        'contact': '012-345-6789',
        'email': 'jade.orange@example.com',
        'address': '666 Oak Ln, Everysuburb, USA'
    }
]





def seed_drivers():
    with app.app_context():
      for name, phone, email, address in drivers_data:
        driver = Driver(name=name, contact=phone, email=email, adress=address)
        db.session.add(driver)
        db.session.commit()




if __name__ == '__main__':
    seed_foods()
    seed_drivers()

