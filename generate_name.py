from faker import Faker
from faker.providers import BaseProvider
import csv
    
faker = Faker()

def get_first_name():
    return faker.unique.first_name()

def get_last_name():
    return faker.unique.last_name()

def generate_name():
    return [f"{get_first_name()} {get_first_name()} {get_last_name()}"]

with open('name_data.csv', 'w') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(['full_name'])
    for n in range(1,21):
        writer.writerow(generate_name())
        
