class Board:
    def __init__(self, board):
        self.board = board

    def print(self):
        for index, cell in enumerate(self.board):
            if index % 9 == 0:
                print('\n', end='')

            print(cell, end=' ')
        print('\n')

    def _possible_numbers(self, index):
        x, y = (index // 9) * 9, index % 9
        numbers = set([n for n in self.board[y::9] if n != 0])
        numbers.update([n for n in self.board[x:x+9] if n != 0])

        for x0 in [(x // 27 * 3) * 9 + n for n in [0, 9, 18]]:
            y0 = x0 + y // 3 * 3
            numbers.update([n for n in self.board[y0:y0 + 3] if n != 0])

        return sorted(set(range(1, 10)) - numbers)

    def solve(self):
        blank = [i for (i, v) in enumerate(self.board) if v == 0]
        index = 0

        while index < len(blank):
            if index < 0:
                index = 0
            if index >= len(blank):
                break

            index2 = blank[index]
            possible_numbers = self._possible_numbers(index2)
            actual_num = self.board[index2]

            try:
                self.board[index2] = [x for x in possible_numbers
                                      if x > actual_num][0]
                index += 1
            except IndexError:
                index -= 1
                self.board[index2] = 0


with open('./example/example1.txt') as f:
    board = Board([int(n) for n in f.read() if n != '\n'])

board.print()
board.solve()
board.print()
