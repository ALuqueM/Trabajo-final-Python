n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])

from modulo import datos
import re
# Cadena entrada
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
print(s)

patron = r"@robot\d"

print(re.findall(r"@robot\w", s))

# Cadena entrada
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
print(s)

patron = r"User_mentions:\d"
print(re.findall(r"User_mentions:\d", s))

patron = r"likes:\d"
print(re.findall(r"likes: \d", s))

patron = r"number of retweets:\d"
print(re.findall(r"number of retweets: \d", s))

analisis_sentimientos = datos.read_pandas(path,780,782)

#regex = r""  # complete aqui
for tweet in analisis_sentimientos:
    print(tweet)
    
    # Encuentre todos los casos
    #print(re.findall(regex, tweet))

re.findall(r"\s\w+.txt$",tweet)
# cadena de texto finaliza con 'the (num)s'


# Escriba una expresión regular para validar un correo
regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   

