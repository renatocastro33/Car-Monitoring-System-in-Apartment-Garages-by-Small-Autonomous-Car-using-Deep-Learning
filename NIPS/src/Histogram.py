#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/adminhpc/Escritorio/NIPS/PAPER3.csv') # Importing the csv file 
x = dataset.iloc[:,0].values # License Plate
y = dataset.iloc[:,1].values # Confidence


X = [] # License Plate
Y = {} #Dictionary License plate -> Total Confidence

# Unique Plates List
for _ in x:
    X.append(_)
X = set(X)

# Unique Plates and Total Confidence Dictionary
for _ in X:
    suma = 0
    for i in range(len(x)):
        if(x[i] == _):
            suma += y[i]
    Y[_] = suma

# Creating Variables to plot
a = []
b = []

for i in Y:
    a.append(i)
    b.append(Y[i])
    
# Plotting the histogram
plt.barh(a,b,align = 'center') # A bar chart horizontal
plt.ylabel('License Plate Candidate')
plt.xlabel('Total Confidence of each candidate')
plt.show()
