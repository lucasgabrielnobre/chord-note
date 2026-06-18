import os
from notasAcorde import notasAcorde, transporAcorde
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    file = open("assets/menu.txt")
    menu = file.read()
    file.close()
    return menu
def logo():
    file = open("assets/logo.txt")
    logo = file.read()
    file.close()
    return logo

def acharMusica(idAc):
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    musica = []
    file.close()
    for linha in linhas:
        dados = linha.split(";")
        id = dados[0]
        if id == idAc:
            musica = dados
            break
    return musica

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
    musica = acharMusica(idAt)
    if len(musica) == 0:
        print("Não existe musica com esse id.")
        return
    print("Digite novos campos (vazio se não quiser mudar) ")
    id = input("Id({}): ".format(musica[0]))
    if len(id) == 0:
        id = musica[0]
    nome = input("Nome({}): ".format(musica[1]))
    if len(nome) == 0:
        nome = musica[1]

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
    fileR = open("data/musicas.txt", "r")
    linhas = fileR.readlines()
    file = open("data/musicas.txt", "w")
    for linha in linhas:
        dados = linha.split(";")
        if dados[0] != idAt:
            file.write(linha)
            continue
        file.write(id + ";" + nome + ";")
        for comp in novoComp:
            file.write(comp + "|")
        file.write("\n")
    file.close()

def transporMusica(musica, id, nome, semitons):
    if len(musica) == 0:
        print("Não existe musica com esse id.")
        return
    compassos = musica[2].split("|")
    novoComp = ""
    for compasso in compassos:
        if compasso == "\n":
            continue
        acs = compasso.split()
        for i in range(len(acs)):
            novoComp += transporAcorde(acs[i], semitons) 
            if i < len(acs) - 1:
                novoComp += " "
        novoComp += "|"
    print(novoComp)
    criarMusica(id, nome, novoComp)


def visualizarMusica(idVis):
    musica = acharMusica(idVis)
    if len(musica) == 0:
        print("Não existe musica com esse id.")
        return
    print("Id: {}, Nome: {}".format(musica[0], musica[1]))

    opA = input("Mostrar as notas dos acordes?(1: sim): ")
    compassos = musica[2]
    acordes = []
    compassos = compassos.split("|")
    for compasso in compassos:
        if compasso == "\n":
            continue
        acs = compasso.split(" ")
        acordes.append(acs)

    for compasso in compassos:
        if compasso == "\n":
            continue
        print(compasso)
    if opA != '1':
        return
    for compasso in compassos:
        if compasso == "\n":
            continue
        acs = compasso.split(" ")
        for ac in acs:
            for nota in notasAcorde(ac):
                print(nota, end = " ")
            print("|", end = "")
        print()

        
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
def criarMusica(id, nome, compassos):
    file = open("data/musicas.txt", "a")
    file.write(id + ";" + nome + ";")
    file.write(compassos)
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
            id = input("Digite o id da musica: ")
            nome = input("Digite o nome da música: ")
            print("Digite os acordes, cada linha é um compasso (0 para terminar): ")
            compasso = ""
            compassos = "" 
            while True:
                compasso = input()
                if compasso == "0":
                    break
                compasso = compasso.strip()
                compassos += compasso + "|"
            criarMusica(id, nome, compassos)
        elif op == '4':
            idDel = input("Digite o id da música: ")
            excluirMusica(idDel)
        elif op == '5':
            idAt = input("Digite o id da música: ")
            atualizarMusica(idAt)
        elif op == '6':
            idTr = input("Digite o id da música: ")
            musica = acharMusica(idTr)
            if len(musica) == 0:
                print("Não existe musica com esse id.")
                continue
            idTr = input("Digite o novo id({}): ".format(musica[0]))
            nomeTr = input("Digite o novo nome({}): ".format(musica[1]))
            semitons = int(input("Semitons para subir(-11 a 11): "))
            transporMusica(musica, idTr, nomeTr, semitons)
        elif op == '7':
            clear()
            print(logo())
            print(menu())
        elif op == '0':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
