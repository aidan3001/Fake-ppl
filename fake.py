import random

fname = ['Aidan', 'James', 'Kaden', 'syd', 'Micah', 'Angie', 'Eli', 'Shawn', 'Zane', 'Tim', 'Jeff', 'Tatiana', 'Emily', 'Jacob', 'Stan', 'Molly', 'Violet', 'Juan', 'Dayana', 'William']
lname = ['Testa', 'Smith', 'John', 'Apple', 'Throckmorton', 'Day', 'Brown', 'Jones', 'Miller', 'Lopez', 'Wilson', 'Jackson', 'White', 'Sanchez', 'Clark', 'Nguyen', 'Green', 'Torres', 'Scott', 'Parker']
street = ['Oak', 'Pine', 'Cedar', 'Maple', 'Elm', 'Hill', 'Lake', 'Second', 'Cherry', 'Cardinal', 'Liberty', 'Walnut', 'Hickory', 'Creek', 'Sunset', 'Church', 'Main', 'Abbey', 'Laurel', 'Balls']
city = ['Little Elm', 'Dallas', 'Fort Worth', 'Little Rock', 'Houston', 'Frisco', 'Sanger', 'Denton', 'Plano', 'Arkedelphia', 'Texarkana', 'Midland', 'Kerrville', 'Odesa', 'Kemp', 'Paris', 'Aubrey', 'Azle', 'Carrolton', 'The Colony']
state = ['TX', 'NY', 'FL', 'OK', 'WA', 'OR', 'CA', 'NM', 'CO', 'KS', 'ND', 'SD', 'TN', 'MI', 'AL', 'GA', 'AR', 'LA', 'IL', 'NC']


for num in range(20) :
    firstname = random.choice(fname)
    lastname = random.choice(lname)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    streetnum = random.randint(100,999)
    streetn = random.choice(street)
    cityn = random.choice(city)
    staten = random.choice(state)
    zip = random.randint(10000, 99999)
    address = f'{streetnum} {streetn} St., {cityn} {staten} {zip}'

    email = firstname.lower() + lastname.lower() + '@coldmail.com'

    print(f'{firstname} {lastname}\n{address}\n{email}\n')