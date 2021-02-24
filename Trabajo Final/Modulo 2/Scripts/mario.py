def mario():
    try:
        n =int(input('Introduce el numero de reglones del triangulo: '))
        if n>=1 and n <=8:
            for i in range(n+1):
                vacio = n-i
                x= ' '*vacio+'#'*i
                print(x)
                
    except:
        print('No es un dato admitido')
        mario()
print(mario())