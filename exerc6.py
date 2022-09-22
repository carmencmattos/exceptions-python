#6. Observe o seguinte programa:
try:
    number_1 = float(input("Insira um número: "))
    number_2 = float(input("Insira outro número: "))
    result = number_1 / number_2
        
    print ("Resultado: {:.2f}".format(resultado)) # "resultado" is not defined Pylance(reportUndefinedVariable) 
except ValueError:
    print("Isso não é um número.")
except ZeroDivisionError:
     print("Divisão por 0 indeterminada.")
except:
    print("Algo deu errado.")
        
#Escreva o que será impresso na tela caso o mesmo seja executado com as 
#seguintes entradas (5, 3):
    #Insira um número: 5
    #Insira outro número: 3
    #Algo deu errado.  
 