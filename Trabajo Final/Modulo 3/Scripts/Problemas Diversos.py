def ingresar_nota():
    while True:
        try:
            nota= float(input('Introduce la nota (0-10): '))
            if nota>=0 and nota<=10:
                return nota
            else:
                print('Nota fuera de rango.')
        except:
            print('Ha ocurrido un error, introduce bien la nota')
        
def listar_alumnos (cantidad_alumnos):
    lista_alumnos =[]
    for i in range (n):
        alumno={}
        alumno['nombre']= input('Ingrese el nombre del alumno {}:'.format(i+1))
        alumno ['nota1'] = ingresar_nota()
        alumno ['nota2'] = ingresar_nota()
        alumno ['nota3'] = ingresar_nota()
    
    
        lista_alumnos.append(alumno)
    return lista_alumnos
n = int(input('Cantidad de alumnos a Ingresar: '))

lista_alumnos =listar_alumnos(n)

a= int(input('Indique de que acuerdo al orden que ingreso que alumno quiere ver si esta aprobado:'))
a=a-1
def aprobado(z):
    aprobados=[]
    for x in range(1,n+1) :
        y=int((lista_alumnos[z]['nota1']+lista_alumnos[z]['nota2']+lista_alumnos[z]['nota3'])/3)
        if y>4:
            print(lista_alumnos[z]['nombre'])
            print('Aprobado')
            aprobados.append(lista_alumnos[z]['nombre'])
        else:
            print(lista_alumnos[z]['nombre'])
            print('Desaprobado')
    
    return 
x= aprobado(a)
print(x)

a= int(input('Indique de que acuerdo al orden que ingreso que alumno quiere ver su promedio:'))-1

def promedio(z):
    promedio=[]
    for x in range(1,n+1) :
        y=(lista_alumnos[z]['nota1']+lista_alumnos[z]['nota2']+lista_alumnos[z]['nota3'])/3
        print(lista_alumnos[z]['nombre'])
    
    return y

y=promedio(a)
print(y)