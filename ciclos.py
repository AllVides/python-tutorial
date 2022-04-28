cond = 0
while ( cond  < 10 ):
    print(cond)
    cond += 1

# el ciclo for unicamente va a ciclar dentro de un dato iterable dado
print ("cilo for")
mylist = [1,5,89,63,7,0,5]
for s in mylist:
    #instrucciones
    print( s )

mystring = "esto es una oracion"
for s in mystring:
    #instrucciones
    print( s )
print ("cilo for dict /n/n")
mydict = {"hola":1 , "adio": 2}
for s in mydict:
    #instrucciones
    print( s , mydict[s])
