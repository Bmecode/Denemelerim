liste1=[1,2,3,4,5]
liste2= list()

for i in liste1:
    liste2.append(i)
print(liste2)

liste3=[1,2,3,4,5]
liste4=[i for i in liste3]
print(liste4)

liste=[3,4,5]
listee=[i *2 for i in liste]
print(listee)