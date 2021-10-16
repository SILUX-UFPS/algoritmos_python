# Algoritmo para aplicar InsertionSort dado un array
# Inicialmente se tiene un solo elemento, que obviamente es un conjunto ordenado. Después, cuando hayk elementos ordenados de menor a mayor
# se toma el elemento k+1 y se compara con todos los elementos ya ordenados, deteniéndose cuando se encuentra un elemento menor 
# (todos los elementos mayores han sido desplazados una posición a la derecha) o cuando ya no se encuentran elementos 
# (todos los elementos fueron desplazados y este es el más pequeño).

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
