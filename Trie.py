MAX_SYMBOLS = 30


class No:
    def __init__(self):
        self.finalPalavra = False
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
    no.finalPalavra = True


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
    return no.finalPalavra


def listarTrie(raiz):
    palavra = [None] * MAX_SYMBOLS
    listar(raiz, palavra, 0)


def listar(raiz, palavra, nivel):
    for j in range(nivel, MAX_SYMBOLS):
        palavra[j] = "\0"
    if (raiz.finalPalavra != False):
        print()

        for letra in palavra:

            if(letra != None):

                print(f"{letra}", end="")

    for i in range(0, MAX_SYMBOLS):

        #i = mapeiaCharParaIndice(palavra[i])
        if(raiz.filhos[i]):
            palavra[nivel] = chr(i + ord('a'))
            listar(raiz.filhos[i], palavra, nivel + 1)


def alturaTrie(raiz):
    palavra = [None] * MAX_SYMBOLS
    global altura

    def calculaAltura(raiz, palavra, nivel):
        global altura
        if(nivel > altura):
            altura = nivel
            
        for i in range(0, MAX_SYMBOLS):
            if(raiz.filhos[i]):
                palavra[nivel] = chr(i + ord('a'))

                calculaAltura(raiz.filhos[i], palavra, nivel + 1)


    calculaAltura(raiz, palavra, 0)


def autocomplete(raiz,prefix):
    no = raiz
    for letra in prefix:
        i = mapeiaCharParaIndice(letra)
        if(no.filhos[i] is None):
            print(f"NÃO foi encontrada o prefixo {prefix}.")
            return False
        no = no.filhos[i]

    return palavrasParaCompletar(prefix, no)

def palavrasParaCompletar(prefix, no):

    pilha = []

    matches = []

    if (no.finalPalavra):
        matches.append(prefix)
    
    for()

# -------------MAIN------------

# Quebra de linha para melhorar estética
print()

# Inserindo
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

# Buscas
print("\n\nBuscas:")

buscar(raiz, "azul")
buscar(raiz, "verde")
buscar(raiz, "preto")
buscar(raiz, "amarelo")

# Quebra de linha para melhorar estética
print()

# Calculando altura

#Altura é utilizada como variável global dentro da função
altura = 0
alturaTrie(raiz)
print(f"Altura da árvore Trie é: {altura}")
# Quebra de linha para melhorar estética
print()
autocomplete(raiz, "pr")

