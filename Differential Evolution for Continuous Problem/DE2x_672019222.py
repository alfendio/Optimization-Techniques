# Import Library
import numpy as np
import random
import matplotlib.pyplot as plt

# Inisialisasi parameter
D = 2 
CR = 0.90 
F = 0.5 
ukuranPopulasi = 5 
BL = -10 
BU = 10 
epochs = 10 

# Inisialisasi populasi 
def initPopulasi(ukuranPopulasi, D, BU, BL):
    
    parent = np.empty([ukuranPopulasi, D])
    for i in range(ukuranPopulasi):
      for j in range(D):
        parent[i][j] = random.random()*(BU - BL) + BL
    return parent

parent  = initPopulasi (ukuranPopulasi, D, BU, BL)
print(parent)

# Sphere 
def Sphere(populasi):
    sz = populasi.shape
    ukuranPopulasi = sz[0]
    dimensi = sz[1]

    Fobj = np.empty(ukuranPopulasi)

    for i in range(ukuranPopulasi):
        d = 0
        for j in range(dimensi):
            d = d + populasi[i][j]**2
        Fobj[i] = d
    return Fobj

Fobj = Sphere(parent)
print(Fobj) # kualitas individu dalam populasi awal

# Crossover
def Crossover(populasi, F, j):
    sz = populasi.shape
    ukuranPopulasi = sz[0]
    dimensi = sz[1]

    random1 = random.randint(0, ukuranPopulasi-1)
    random2 = random.randint(0, ukuranPopulasi-1)
    random3 = random.randint(0, ukuranPopulasi-1)

    while random1 == random2:
      random2 = (random2 + 1)%ukuranPopulasi

    while random3 == random1 or random3 == random2:
      random3 = (random3 + 1)%ukuranPopulasi

    resultCrossover = parent[random3][j] + F*(parent[random1][j] - parent[random2][j])
    
    return resultCrossover

resultCrossover = Crossover (parent, F, 1)
print(resultCrossover)

# Prosedur DE
parent = initPopulasi(ukuranPopulasi, D, BU, BL)
print(parent)

Fobj = Sphere(parent)
print(Fobj) 

U = np.empty((1, D))

bestFobj = np.empty((epochs+1))
bestFobj[0] = Fobj.min()

for it in range(epochs):
    
    for i in range (ukuranPopulasi):
        for j in range (D):
            U[0][j] = parent[i][j]

        jrand = random.randint(0, D)

        for j in range (D):
            if random.random() < CR or j == jrand:
              resultCrossover = Crossover(parent, F, j)
              U[0][j] = resultCrossover
        
        # Replacement
        FobjU = Sphere(U)

        if FobjU < Fobj[i]:
            Fobj[i] = FobjU
            for j in range (D):
                parent[i][j] = U[0][j]
    bestFobj[it+1] = Fobj.min()

print(bestFobj)

# Plot
plt.plot(bestFobj)
plt.xlabel('Epochs')
plt.ylabel('Fobj')
plt.show()