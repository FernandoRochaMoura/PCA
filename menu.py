import jogo


def init_tela():
    print(f'''
     __   ___                       __   __  
    |__) |__   |\/|    \  / | |\ | |  \ /  \ 
    |__) |___  |  |     \/  | | \| |__/ \__/ 
                                         
''')
    opt = input('😀 Escreva "sim" se quiser iniciar o jogo:').lower()

    if opt == 'sim':
        jogo.init_game()
    else:
        print('Jogo encerrado')

