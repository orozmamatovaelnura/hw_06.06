 
import random 

def decorator_povtor(main_func):
  def wrapper():
    for i in range(7):
      print(main_func())
  return wrapper

@decorator_povtor
def main_func():
  chislo=random.randint(1,100)
  return f'Ваше случайное число - {chislo}'


main_func()
