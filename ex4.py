# Exercice 4

f = open("frenchssaccent.dic", "r")
lexique = f.read()
lexique=lexique.split("\n")


def score(mot):
    a = 0
    b = 0
    for lettre in mot:
        if lettre in ['a','e','i','l','n','o','r','s','t','u']:
            a = a + 1
        elif lettre in ['d','g','m']:
            a = a + 2
        elif lettre in ['b','c','p']:
            a = a + 3
        elif lettre in ['f','h','v']:
            a = a + 4
        elif lettre in ['j','q']:
            a = a + 8
        elif lettre in ['k','w','x','y','z']:
            a = a + 10
        elif lettre == '?':
            b = b + 1
        elif b > 1:
            return None
    return a

def scoremax(liste):
    max = score(liste[0])
    motmax = liste[0]
    for mot in liste:
        if score(mot) > max:
            max = score(mot)
            motmax = mot
    return motmax,max
    
    
    
def solve(tirage,lexique):
    L = []
    T = []
    M = []
    for mot in lexique:
        for lettre in mot:
            for caractere in tirage:
                if caractere not in mot:
                    T.append(mot)
            for mot in lexique:
                if mot not in T:
                    L.append(mot)
        for mot in L:
            M.append(mot)
        return scoremax(M)
        
print(solve('zxcrrtv?',lexique))

#le programme ne renvoit pas la bonne réponse, je n'arrive pas à l'améliorer