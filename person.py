#person.py
class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('내 이름은 '+self.name)
