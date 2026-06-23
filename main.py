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
def buscarMusica(nomeBusca):
    file = open("data/musicas.txt", "r")
    linhas = file.readlines()
    file.close()
    musicas = []
    for linha in linhas:
        dados = linha.split(";")
        nome = dados[1].lower()
        if nome.find(nomeBusca) != -1:
            musicas.append(dados)
    return musicas

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
            c = " ".join(c.split())
            novoComp.append(c)
    fileR = open("data/musicas.txt", "r")
    linhas = fileR.readlines()
    fileR.close()
    file = open("data/musicas.txt", "w")
    for linha in linhas:
        dados = linha.split(";")
        if dados[0] != idAt:
            file.write(linha)
            continue
        file.write(str(idAt) + ";" + nome + ";")
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
        try:
            for ac in acs:
                    for nota in notasAcorde(ac):
                        print(nota, end = " ")
                    print("|", end = "")
        except KeyError:
            print("Acordes não escritos na formatação correta.\nExemplos de acordes: Cmaj7, Dbm7, D#m7b5(9), etc.")
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
    file.write(str(id) + ";" + nome + ";")
    file.write(compassos)
    file.write("\n")        
    file.close()
def main():
    clear()
    print(logo())
    print(menu())
    file = open("data/id.txt")
    id = int(file.read())
    file.close()
    op = "1"
    while True:
        op = input("Digite uma opção: ")
        if op == '1':
            listarMusicas()
        elif op == '2':
            opBusca = input("Procurar por nome(1: sim)? ")
            idVis = "0"
            if opBusca.strip()  == "1": # se quer buscar por nome
                nomeBusca = input("Digite o nome: ").lower()
                nomeBusca = " ".join(nomeBusca.split())
                musicas = buscarMusica(nomeBusca)
                if len(musicas) == 0: # se não achou musica com tal nome
                    print("Não existe musica com esse nome.")
                    continue
                elif len(musicas) == 1: # se existir apenas uma musica não precisa buscar por id
                    idVis = musicas[0][0]
                else: # mostra todas as opcoes
                    for musica in musicas:
                        print(musica[0], "-", musica[1])
                    idVis = input("Digite o id da música: ")
            else:
                idVis = input("Digite o id da música: ")
            visualizarMusica(idVis)
        elif op == '3':
            nome = input("Digite o nome da música: ")
            print("Digite os acordes(0 para terminar): ")
            compasso = ""
            compassos = "" 
            while True:
                compasso = input()
                if compasso == "0":
                    break
                compasso = " ".join(compasso.split())
                compassos += compasso + "|"

            criarMusica(id, nome, compassos)
            id += 1
            file = open("data/id.txt", "w")
            file.write(str(id))
            file.close()
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
            nomeTr = input("Digite o novo nome({}): ".format(musica[1]))
            semitons = int(input("Semitons de mudança(-11 a 11): "))
            transporMusica(musica, id, nomeTr, semitons)
            id += 1
            file = open("data/id.txt", "w")
            file.write(str(id))
            file.close()
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
