class gameOfLife:
    """
    Do not return anything, modify board in-place instead.
    """
    def __init__(self, board: list[list[int]]):
        self._board = board
        # print("board: {}".format(self._board))

    def nearest_neighbors(self, i, j, distance=1):
        return [row[max(0, j-distance): j+distance+1] for row in self._board[max(0, i-distance): i+distance+1]]

    def next_state(self, i, j):
        neighbors = self.nearest_neighbors(i, j)
        # print("cell: {}".format(self._board[i][j]))
        # print("neighbors: {}".format(neighbors))
        count_live_neighbors = sum(col for row in neighbors for col in row) - self._board[i][j]
        # print("count_live_neighbors: {}".format(count_live_neighbors))
        if self._board[i][j] and (count_live_neighbors < 2 or count_live_neighbors > 3):
            return 0
        elif not self._board[i][j] and count_live_neighbors == 3:
            return 1
        else:
            return self._board[i][j]
    
    def next_board_state(self):
        new_board = []
        for i, row in enumerate(self._board):
            new_board.append([])
            for j, col in enumerate(self._board[i]):
                new_board[i].append(self.next_state(i, j))
        
        # print("new board: {}".format(new_board))
        self._board = new_board
        # print("new board: {}".format(self._board))
    
def test_gameOfLife():
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    g = gameOfLife(board)
    g.next_board_state()
    assert g._board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    board = [[1,1],[1,0]]
    g = gameOfLife(board)
    g.next_board_state()
    assert g._board == [[1,1],[1,1]]

if __name__ == "__main__":
    test_gameOfLife()