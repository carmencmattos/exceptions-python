""" 2. Faça um programa que calcule a divisão de dois números m e n e trate os casos em
que n = 0.""" 

import logging

logging.basicConfig(level="INFO", filename="logs_example.log")

try:
    m = int(input("Numerador: "))
    n = int(input("Denominador: "))
    result = m / n
    logging.info(result)
    print(f"O resultado é {result}")
    
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
    logging.error("Não é possível dividir um número por zero")
    
except (ValueError, TypeError):
    print("Erro nos tipos de dados que você digitou")
    
except KeyboardInterrupt:
    print("Dados não informados")
    
finally:
    print("Obrigada!")