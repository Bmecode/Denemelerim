sözlük1={"bir":1,"iki":2,"üç":3,"dört":4}
print(type(sözlük1))
sözlük2={}
print(sözlük2)
sözlük2=dict()
print(sözlük2)
print(sözlük1["bir"])
sözlük1["beş"]= 5
print(sözlük1)
sözlük1["beş"]=10
print(sözlük1)
a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
print(a["iki"])
print(a["iki"][1][1])
a["üç"]+=5
print(a["üç"])
print(a)
a={'bir':1, 'iki':2,'üç':20}
a["dört"]= 4
print(a)
a = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
print(a["sayılar"]["bir"])
print(a["meyveler"]["kiraz"])
print(sözlük1)
print(sözlük1.keys())
print(sözlük1.values())
print(sözlük1.items())