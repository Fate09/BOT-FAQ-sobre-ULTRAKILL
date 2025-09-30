# Mini Bot de Perguntas sobre a arma Revolver em ULTRAKILL

print("🤖: Olá! Eu sou o Terminal, seu assistente sobre a seção 'ARMAS // Revolver' do jogo ULTRAKILL, oque busca?")
print("Digite 'sair' para encerrar a conversa.\n")

while True:
    pergunta = input("Você: ").strip().lower()

    if pergunta == "sair":
        print("Terminal: Até mais!👋")
        break

    # Respostas pré-definidas
    elif "revolver(piercer)" in pergunta or "piercer" in pergunta or "revolver inicial" in pergunta or "arma inicial" in pergunta:
        print("🤖: O Revólver Perfurador é a primeira arma encontrada em ULTRAKILL e é a variante azul do Revólver, obtida em [ 0-1: INTO THE FIRE ]. Ele pode \ncausar quantidades moderadas de dano com seu disparo primário e perfurar vários alvos fracos ou infligir dano concentrado em alvos únicos com seu disparo secundário segurando o botão direito do mouse.")

    elif "revolver(marksman)" in pergunta or "marksman" in pergunta or "segunda variante do revolver" in pergunta:
        print("🤖: O Revólver Marksman é a variante verde do Revólver e dá ao V1 a habilidade de lançar moedas para o ar apertando o botão direito. Ele pode ser comprado no Terminal por 7.500P após obter o Revólver Piercer em [ 0-1: INTO THE FIRE ].")

    elif "revolver(sharpshooter)" in pergunta or "sharpshooter" in pergunta or "terceira variante do revolver" in pergunta:
        print("🤖: O Revólver Atirador de Elite é a variante vermelha do Revólver, que pode ser comprado no Terminal por 25.000P após obter o Revólver Perfurador em [ 0-1: NO FOGO ]. Seu disparo alternativo dispara raios de energia vermelha que podem ricochetear em superfícies, perfurar inimigos e destruir projéteis. O número de ricochetes aumenta com a velocidade com que o revólver é girado.")

    elif "revolver(alternativo)" in pergunta or "revolver alternativo" in pergunta or "versão alternativa do revolver" in pergunta:
        print("🤖: O Revólver Alternativo (também conhecido como Revólver de Placa ou Canhão de Mão) é a versão alternativa do Revólver. Ele pode ser desbloqueado em [ 1-4: CLAIR DE LUNE ] após interagir com todas as quatro placas secretas encontradas no Limbo. É a primeira arma alternativa que os jogadores podem encontrar no jogo e altera as variantes compraveis no terminal por versões mais fortes das mesmas.")


    else:
        print("🤖: não possuo uma informação coerente com seu requisito, tente \n revolver(piercer) \n revolver(marksman) \n revolver(sharpshooter) \n revolver alternativo.") 
