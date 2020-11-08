print("1.")
print("Перша константа", False)
print("Друга константа", Ellipsis)
print("Третя константа",NotImplemented)
print("2.")

class Olyalya:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b
object = Olyalya()
print(vars(object))

number = 435
print(number, 'in hex =', hex(number))
print("3.")
for i in range(10):
    print(i)

a = 5
if a % 2 == 0 :
    print("число парне")
else:
    print("число непарне")

print("4.")

a = 1
b = '2'
try:
    print("Що буде, якщо", a + b, "?" )
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

print("5.")

with open('file.txt', 'w') as opened_file:
    opened_file.write('Hello world')

print("6.")

this_is_lambda = lambda first, last: f'Цей код написала: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Оля', 'Вальчак'))

print("6.")

def funct(x):
  if x:
    a=[i for i in range (0,101) if i%2==0 ]
    print(a)
  else:
    a=[i for i in range(1,100) if i%2==1]
    print(a)