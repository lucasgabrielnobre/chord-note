import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    file = open("assets/menu.txt")
    return file.read()
def logo():
    file = open("assets/logo.txt")
    return file.read()

def listarMusicas():
    arquivo = open("data/musicas.txt", "r")
    linhas = arquivo.readlines()
    for musica in linhas:
        dados = musica.split(";")
        id = dados[0]
        nome = dados[1]
        print(id, "-", nome)

def criarMusica():
    id = input("Digite o id da musica: ")
    nome = input("Digite o nome da música: ")
    file = open("data/musicas.txt", "a")
    file.write(id + ";" + nome + ";")
    print("Digite os acordes, cada linha é um compasso (0 para terminar): ")
    compasso = ""
    while True:
        compasso = input()
        if compasso == "0":
            break
        file.write(compasso + ";")
    file.write("\n")        
def main():
    clear()
    print(logo())
    print(menu())
    op = "1"
    while True:
        op = input("Digite uma opção: ")
        if op == '1':
            listarMusicas()
        if op == '2':
            pass
        if op == '3':
            criarMusica()
        if op == '4':
            pass
        if op == '5':
            pass
        if op == '0':
            break

if __name__ == "__main__":
    main()
