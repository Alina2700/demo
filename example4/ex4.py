'''
Citim de la tastatura 3 valori int> a, b, c care ne descriu o ecuatie de gradul 2
Vrem sa aflam solutiile acestei ecuatii si sa aflam coordonatele punctului de min sau max al functiei aferente acestei ecuatii
'''
import math
# pasul 1. citim a, b si c
a= int(input("Introduceti valoarea pentru a: "))
b= int(input("Introduceti valoarea pentru b: "))
c= int(input("Introduceti valoarea pentru c: "))

'''
a*(x^2)+b*x+c=0
delta = b^2-4*a*c
x1,2=(-b +- sqrt(delta))/2a

'''
x1=-999
x2=-999
delta= b ** 2 - 4 * a * c
if delta >=0:
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)

print(x1, x2)

max_point=list() # x primul element, y al doilea element
min_point=list()
if a > 0: #functie convexa, tine apa----avem punct de minim
    min_point.append(-b/(2*a))
    min_point.append(-delta/(4*a))
    print(min_point)
elif a < 0: #functie concava, nu tine apa----este punct de maxim
    max_point.append(-b/(2*a))
    max_point.append(-delta/(4*a))
    print(max_point)



