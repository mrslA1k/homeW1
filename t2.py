#вывести целую часть и остаток от деления выражения ((a^2+b^2)/(3b-4))/((4c^5)/6)
import math
#s1:str = str(input("Введите число a: "))
#s2:str = str(input("Введите число b: "))
#s3:str = str(input("Введите число c: "))
a:float = float(input("Введите число a: "))
b:float = float (input("Введите число b: "))
c:float = float (input("Введите число c: "))

#print(type(s1))
#res:float=0.0
#a=s1
#b=s2
#c=s3
res:float = (((a**2+b**2)/(3*b-4))/((4*c**5)/6))
print("Вариант 1")
print(f'целая часть {int(res)}, дробная часть {res%1}.')

print("Bye")
input("жмякни Интер для выхода")
