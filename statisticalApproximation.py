# Zombie: 370,28,886
# Spider: 365,37,945
# Spider: 359,39,917
# Spider: 381,42,917
# Spider: 351,44,931
# Zombie: 362,44,891
# Spider: 408,44,927
# Spider: 429,35,897

# Mean: 378.125,39.125,913.875
import statistics
import math

somX = 0
somY = 0
somZ = 0

spawnersX = []
spawnersY = []
spawnersZ = []
elementen = 0

q1 = 0
q3 = 0

gemX = 0
gemY = 0
gemZ = 0

# array with all the spawners
spawners = [(370, 28, 886), (365, 37, 945), (359, 39, 917), (381, 42, 917),
            (351, 44, 931), (362, 44, 891), (408, 44, 927), (429, 35, 897)]

for i in spawners:
	spawnersX.append(i[0])
	spawnersY.append(i[1])
	spawnersZ.append(i[2])

spawnersX.sort()
spawnersY.sort()
spawnersZ.sort()

elementen = len(spawnersX)

q1 = elementen // 4
q3 = q1 * 3

elementen = q1 * 2

for i in range(q1):
	spawnersX.pop()
	spawnersX.pop(0)
	spawnersY.pop()
	spawnersY.pop(0)
	spawnersZ.pop()
	spawnersZ.pop(0)

for i in spawnersX:
	somX += i   

for i in spawnersY:
    somY += i
    
for i in spawnersZ:
    somZ += i

gemX = somX // elementen
gemY = somY // elementen
gemZ = somZ // elementen

print("Coordinaten: ", gemX, " ", gemY, " ", gemZ)
