import jmespath
import jsonpath


data = [
    {
        "name": "John",
        "age": 26,
        "address": {
            "street": "Main st",
            "city": "New York",
            "state": "NY",
            "zip": 10001,
            "country": "USA"
        },
        "job": {
            "position": "Manager",
            "salary": {
                "base": 50000,
                "bonus": 10000
            }
        }
    },
    {
        "name": "Mary",
        "age": 22,
        "address": {
            "street": "Second st",
            "city": "Chicago",
            "state": "IL",
            "zip": 60601,
            "country": "USA"
        },
        "job": {
            "position": "Assistant",
            "salary": {
                "base": 30000,
                "bonus": 5000
            }
        }
    },
    {
        "name": "Peter",
        "age": 33,
        "address": {
            "street": "Third st",
            "city": "Los Angeles",
            "state": "CA",
            "zip": 90001,
            "country": "USA"
        },
        "job": {
            "position": "Developer",
            "salary": {
                "base": 80000,
                "bonus": 15000
            }
        }
    },
    {
        "name": "Sarah",
        "age": 29,
        "address": {
            "street": "Fourth st",
            "city": "San Francisco",
            "state": "CA",
            "zip": 94103,
            "country": "USA"
        },
        "job": {
            "position": "Designer",
            "salary": {
                "base": 65000,
                "bonus": 10000
            }
        }
    },
    {
        "name": "Mike",
        "age": 35,
        "address": {
            "street": "Fifth st",
            "city": "Seattle",
            "state": "WA",
            "zip": 98109,
            "country": "USA"
        },
        "job": {
            "position": "Marketing",
            "salary": {
                "base": 75000,
                "bonus": 12000
            }
        }
    }
]


# 1. Get all the people who are older than 25 years old and print their names
old_people = jmespath.search('[?age > `25`].name', data)
print(old_people)

old_people = jsonpath.jsonpath(data, '$[?(@.age > 25)].name')
print(old_people)

old_people = [person for person in data if person['age'] > 25]
print([person['name'] for person in old_people])

# 2. Get all the people who live in California and print their names
california_people = jmespath.search('[?address.state == `CA`].name', data)
print(california_people)

california_people = jsonpath.jsonpath(
    data, '$[?(@.address.state == "CA")].name')
print(california_people)

california_people = [
    person for person in data if person['address']['state'] == 'CA']
print([person['name'] for person in california_people])

# 3. Get all the people who are older than 30 years old and live in California and print their names
california_old_people = jmespath.search(
    '[?age > `30` && address.state == `CA`].name', data)
print(california_old_people)

california_old_people = jsonpath.jsonpath(
    data, '$[?(@.age > 30 && @.address.state == "CA")].name')
print(california_old_people)

california_old_people = [person for person in data if person['age']
                         > 30 and person['address']['state'] == 'CA']
print([person['name'] for person in california_old_people])

# 4 Get all the people whose bonus is greater than 10000 and print their names
bonus_people = jmespath.search('[?job.salary.bonus > `10000`].name', data)
print(bonus_people)

bonus_people = jsonpath.jsonpath(data, '$[?(@.job.salary.bonus > 10000)].name')
print(bonus_people)

bonus_people = [person for person in data if person['job']
                ['salary']['bonus'] > 10000]
print([person['name'] for person in bonus_people])

# 5. Get all the people whose salary base is greater than 70000 and live in state CA and print their names
base_CA_people = jmespath.search(
    '[?job.salary.base > `70000` && address.state == `CA`].name', data)
print(base_CA_people)

base_CA_people = jsonpath.jsonpath(
    data, '$[?(@.job.salary.base > 70000 && @.address.state == "CA")].name')
print(base_CA_people)

base_CA_people = [person for person in data if person['job']
                  ['salary']['base'] > 70000 and person['address']['state'] == 'CA']
print([person['name'] for person in base_CA_people])

# 6. Get all the people whose first number of zip code is 9 and print their names use regex
zip_9_people = jmespath.search(
    '[?starts_with(to_string(address.zip), to_string(`9`))].name', data)
print(zip_9_people)

zip_9_people = jsonpath.jsonpath(
    data, '$[?(str(@.address.zip)[0] == "9")].name')

print(zip_9_people)

zip_9_people = [person for person in data if str(
    person['address']['zip'])[0] == '9']
print([person['name'] for person in zip_9_people])

