liste1 =  [1,2,3,4,5]
liste2 =  [6,7,8,9,10]
liste3= liste1 + liste2
liste3= (liste3+["Burak"])
print(liste3)
liste3[0]=111
print(liste3)
liste1[:2]=[10,11]
print(liste1)
liste2=liste2*2
print(liste2)
liste = [3,4,5,6]
liste.append(7)
print(liste)
liste = [1,2,3,4,5]
print(liste.pop())
print(liste)
eleman= liste.pop(2)
print(liste)
liste = [34,1,56,334,23,2,3,19]
liste.sort() # Küçükten büyüğe sıralar.
print(liste)
liste.sort(reverse = True) # Büyükten küçüğe sıralar.
print(liste)
liste = ["Elma","Armut","Muz","Kiraz"]
liste.sort() # Alfabetic olarak küçükten büyüğe
print(liste)
liste = ["Elma","Armut","Muz","Kiraz"]
liste.sort(reverse = True) # Alfabetic olarak büyükten küçüğe
print(liste)