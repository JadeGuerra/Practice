#multiplica os maiores adjacentes do array entre si 
# e retorna o maior produto

def multiplica(inputArray):
    multiply = 0
    bigger = 0
    a = 0
    b = 1
    while b < len(inputArray):    
        #multiplica os elementos do array
        multiply = inputArray[a] * inputArray[b]
        if multiply > bigger:
            bigger = multiply        
        a+=1
        b+=1
    return bigger

inputArray = [3, 6, -2, -5, 7, 3]

print(multiplica(inputArray))