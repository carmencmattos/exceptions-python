""" 7. Uma colega tentou executar o seguinte programa:
file = open("file.txt", "r")
file_lines = file.readline()
file.close()
E obteve a seguinte mensagem de erro: FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
Reescreva o código para que esse erro seja exibido de forma mais clara e amigável."""

try:
    file = open("file.txt", "r")
    file_lines = file.readline()
    file.close()

except FileNotFoundError:
    print("Este arquivo não foi encontrado.")