#вывести целую часть и остаток от деления выражения ((a^2+b^2)/(3b-4))/((4c^5)/6)
a:float = float(input("Введите число a: "))
b:float = float (input("Введите число b: "))
c:float = float (input("Введите число c: "))

res1:float = ((a**2+b**2)/(3*b-4))
res2:float = ((4*c**5)/6)

print(f'целая часть от деления {res1} на {res2} -  {res1//res2}, дробная часть {res1%res2}.')

print("Bye")
input("жмякни Интер для выхода")
