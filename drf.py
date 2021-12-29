import requests
#
# user = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(user.json())
# print(dir(user))
import json

#
# name = {'name':'johan'}
# _json = json.dumps(name)
# print(type(_json))
# print(_json)
# _dict = json.loads(_json.encode())
# print(_dict, type(_dict))
#
# with open('first_json.json', 'w') as file:
#     name=json.dumps(name, indent=4)
#     file.write(name)
#
# d = ''
# with open('first_json.json', 'r') as file:
#     d=json.load(file)
#
# print(d)


# class A:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.username = username
#         self.email = email
#
#     def get_name(self):
#         return self.name
#
#
# user = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(type(user.text))
# a1 = user.json()
# print(type(a1))
# a = A(a1['name'], a1['username'], a1['email'])
# print(a.get_name())
# res = json.dumps(a.__dict__)
# print(res)

d = {'id':1, 'name':'Johan'}
c = {'name': 'nasa'}
# _json = json.dumps(d)
print(d | c)