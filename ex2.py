
class Pizza:
  def __init__(self,name,ingridients):
    self.name=name
    self.ingridients=ingridients

  @classmethod
  def margarita(self):
    #self.name = 'Margarita'
    #self.ingridients = ['mozarella', 'tomatos', 'olives']
    new_pizza = Pizza('Margarita',['mozarella', 'tomatos', 'olives'])
    return new_pizza

  @staticmethod
  def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

marg = Pizza.margarita()
print(marg.name)


print(marg.calculate_area(50))
