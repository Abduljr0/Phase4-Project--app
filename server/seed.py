from random import choice, choices, randint
import faker

from models import SearchIcon,HomePage,Login, db

fake = faker.Faker()

from app  import app

with app.app_context():
    
    SearchIcon.delete()
    HomePage.query.delete()
    Login.query.delete()

    for n in range(30):
        fake_name=  fake.name()
        address= fake.address()

        
        SearchIcon = HomePage(name=fake_name ,address=address)
        db.session.add(Login)
        db.session.commit()



    Login= []

    print(Login)
    db.session.add_all(Login)
    db.session.commit()

    for record in range(15):
        rnd_rest=choice([x.id for x in SearchIcon.query.all()])
        rnd_pizza= choice([p.id for p in  Login.query.all()])
        db.session.add(SearchIcon)  
        db.session.commit()

    