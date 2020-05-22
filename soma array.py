#
# Complete the simpleArraySum function below.
#

ar = 0

def simpleArraySum(ar):
    index = input("get index: \n")
    a = 0
    array= []
    while a < int(index):
        number = input("number: ")
        array.append(int(number))
        a+=1
    
    ar = sum(array)
    return ar

soma = simpleArraySum(ar) 
print(soma)


