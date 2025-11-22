#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

#CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)
MIN_LENGTH= 9
firt_name= input("seet your firts name :").strip()

if firt_name== "":
    print("ERROR: you did not enter your name")
elif len(firt_name) < MIN_LENGTH:
    print("your  name is too short")
else:
    print("your name is :", firt_name.title())
