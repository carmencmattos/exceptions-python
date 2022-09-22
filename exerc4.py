""" 4.Observe o seguinte programa:
    number = int(input("Digite um número: "))
    print("O número digitado foi: ", n)
Tendo em mente que ao executá-lo a exceção NameError é gerada, reescreva o 
código de forma com que tal exceção seja tratada."""

try:
    number = int(input("Digite um número: "))
    print(f"O número digitado foi: {number}")   
    
except NameError:  
        print("Variável não definida")
        