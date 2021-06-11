import random
from typing import Tuple
from copy import deepcopy, error
import json

import numpy as np
from dokusan import generators

solution = []


def solve(board: list[int]) -> bool:
    spaceAt = spaces(board)
    if not spaceAt:
        return True
    else:
        (x, y) = spaceAt
    for i in range(1, 10):
        if valid(board, i, spaceAt):
            board[x][y] = i
            if(solve(board)):
                return True
            board[x][y] = 0
    return False


def printBoard(board: list[int]) -> None:
    for i in range(len(board)):
        if i % 3 == 0:
            print("--------------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ", end="")
            if j == 8:
                print(str(board[i][j])+" |")
            else:
                print(str(board[i][j])+" ", end=" ")


def spaces(board: list[int]):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x, y)
    return None


def valid(board: list[int], num: int, pos: Tuple) -> bool:
    # check row
    (x, y) = pos
    for i in range(len(board[x])):
        if num == board[x][i] and not i == y:
            return False

    # check coloumn
    for j in range(len(board)):
        if num == board[j][y] and not j == x:
            return False

    # check box
    x //= 3
    y //= 3

    for k in range(x*3, x*3+3):
        for l in range(y*3, y*3+3):
            if num == board[k][l] and not (k, l) == pos:
                return False

    return True


def generateBoard(upto: int = 21) -> list[int]:
    randomBoard = np.array(
        list(str(generators.random_sudoku(avg_rank=150)))).reshape(9, 9)
    randomBoard = randomBoard.astype(np.int)
    # if not randomBoard in json.load(open('puzzles.json')):
    #     # converting dictionary to json object
    #     json_object = json.dumps(randomBoard, indent=4)
    #     # Writing to FileTypes.json
    #     with open("puzzles.json", "w") as outfile:
    #         outfile.write("puzzles.json")
    return randomBoard
    print("here")


def TestBoard(sudokouBoard: list[int]) -> bool:
    solve(sudokouBoard)
    s = 0
    for i in sudokouBoard:
        s += sum(i)
    if s == 405:
        print("board generated")
        return True
    else:
        return False
        print("error! in board something went wrong")


def solveBoard(board: list[int]) -> list[int]:
    solution = board
    solve(solution)
    return(solution)


print(generateBoard())
