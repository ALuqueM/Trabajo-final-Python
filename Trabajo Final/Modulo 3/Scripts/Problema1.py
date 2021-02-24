def digit(string):
    x =len(string)
    y =0
    z =0
    if (x==0):
        return 0
    else:
        if (x%2==0):
            last=int(string[-1])
            z += last
            return z + digit(string[:-1])
        if int(string[0:2])>49 and int(string[0:2])<56:
            print('**MasterCard**')
        if string[0:2]=="34" or string[0:2]==37:
            print("**America Express**")
        if string[0]=="4":
            print("**VISA**")
        if string[0:2] in ["60","62","64","65"]:
            print("**Discover**")
        else:
            last=int(string[-1])
            last =2*last
            part_sum=last//10+last%10
            y+=part_sum
            
            return y + digit(string[:-1])
def luhns():
    string =input('Ingrese los 16 digitos de la tarjeta: ')
    total = digit(string)
    if (total % 10==0):
        print('Tarjeta Valida.')
    else:
        print('Tarjeta invalida.')

        
def confe():
    luhns()
    
print(confe())