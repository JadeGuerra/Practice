#multiplica os maiores adjacentes do array entre si 
# e retorna o maior produto
#TODO o resultado do maior número está trabalhando por módulo ao invés de 
#trabalhar o valor da reta.

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
        print(inputArray[a], inputArray[b])  
        print(multiply)      
        a+=1
        b+=1
    return bigger

inputArray = [-23, 4, -3, 8, -12]

print(multiplica(inputArray))