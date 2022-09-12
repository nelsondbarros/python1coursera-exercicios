def pPrimo(k):
    for z in range(2,k):
        if (k % z) == 0:
            return False
    return True

            
    

def maior_primo(x):
    k = x
    teste = pPrimo(k)
    while teste == False:
        k -= 1
        if pPrimo(k) == True:
            return k
