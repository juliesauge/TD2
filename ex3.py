# Exercice 3 

def score(mot):
    a = 0
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
    return a

def scoremax(liste):
    max = score(liste[0])
    motmax = liste[0]
    for mot in liste:
        if score(mot) > max:
            max = score(mot)
            motmax = mot
    return motmax,max

def meilleur(tirage,lexique):
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
        
print(meilleur(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],['bonjour','sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']))

