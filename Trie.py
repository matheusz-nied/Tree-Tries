class No:
    def __init__(self):
        self.finalPalavra = False
        self.filhos = []
        for i in range(0, 30):
	        self.filhos.append(None)

def mapeiaCharParaIndice(char):
    # ord() retorna o valor na tabela ASCI
    return (ord(char) - ord('a'))

def insert( raiz, chave):
    no = raiz
    for letra in chave:
        i = mapeiaCharParaIndice(letra)
        if(not no.filhos[i]):
            no.filhos[i] = No()
        no = no.filhos[i]
    no.finalPalavra = True
    return no

raiz = No()
raiz = insert(raiz,'preto')
print(raiz[0].filhos)

