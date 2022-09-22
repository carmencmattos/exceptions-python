""" 1. Faça um programa que calcule a raiz quadrada de um número n e trate os casos em que n < 0.
OBS: Utilize o módulo math para calcular a raiz quadrada."""

from math import sqrt

def square_root():
    try:
        n = float(input("Digite o número que você quer calcular a raiz quadrada: "))     
        square_root = sqrt(n) 
        print(f'A raiz quadrada do número digitado é {square_root}')  
        
    except ValueError:  
        print("Não é possível extrair a raiz quadrada de um número negativo")
        