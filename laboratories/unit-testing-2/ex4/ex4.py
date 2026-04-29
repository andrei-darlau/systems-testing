#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 

from dataclasses import dataclass
from faker import Faker
import random
fake = Faker()

@dataclass()
class Person:
    name: str
    age: int
    email: str

people: dict = {}

for i in range(500):
    name = fake.name()
    email = fake.email()
    age = fake.random_int(min=1, max=100)
    people[email] = Person(name, age, email)

random_people = random.sample(list(people.values()), 3)

for person in random_people:
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")
