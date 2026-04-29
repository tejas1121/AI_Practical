class NQueens:
    def __init__(self, n):
        self.N = n
        
        # arrays
        self.queens = [0] * n
        self.column = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)

    def solve(self):
        self.place_queen(0)

    def place_queen(self, row):
        if row == self.N:
            self.print_solution()
            return

        for col in range(self.N):
            if (self.column[col] == False and 
                self.diag1[row - col + self.N - 1] == False and 
                self.diag2[row + col] == False):

                # place queen
                self.queens[row] = col
                self.column[col] = True
                self.diag1[row - col + self.N - 1] = True
                self.diag2[row + col] = True

                self.place_queen(row + 1)

                # backtrack
                self.column[col] = False
                self.diag1[row - col + self.N - 1] = False
                self.diag2[row + col] = False

    def print_solution(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.queens[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()


# -------- MAIN --------
n = 4
q = NQueens(n)
q.solve()