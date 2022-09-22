""" 3. Observe o programa abaixo:
    number = int(input("Digite um número: "))
    print("O número digitado foi:" , number)
Reescreva esse código de uma forma com que ele seja capaz de tratar a inserção 
de um caractere por parte do usuário"""

import logging

logging.basicConfig(level="ERROR")

def number_validate(number):
    if number < 0:
        raise ValueError("O número digitado deve ser positivo.")
        
def number_insert():
    try:
        number = int(input("Digite um número: "))
        number_validate(number)
        print("O número digitado foi: " , number)
    except ValueError:  
        print("Número digitado não é válido")
        logging.error("Número digitado não é válido")
        return
        