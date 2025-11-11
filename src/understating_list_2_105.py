"""
  slicing a list

"""
players= ["charles", "martina","michel","florence", "eli"]
print("list original :", players)

print("slice de lista original",players[0:3])
print("slice de lista original", players[1:4]) 
print("slice de lista original", players[:4])
print("slice de lista original", players[2:])
print("slice de lista original", players[-3:]) # ultimos 3 elementos
print("slice de lista original", players[5:2])
print("slice de lista original", players[-3:-1])

"""
slincing en un for
"""
players= ["charles","martina", "michel","florence","eli"]
print("aqui se presenta los primeros  3 jugadores del equipo ")
for players in players[0:3]
    print(players.tittle() )

"""
copia una lista
"""
my_foods= ["pizza","tacos","falutas","goriditas"]
#my_foods_copy= my_foods #error eswa no es la manera
my_foods_1= my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3=list(my_foods)

