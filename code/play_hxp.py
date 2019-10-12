from dlgo import minimax
from dlgo import hxp

from six.moves import input


def print_board(board):
    print('    C1   C2   C3')
    for row in (1, 2, 3):
        pieces = []
        for col in (1, 2, 3):
            minion = board.get(hxp.Point(row, col))
            pieces.append(minion or '  ')
        print('R%d  %s' % (row, ' | '.join(pieces)))
    print()


def main():
    game = hxp.GameState.new_game()

    human_player = hxp.Player.x
    # bot_player = hxp.Player.o

    bot = minimax.MinimaxAgent()

    while not game.is_over():
        if game.next_player == human_player:
            print("===================")
            print_board(game.board)
            print("Human player's turn")
            print("===================")
            moves = game.legal_moves()
            print('\n'.join('{} {}'.format(idx, m) for idx, m in enumerate(moves)))
            human_select = int(input('-- ').strip())
            move = moves[human_select]
        else:
            print("===================")
            print_board(game.board)
            print("AI player's turn")
            print("===================")
            move = bot.select_move(game)
        game = game.apply_move(move)

    print_board(game.board)
    winner = game.winner()
    if winner is None:
        print("It's a draw.")
    else:
        print('Winner: ' + str(winner))


if __name__ == '__main__':
    main()
