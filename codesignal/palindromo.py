def isPalindrome(inputString):
    rev = ''.join(reversed(inputString))
    if (inputString == rev): 
        return True
    return False

inputString = input("Palavra: ")
print(isPalindrome(inputString))