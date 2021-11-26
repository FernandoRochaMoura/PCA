import const


def init_game():
    resources = const.RESOURCES

    pts = 0
    choice = None

    for q in resources:
        q.print_questao()
        q.print_alternativas()

        choice = int(input("\n>> "))

        if (choice - 1) == q.resposta:
            pts += 1
            print('Parabéns! Você acertou! 🥳🍾\n')
        else:
            print(f'Que pena, você errou! 😞\n')

    print(f'''PONTOS: {pts}''')
