import jogo


def init_tela():
    print('Bem Vindo 😀')
    opt = input('Escreva "sim" se quiser iniciar o jogo:').lower()

    if opt == 'sim':
        jogo.init_game()
    else:
        print('Jogo encerrado')

