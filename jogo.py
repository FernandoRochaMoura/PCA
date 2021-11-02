import const


def init_game():
    resources = const.RESOURCES

    pts = 0
    choice = None

    for q in resources:
        q.print_questao()
        q.print_alternativas()

        choice = int(input())

        if (choice - 1) == q.resposta:
            pts += 1

    print(f'''PONTOS: {pts}''')
