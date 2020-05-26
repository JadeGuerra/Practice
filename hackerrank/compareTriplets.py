#resolvido diretamente na plataforma

def compareTriplets(a, b):
    ind = 0
    alice = 0
    bob = 0
    array_points = []
    for i in a:
        if a[ind] > b[ind]:
            alice +=1
        elif a[ind] < b[ind]:
            bob +=1
        ind +=1
    
    array_points.append(alice)
    array_points.append(bob)

    return array_points