#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    This code defines a backtrack function to find
    solutions to a problem. It uses
    backtracking to explore all possibilities by recursively
    trying different options. It is written in Python
    """
    if r == n:
        res = []
        for j in range(len(board)):
            for k in range(len(board[j])):
                if board[j][k] == 1:
                    res.append([j, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_n = int(n[1])
        if n_n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n_n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
