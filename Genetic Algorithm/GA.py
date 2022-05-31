# 5 Langkah AG, 1. Init Populasi, 2. Seleksi, 3. Reproduksi, 4. Elitism, 5. Output
#%%
# 1. Inisialisasi Populasi
 
# y = 15x - x^2
# [0, 0, 0, 0] -- [1, 1, 1, 1]
N = 3
rows, cols = (N, 4)
induk = [[0 for i in range(cols)] for j in range(rows)]
print (induk)

N_Anak = 6
rows, cols = (N_Anak, 4)
anak = [[0 for i in range(cols)] for j in range(rows)]
print (anak)

# Inisialisasi Paramater
Pc = 0.7
Pm = 0.3
#%%
import random

for i in range (N):
        a = random.randint(0, 15)
        induk[i] = [int (x) for x in '{0:04b}'.format(a)]
        print(a, induk[i])
#%%
# Buat function untuk cross over
def crossover(ind1 = [], ind2 = []):
    anak1 = [0, 0, 0, 0]
    anak2 = [0, 0, 0, 0]

    # ind1 = [0, 0, 0, 1] ind2 = [1, 0, 0, 1]
    # anak1 = [0, 0, 0, 1] anak2 = [1, 0, 0, 1]

    anak1[0] = ind1[0]
    anak1[1] = ind1[1]
    anak1[2] = ind2[2]
    anak1[3] = ind2[3]

    anak2[0] = ind2[0]
    anak2[1] = ind2[1]
    anak2[2] = ind1[2]
    anak2[3] = ind1[3]

    return anak1, anak2

# Buat function untuk mutasi
def mutasi(ind=[]):
    # ind1 = [0, 0, 0, 1] --> ind1 = [0, 1, 0, 1]
    ind[1] = 1 - ind[1]
    return ind

# Buat function untuk melakukan hitung Int
def hitungInt(ind = []):
    a = ind[3] * 1
    a = a + ind[2] * 2
    a = a + ind[1] * 4
    a = a + ind[0] * 8
    return a
    
# Buat function untuk melakukan hitung fitness
def hitungFitness(ind = []):
    a = hitungInt(ind)
    
    y = 15*a - a*a
    return y
#%%
# 2. Seleksi: tidak dilakukan, tetapi diambil semua


# 3. Reproduksi + 4. Elitism
i = 1
epochs = 50
MaxFitness = [0 for i in range(epochs)]
angkaFitness = [0 for i in range(epochs)]

# Hitung dulu nilai fitness untuk induk
for j in range (N):
    if (hitungFitness(induk[j]) > MaxFitness[0]):
        MaxFitness[0] = hitungFitness(induk[j])

print(MaxFitness)

# Melakukan perluangan sampai 'epochs' kali
while i < epochs:
    print("Iterasi: ", i)
  
    # Reproduksi
    a = random.random()
    if (a < Pc):
        # Cross over
        anak[0], anak[1] = crossover(induk[0], induk[1])
        anak[2], anak[3] = crossover(induk[0], induk[2])
        anak[4], anak[5] = crossover(induk[1], induk[2])
    else:
        # Mutasi
        for j in range(N):
            induk [j] = mutasi(induk[j])
    # ---------------------------------- end reproduksi

    # Elitism
    minFitness = 10000
    idx = 0 
    idxanak = 0
    # Cari minFitness (induk terburuk)
    for j in range(len(induk)):
        # print(minFitness, hitungFitness(induk[j]))
        if (hitungFitness(induk[j]) < minFitness):
            minFitness = hitungFitness(induk[j])
            idx = j  

    # Cari maxFit (anak terbaik)
    maxFit = 0
    for j in range(len(anak)):
        if (hitungFitness(anak[j]) > maxFit):
            maxFit = hitungFitness(anak[j])
            idxanak = j

    # Bandingkan individiual replacement
    if (minFitness < maxFit):
        induk[idx] = anak[idxanak]
    
    # Dari populasi induk yang baru mana yang paling baik
    for j in range(N):
        if (hitungFitness(induk[j]) > MaxFitness[i]):
            MaxFitness[i] = hitungFitness(induk[j])
    i+=1

    print(MaxFitness)

x = [i for i in range(epochs)]

import matplotlib.pyplot as plt
plt.plot(x, MaxFitness)