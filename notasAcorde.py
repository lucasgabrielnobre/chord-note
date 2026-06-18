from notaValor import *
maior     = [0, 0, 2, 4, 5, 7, 9, 11] # b5 maior[5] - 1
mixolidio = [0, 0, 2, 4, 5, 7, 9, 10] 
menor     = [0, 0, 2, 3, 5, 7, 8, 10]
diminuta  = [0, 0, 1, 3, 5, 6, 8, 10] # Lócrio (contém 1, b3, b5)
aumentada = [0, 0, 2, 4, 6, 8, 9, 11] # Lídio Aumentado (contém 1, 3, #5)

def jump(t, x):
    return (t + x) % 12

def lerAcorde(s):
    acorde = {'tonica' : 0, 'qualidade' : "mixolidio", 'extensoes': [], 'triade' : [], 'baixo' : 0 }
    #tonica
    if  len(s) >= 2 and (s[1] == 'b' or s[1] == '#'):
        acorde['tonica'] = notaValor[s[0] + s[1]]
    else:
        acorde['tonica'] = notaValor[s[0]]
    t = acorde['tonica']
    acorde['baixo'] = t
    #extensoes
    add = '' 
    for i in range(len(s)):
        c = s[i]
        if c == 'b' or c == '#':
            add = c
        if c.isdigit():
            if c != '1' or (add and add[-1] == '1'):
                c = add + c
                acorde['extensoes'].append(c)
                add = ''
            else:
                add += c
            

    #qualidade
    if "m" in s:
        acorde['qualidade'] = "menor"
    if "maj" in s or "M" in s: # se for maj vai sobrepor, se não fica menor
        acorde['qualidade'] = "maior"
    if "aug" in s:
        acorde['qualidade'] = "aumentada"
    if "dim" in s: #idem
        acorde['qualidade'] = "diminuta"
    if "sus2" in s: 
        acorde['qualidade'] = "sus2"
    if "sus4" in s: 
        acorde['qualidade'] = "sus4"
    # baixo
    if '/' in s[-3:-1]:
        if s[-1] == 'b' or s[-1] == '#':
            acorde['baixo'] = s[-2] + s[-1]
        else:
            acorde['baixo'] = s[-1]
    else:
        acorde['baixo'] = t
    # colocando a triade
    if acorde['qualidade'] == "maior" or acorde['qualidade'] == "mixolidio":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, maior[3])][0], valorNota[jump(t, maior[5])][0]]
    elif acorde['qualidade'] == "menor":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, menor[3])][-1], valorNota[jump(t, menor[5])][0]]
    elif acorde['qualidade'] == "aumentada":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, aumentada[3])][0], valorNota[jump(t, aumentada[5])][0]]
    elif acorde['qualidade'] == "diminuta":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, diminuta[3])][-1], valorNota[jump(t, diminuta[5])][-1]]
    elif acorde['qualidade'] == "sus2":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, maior[2])][0], valorNota[jump(t, maior[5])][0]]
    elif acorde['qualidade'] == "sus4":
        acorde['triade'] = [valorNota[t][0], valorNota[jump(t, maior[4])][0], valorNota[jump(t, maior[5])][0]]
    return acorde

# if semitons < 0: #diminuir por 1 é a mesma coisa que aumentar por 11, por 2, 10
# semitons = 12 + semitons

def transporAcorde(acorde, semitons):
    if len(acorde) == 1:
        return valorNota[jump(notaValor[acorde], semitons)][-1]
    elif acorde[1] == "#" or acorde[1] == "b":
        tonica = acorde[0] + acorde[1]
        tonica = valorNota[jump(notaValor[tonica], semitons)][-1]
        extensoes = acorde[1:-1]
        return tonica + extensoes
    else:
        tonica = valorNota[jump(notaValor[acorde[0]], semitons)][-1]
        extensoes = acorde[1:]
        return tonica + extensoes
def notasAcorde(s):
    # notas + notaValor
    acorde = lerAcorde(s)
    notas = []
    t = acorde['tonica']
    q = acorde['qualidade']
    if (t != acorde['baixo']): 
        notas.append(acorde['baixo'])
    if len(acorde['extensoes']) > 0: # se tem extensao tem a setima C9 => C E G Bb D
        if '6' in acorde['extensoes']:  
            notas.append(valorNota[jump(t, maior[6])][-1])
        elif q == "maior":
            notas.append(valorNota[jump(t, maior[7])][0])
        else:
            notas.append(valorNota[jump(t, menor[7])][-1])
    for ext in acorde['extensoes']:
        # 4 casos: 5, b5, 13, b13
        grau = 0
        acidente = ''
        if (len(ext) == 1):
            grau = int(ext)
        elif (len(ext) == 2):
            if ext[0].isnumeric():
                grau = int(ext)
            else:
                grau = int(ext[1])
                acidente = ext[0]
        else:
            acidente = ext[0]
            grau =  int(ext[1:3])


        if grau == 5:
            n = acorde['triade'][2] # pega a quinta
            n = notaValor[n]
            if acidente == "b":
                n -= 1
            elif acidente == "#":
                n += 1
            acorde['triade'][2] = valorNota[n][-1] if acidente == "b" else valorNota[n][0]
            continue
        if grau >= 8: # ajeitar b5 mudar a triade
            grau -= 7
        if grau == 7 or grau == 6:
            continue
        valor = 0

        if q == "maior":
            valor = maior[grau]
        elif q == "mixolidio":
            valor = mixolidio[grau]
        elif q == "menor":
            valor = menor[grau]
        elif q == "aumentada":
            valor = aumentada[grau]
        elif q == "diminuta":
            valor = diminuta[grau]

        if acidente == "b":
            valor -= 1
        elif acidente == "#":
            valor += 1
        #nota = valorNota[jump(t, valor)][1]+"/"+valorNota[jump(t,valor)][0] if len(valorNota[jump(t, valor)]) > 1 else valorNota[jump(t,valor)][-1] 
        #nota = valorNota[ jump(t, valor) ][-1] if acidente == "b" else valorNota[ jump(t, valor) ][0] 
        if acidente == "b":
            nota = valorNota[ jump(t, valor) ][-1]

        elif len(acorde['triade'][0]) > 1 and acorde['triade'][0][-1] == "b": # Db
            nota = valorNota[ jump(t, valor) ][-1]

        else:
            nota = valorNota[ jump(t, valor) ][0]

        if grau == 6:
            notas.pop()
        notas.append(nota)
    notas = acorde['triade'] + notas
    return notas

def main():
    pass

if __name__ == "__main__":
    main()
