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
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    for linha in linhas:
        dados = linha.split(";")
        id = dados[0]
        nome = dados[1]
        print(id, "-", nome)
    file.close()

def atualizarMusica(idAt):
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    musica = []
    file.close()
    for linha in linhas:
        dados = linha.split(";")
        id = dados[0]
        if id == idAt:
            musica = dados
            break
    if len(musica) == 0:
        print("Não existe uma música com esse id.")
        return

    print("Digite novos campos (vazio se não quiser mudar) ")
    id = input("Id({}): ".format(musica[0]))
    if len(id) == 0:
        id = musica[0]
    nome = input("Nome({}): ".format(musica[1]))
    if len(nome) == 0:
        id = musica[1]

    compassos = musica[2].split("|")
    novoComp = []
    for compasso in compassos:
        if compasso == "\n":
            continue
        c = input("({}):".format(compasso))
        if len(c) == 0:
            novoComp.append(compasso)
        else:
            novoComp.append(c)
    print(id, nome, novoComp)
    file = open("data/musicas.txt", "w")
    for linha in linhas:
        dados = linha.split(";")
        if dados[0] != idAt:
            file.write(linha)
            continue
        file.write(id + ";" + nome + ";")
        for comp in novoComp:
            file.write(comp + ";")
        file.write("\n")
    file.close()
def visualizarMusica(idVis):
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    musica = []
    for linha in linhas:
        dados = linha.split(";")
        id = dados[0]
        if id == idVis:
            musica = dados
            break
    if len(musica) == 0:
        print("Não existe musica com esse id.")
        return
    print("Id: {}, Nome: {}".format(musica[0], musica[1]))
    compassos = musica[2]
    acordes = []
    compassos = compassos.split("|")
    for compasso in compassos:
        if compasso == "\n":
            continue
        print(compasso)
        acs = compasso.split(" ")
        acordes.append(acs)


    

        
def excluirMusica(idDel):
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    file.close()
    file = open("data/musicas.txt", "w")
    found = False
    for musica in linhas:
        dados = musica.split(";")
        id = dados[0]
        if id == idDel:
            found = True
        else:
            file.write(musica)
    if (not found):
        print("Não existe música com esse id.")
    file.close()
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
        file.write(compasso + "|")
    file.write("\n")        
    file.close()
def main():
    clear()
    print(logo())
    print(menu())
    op = "1"
    while True:
        op = input("Digite uma opção: ")
        if op == '1':
            listarMusicas()
        elif op == '2':
            idVis = input("Digite o id da música: ")
            visualizarMusica(idVis)
        elif op == '3':
            criarMusica()
        elif op == '4':
            idDel = input("Digite o id da música: ")
            excluirMusica(idDel)
        elif op == '5':
            idAt = input("Digite o id da música: ")
            atualizarMusica(idAt)
        elif op == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
