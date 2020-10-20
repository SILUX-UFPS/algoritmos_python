#Unión de 2 vectores de longitud n, para crear un tercer vector con los elementos de ambos ordenados ascendentemente
def union(arrA,arrB):
     c = []
     j = 0
     k = 0
     for i in range(0,len(arrA)+len(arrB),2):
                          if(arrA[j] < arrB [k]):
                                  if(j<len(arrA)):
                                         c.append(arrA[j])
                                         j = j+1
                                  if(k<len(arrB)):
                                         c.append(arrB[k])
                                         k= k+1
                          else:
                                  if(k<len(arrB)):
                                        c.append(arrB[k])
                                        k = k+1
                                  if(j<len(arrA)):
                                        c.append(arrA[j])
                                        j = j+1

     c.sort()
     return c




a = [0,1,2,4]
b = [3,5,6,7]

c=union(a,b)

print(c)
