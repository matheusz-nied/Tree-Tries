searchPrefix(prefix) {
  // Define a raiz da árvore como o inicio da busca
  let currentNode = this.root;

  // Itera por cada caractere do prefixo de busca
  for (let i = 0; i < prefix.length; i++) {
    // Se o caractere atual não existir no ramo atual da árvore, retorna uma lista vazia
    if (currentNode.children.get(prefix[i]) === undefined) {
      return [];
    }

    // Define o próximo ramo de busca
    currentNode = currentNode.children.get(prefix[i]);
  }

  // Se todos os caracteres do prefixo foram iterados, significa que o prefixo existe na Trie
  // Esse método realiza uma busca em profundidade (DFS) no restante da árvore para apresentar como auto-complete 
  return this.wordsToAutocomplete(prefix, currentNode);
}

// Método que utiliza busca em profundidade (DFS) a partir de um nó e exibe todas as palavras a partir desse nó 
// Solução ideal para retornarmos palavras que podem completar um prefixo
wordsToAutocomplete(prefix, node) {
  // Aqui utilizamos uma pilha para fazer a busca em profundidade (a última letra adicionada vai ser a próxima letra consumida)
  const stack = [];

  // Guardamos uma lista com todas as palavras completas, esse será o nosso retorno
  const matches = [];

  // Se a letra atual for o final de alguma palavra na Trie, devemos adicionar à nossa variável de retorno também
  if (node.endOfWord) {
    matches.push(prefix);
  }

  // Começamos adicionando na nossa pilha todas as letras que o nó atual faz apontamento
  for (let [key, child] of node.children) {
    stack.push([key, child, []]);
  }

  // Enquanto tiver letras nessa pilha, vamos consumir elas
  while (stack.length > 0) {
    // Cada elemento da pilha terá 3 variáveis de controle
    // Sempre mantemos a letra atual, o nó atual
    // E uma referência para um stringBuilder, pois conforme passamos pela pilha vamos construindo uma palavra com as letras encontradas
    let [char, node, currentWord] = stack.pop();

    // E sempre vamos adicionando a letra atual ao stringBuilder
    currentWord.push(char);

    // Se a letra atual for o final de alguma palavra, podemos completar o stringBuilder
    // E adicionar a palavra completa à nossa variável de retorno
    if (node.endOfWord) {
      matches.push(currentWord.join(""));
    }

    // E adicionamos todas as letras que o nó atual faz apontamento
    // Para que a pilha continue consumindo o restante das letras
    for (let [key, child] of node.children) {
      stack.push([key, child, [...currentWord]]);
    }
  }

  // Por fim, retornamos todas as palavras encontradas a partir do nó recebido
  return matches;
}