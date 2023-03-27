##1
num1 = int(input("Qual o primeiro número?"))
num2 = int(input("Qual o segundo número?"))
def maximo(num1,num2):
    if num1 > num2:
        return (num1)
    else:
        return (num2)
print(maximo(num1,num2))
