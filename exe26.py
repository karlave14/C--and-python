print("How old are you?", end=' ') #Impresión de salida
age = input() #entra la variable
print("How tall are you?", end=' ') #solo salida 
tall = input() # se agrego la entrada de la variable tall 
print("How much do you weigh?", end=' ') # faltaba un parentesis 
weight = input() #entrada de la variable 

print(f"So, you're {age} old, {tall} tall and {weight} heavy.") #cambiar el nombre 

from sys import argv # importar biblioca para los comandos de argv y menejar el script  
script, filename = "argv"

txt = open(filename) #corregir la palabra a filename

print("Here's your file {filename}:")
print(txt.read()) #escribir bien el txt 

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again_read())


print("Let's practice everything.") # debe ser con comillas dobles
print('You\'d need to know \'bout escapes with \\ that do:') #linea corregida junta
print(' \n newlines and \t tabs.') #otra linea separada

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #cerrar comillas
print(poem)
print("--------------") #abrir comillas


five = 10 - 2 + 3 - 6 #agregar el 6 
print(f"This should be five: {five}") #cerrar print

def secret_formula(started): #añadir :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 #dividirlo 
    return jelly_beans, jars, crates


start_point = 10000
beans, jars = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") #cerrar print

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: #cerrar con : 
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #cerrar con : 
    print("People are less than or equal to dogs.") #cerrar comillas dobles ""


if people == dogs: #agregar == boleean 
    print("People are dogs.")

