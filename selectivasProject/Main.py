#Simple
a = 33
b = 200
if b > a:
    print(b, " es mayor que " ,a)

#Doble
y = 200
z = 33
if y > z:
    print(y, " es mayor que " ,z)
else:
    print(z, " no es mayor que " ,y)

#Multiple
c = 200
d = 207
if c > d:
    print(c, " es mayor que " ,d)
elif c < d:
    print(c, " es menor que " ,d)
else:
    print(c, " es igual que " ,d)

#Condiciones Enlazadas
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")


#parametro END
print("estudiar los sabados", end=' ')
print("es genial")
print("estudiar los sabados")
print("es genial")

#parametro SEP
print("Daniela", "Luis", "Carlos", "Camila")#agrega un espacio por defecto
print("Daniela", "Luis", "Carlos", "Camila", sep="")#quita el espacio
print("Daniela", "Luis", "Carlos", "Camila", sep=",")#agrega una coma

print("Daniela", "Luis", "Carlos", "Camila", sep="_", end="_Curso_Python")#implementacion end y sep
