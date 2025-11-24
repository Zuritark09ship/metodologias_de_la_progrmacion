#empy ditionary

from tokenize import Name


homer_0={"color": "yelow",
    "bag":"homer-donut", 
    "hair": "black",
    "Dress":"casual",}
print(homer_0)
print(type(homer_0))

marge_0={"color": "yelow",
    "bag":"homer-donut",
    "hair": "blue", 
    "Dress":"casual",}
scar_0={"color": "yelow",
    "headshot":1.5,}

print(marge_0["bag"])
print(marge_0["color"])

#agregar elemenosa un diccionario 

homer_0["x-posicion"]=15
homer_0["y-posicion"]=20
homer_0["z-posicion"]=10
print(homer_0)  

alien_2=["color": "blue"] 
alien_2["x-position"]= 0
alien_2["y-position"]= 25
print(alien_2)

Name["name"] = "paul"

for key, value in alien_2.items():
    print(f"the key{key} has value {value}")
    
##lopping thoung keys}
for key in alien_2.keys():
    print(key)

##looping though items
for item in alien_2.items():
    print(item)