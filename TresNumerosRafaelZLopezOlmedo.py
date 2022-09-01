#entrada de datos
num=[0,0,0]

for i in range (3):
    o = i+1
    num[i] = input('inserta numero ' + str(o) + ' : ')
  
    i=0  

#validar datos sin repetir
for i in range (3):
 p=i+1
 for p in range (i+1,3,1):
        if(num[i]==num[p]):
            print('datos repetidos.')
            exit()
            
#ordenar datos
i=0
for i in range (len(num)):
    j=0
   
    for j in range (i+1,len(num),1):
        if(num[i]<num[j]):
            aux=num[i]
            num[i]=num[j]
            num[j]=aux

print('Resultado: ')
print(*num)