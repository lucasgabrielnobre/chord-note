from notaValor import *
#dado um s retornar os valores 
maior = [0, 0, 2, 4, 5, 7, 9, 11] # b5 maior[5] - 1
menor = [0, 0, 2, 3, 5, 7, 8, 10]
diminuta  = [0, 0, 1, 3, 5, 6, 8, 10] # Lócrio (contém 1, b3, b5)
aumentada = [0, 0, 2, 4, 6, 8, 9, 11] # Lídio Aumentado (contém 1, 3, #5)

def add(t, n):
    return (t + n) % 12

def lerAcorde(s):
    # aug, +     => 0, 4, 8        -> 1 3 5#
    # dim, -     => 0, 3, 6, (10)  -> 1 3b 5b
    # sus2       => 0, 2, 7        -> 1 2 5
    # sus4       => 0, 2, 5        -> 1 4 5
    acorde = {'tonica' : 0, 'qualidade' : "maior", 'extensoes': [], 'triade' : [], 'baixo' : 0 }
    #tonica
    if  len(s) >= 2 and (s[1] == 'b' or s[1] == '#'):
        acorde['tonica'] = notaValor[s[0] + s[1]]
    else:
        acorde['tonica'] = notaValor[s[0]]
    t = acorde['tonica']

    #extensoes
    s_ext = []
    doubleDigit = False
    for i in range(len(s)): 
        if s[i].isdigit():
            if doubleDigit:
                s_ext[i - 1] += s[i]
                doubleDigit = False
            if s[i] == '1':
                doubleDigit = True
    print(s_ext)

    #qualidade
    if "m" in s and not ("maj" in s):
        acorde['qualidade'] = "menor"
    if "aug" in s:
        acorde['qualidade'] = "aumentada"
    if "dim" in s: 
        acorde['qualidade'] = "diminuta"
    if "sus2" in s: 
        acorde['qualidade'] = "sus2"
    if "sus4" in s: 
        acorde['qualidade'] = "sus4"
    # baixo
    if '/' in s[-3:-1]:
        if s[-1] == 'b' or s[-1] == '#':
            acorde['baixo'] = notaValor[s[-2] + s[-1]]
        else:
            acorde['baixo'] = notaValor[s[-1]]
    else:
        acorde['baixo'] = t
    # colocando a triade
    if acorde['qualidade'] == "maior":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, maior[3])][0], valorNota[add(t, maior[5])][0]]
    elif acorde['qualidade'] == "menor":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, menor[3])][-1], valorNota[add(t, menor[5])][0]]
        acorde['triade'] = [t, add(t, menor[3]), add(t, menor[5])]
    elif acorde['qualidade'] == "aumentada":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, aumentada[3])][0], valorNota[add(t, aumentada[5])][0]]
    elif acorde['qualidade'] == "diminuta":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, diminuta[3])][-1], valorNota[add(t, diminuta[5])][-1]]
    elif acorde['qualidade'] == "sus2":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, maior[2])][0], valorNota[add(t, maior[5])][0]]
    elif acorde['qualidade'] == "sus4":
        acorde['triade'] = [valorNota[t][0], valorNota[add(t, maior[4])][0], valorNota[add(t, maior[5])][0]]

    
    return acorde

def notasAcorde(s):
    # notas + notaValor
    acorde = lerAcorde(s)
    notas = acorde['triade']
    return notas

def main():
    print(notasAcorde(input()))

if __name__ == "__main__":
    main()
