import sys
import numpy as np
import matplotlib.pyplot as plt
import json

#Argumen check
if len(sys.argv) !=2 :
    print ("\n\nPenggunaan\n\trank-game.py [fileScore.json]\n")
    sys.exit(1)

#Argumen Store
sourceFile = sys.argv[1]

#read file
file = open(sourceFile).read()
list_data = file.split("\n")

#declaration
score=[]
produk=[]

top = json.loads(list_data[0])

for x in range(0, 20) :
    data = json.loads(list_data[x])
    temp_score = data['score'] / top['score']
    score.append(float(temp_score))
    produk.append(data['produk'])

# set ploting y
y_pos = np.arange(len(produk))

#create bar
plt.bar(y_pos, score, color='orange')

# Add title and axis names
plt.title("Top 20 Gaming Product Reviews 2018")
plt.xlabel('Product')
plt.ylabel('Score')

#insert word and rotate word
plt.xticks(y_pos, produk, rotation=45, horizontalalignment='right')

#set margin bottom
plt.subplots_adjust(bottom= 0.2)

#show histogram
plt.show()
