#Dados N articulos, cada uno con su propio valor y peso y un tamaño maximo de una mochila, se debe calcular el valor maximo de los elementos que es posible llevar.
#Debe seleccionarse un subconjunto de objetos, de tal manera que quepan en la mochila y representen el mayor valor posible.

def knapSack(W, wt, val, n): 

    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 

    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1)) 
                   
