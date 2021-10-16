# Algoritmo de coeficiente binomial
# Numero de formas de seleccionar k elementos de n elementos

def binomialCoeff(n , k):

	if k==0 or k ==n :
		return 1

	return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)
