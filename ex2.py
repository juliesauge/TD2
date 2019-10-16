# Exercice 1 et 2

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
            M.append([len(mot),mot])
        a = M[0][0]
        b = M[0][1]
        for k in range(len(M)):
            if M[k][0] > a:
                a = M[k][0]
                b = M[k][1] 
        return b

print(solve(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],['bonjour','sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']))

