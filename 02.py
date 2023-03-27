##2
num1 = int(input("Qual o primeiro número?"))
num2 = int(input("Qual o segundo número?"))
def multiplo(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
print(multiplo(num1,num2))