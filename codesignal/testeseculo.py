def centuryFromYear(year):
    century = year // 100
    century1 = year%100
    if century1 >=1:
        century +=1

    return century

ano = input("Digite ano: ")

year = int(ano)

print("Esse ano é século: ", centuryFromYear(year))