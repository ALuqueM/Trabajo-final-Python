# Problema 1
x= int(input('Ingresar cantidad de ahorros en soles: '))
y= x+ (x*0.04)
y=round(y,2)
print('El primer año recibe: {}.'.format(y))
z= y+ (y*0.04)
z=round(z,2)
print('El segundo año recibe: {}.'.format(z))
a= z+ (z*0.04)
a=round(a,2)
print('El tercer año recibe: {}.'.format(a))

# Problema 2
import math
x= int(input('Ingrese primer coeficiente: '))
y= int(input('Ingrese segundo coeficiente: '))
z= int(input('Ingrese tercer coeficiente: '))
d= pow(y,2)-4*x*z
if d >=0:
    x1 = (-y+math.sqrt(d)/(2*x))
    x2 = (-y-math.sqrt(d)/(2*x))
    print('Primera Solucion:',x1)
    print('Segunda Solucion: ',x2)
else:
    print('No tinen solucion.')