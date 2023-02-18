MAX_SYMBOLS = 30


class No:
    def __init__(self):
        self.filhos = [None] * MAX_SYMBOLS


def mapeiaCharParaIndice(char):
    # ord() retorna o valor na tabela ASCI
    return (ord(char) - ord('a'))


def insert(raiz, chave):
    no = raiz
    for letra in chave:
        i = mapeiaCharParaIndice(letra)
        if(no.filhos[i] is None):
            no.filhos[i] = No()
        no = no.filhos[i]
    


def buscar(raiz, chave):
    print("Procurando:", chave, end=" - ")
    no = raiz
    for letra in chave:
        i = mapeiaCharParaIndice(letra)
        if(no.filhos[i] is None):
            print(f"NÃO foi encontrada a chave {chave}.")
            return False
        no = no.filhos[i]
    print(f"Foi encontrada a chave {chave}.")
    return True


def listarTrie(raiz):
    palavra = [None] * MAX_SYMBOLS
    listar(raiz, palavra, 0)


def listar(raiz, palavra, nivel):
    
    if (raiz.finalPalavra != False):
        print()
        palavra[nivel] = "\0"

        for letra in palavra:
            if(letra != None):
                if(letra == "\x00"):
                    return

                print(f"{letra}", end="")


    for i in range(0, MAX_SYMBOLS):
           
        #i = mapeiaCharParaIndice(palavra[i])
        if(raiz.filhos[i]):
            palavra[nivel] = chr(i + ord('a'))
            listar(raiz.filhos[i], palavra, nivel + 1)
    
#-------------MAIN------------

# Quebra de linha para melhorar estética
print()

#Inserindo
raiz = No()
insert(raiz, 'vermelho')
insert(raiz, 'azul')
insert(raiz, 'purpura')
insert(raiz, 'branco')
insert(raiz, 'violeta')
insert(raiz, 'prata')
insert(raiz, 'preto')
insert(raiz, 'rosa')
insert(raiz, 'rosachoque')

# Listando
print("Listando Árvore Trie:", end="")
listarTrie(raiz)

print()