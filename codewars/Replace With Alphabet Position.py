def alfabet_position(text):
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    frase = list(text.lower())
    a = 0
    new_text = []

    for i in frase:
        if i in alfabet:
            position = alfabet.index(frase[a])
            new_text.append(position+1)
        a+=1    
    
    text = ' '.join(map(str, new_text)) 

    return text

text = input("digite a frase: ")
print (alfabet_position(text))

