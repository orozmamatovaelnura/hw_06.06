class Person:
  def __init__(self,name):
    self.name=name

  def show_name(self):
    return f'My name is {self.name}'

  
def strange_func(*args):
  for arg in args:
    try:
      print(arg.show_name())
    except:
      print("У данного аргумента нет имени")

john = Person('John')
alice = Person('Alice')
charlie = Person('Charlie')

strange_func(john,alice,charlie)
