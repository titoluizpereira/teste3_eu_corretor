def ladderLengthSimple(inicial, final, listaPalavras):

    # Converte a lista para um conjunto para tornar a busca mais rápida
    listaPalavras = set(listaPalavras)

    # A rota guarda tuplas com (palavra atual, número de passos até aqui)
    rota = [(inicial, 1)]

    while rota:
        nova_rota = []

        for palavra, prox_passo in rota:
            # Se encontramos a palavra final, retornamos o número de passos
            if palavra == final:
                return prox_passo

            # Para cada posição da palavra tenta substituir por cada letra do alfabeto
            for i in range(len(palavra)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nova_palavra = palavra[:i] + c + palavra[i+1:]

                    # Se a nova palavra for válida (estiver na lista) adiciona essa nova palavra na próxima rota, com +1 passo e remove do conjunto para não visitar novamente
                    if nova_palavra in listaPalavras:
                        nova_rota.append((nova_palavra, prox_passo + 1))
                        listaPalavras.remove(nova_palavra)

        # Atualiza a rota com os próximos caminhos possíveis
        rota = nova_rota

    # Se não encontrou a palavra final, retorna 0
    return 0

print(ladderLengthSimple("casa", "rato", ["casa", "cava", "cata", "rata", "rato"]))
# Saída: 4 ("casa" -> "cata" -> "rata" -> "rato")

print(ladderLengthSimple("sol", "mar", ["sol", "sal", "mel", "mil"]))
# Saída: 0 (não há caminho possível até "mar")