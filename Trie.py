# Rodar o arquivo Trie.py em python 3
# Caso não consiga executar o código,
# eu o deixei no seguinte site que é um interpretador online.
# Basta acessar o link
# https://onlinegdb.com/-3nB77Y21


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


def autocomplete(raiz, prefix):
    no = raiz
    for letra in prefix:
        i = mapeiaCharParaIndice(letra)
        if(no.filhos[i] is None):
            print(f"NÃO foi encontrada o prefixo {prefix}.")
            return False
        no = no.filhos[i]

    palavra = [None] * MAX_SYMBOLS
    listarPrefix(no, prefix, palavra, 0)

    # return palavrasParaCompletar(prefix, no)


def listarPrefix(raiz, prefix, palavra, nivel):
    for j in range(nivel, MAX_SYMBOLS):
        palavra[j] = "\0"
    if (raiz.finalPalavra != False):
        print()
        print(f"{prefix}", end="")
        for letra in palavra:

            if(letra != None):

                print(f"{letra}", end="")

    for i in range(0, MAX_SYMBOLS):

        #i = mapeiaCharParaIndice(palavra[i])
        if(raiz.filhos[i]):
            palavra[nivel] = chr(i + ord('a'))
            listarPrefix(raiz.filhos[i], prefix, palavra, nivel + 1)
# -------------MAIN------------


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


# Altura é utilizada como variável global dentro da função
altura = 0
alturaTrie(raiz)
print(f"\nAltura da árvore Trie é: {altura} \n")


prefix = input("Entre com o prefixo que deseja autocompletar: ")

autocomplete(raiz, prefix)

# Quebra de linha para melhorar estética
print()
