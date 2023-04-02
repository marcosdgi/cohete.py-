cantidad = 10
print ("*")
cadena = ""
i = 1
while i < cantidad :

    for j in range(0,i):
      
        cadena += (str(j))

    if len(cadena) %2 !=0:
        print ("*" +cadena + "*")
    
                    
   
    i+=1
    cadena = ""


