


"""
UNA LISTA Y UN DICCIONARIO

dict = {'name' : 'Paula' , 'lastname' : 'Scatarelli', 'age' : '47', 'job' : 'yoga teacher' }

list = [47, 'yoga teacher', 1974 , 55.6, 1.7 , 'India']

IMPRIMO EL DICT

for key,value in dict.items():
    print(key, ' ',value)

------------------------------------
IMPRIMO LA LISTA

for i in list:
    print(i)

IMPRIMO UN ELEMENTO DE LA LISTA
#print(list[1])


IMPRIMO LA PRIMERA LETRA DE CADA KEY Y DE CADA VALUE XD
#for key,value in dict.items():
    #print(key[0], ' ', value[0]) """






superlist = [{'name' : 'Paula' , 'lastname' : 'Scatarelli'},
{'name' : 'Manuela' , 'lastname' : 'Tomassetti'},
{'name' : 'Moki' , 'lastname' : 'Scatarelli'},
{'name' : 'Tiffany' , 'lastname' : 'Tomassetti'}
   ] 
    
for i in superlist:
    print(i['name'], ' ', i['lastname']) 
    
# Lo de arriba imprime el contenido de cada llave y valor despojados de llaves

"""
Paula   Scatarelli
Manuela   Tomassetti
Moki   Scatarelli
Tiffany   Tomassetti

"""
