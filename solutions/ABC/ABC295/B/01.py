# from collections import Counter
import bisect
import fractions
import heapq
import itertools
import math
import pprint
import re
import sys
from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations, product

# import numpy as np
from operator import itemgetter
from socket import AddressInfo

# from itertools import permutations # 順列を列挙する
from typing import Counter


def i_single(input_type: type):  # 単一入力
    return input_type(input())


def i_multi(input_type: type = int, sep=" "):  # 複数入力
    return map(input_type, input().split(sep))


def i_list(input_type: type = int, sep=" "):  # リスト入力
    return list(map(input_type, input().split(sep)))


def o_judge(judge: bool):  # 判定出力
    print("Yes" if judge else "No")

def main():
    r, c = i_multi(int)
    board = []
    for _ in range(r):
        board.append(list(input()))

    wall = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == '#':
                wall.append([i, j])

    for i in range(r):
        for j in range(c):
            if board[i][j] != '.' and board[i][j] != '#':
                b = int(board[i][j])
                board[i][j] = '.'
                for w in wall:
                    d = abs(w[0] - i) + abs(w[1] - j)
                    if d <= b:
                        board[w[0]][w[1]] = '.'

    for row in board:
        print(*row, sep='')
            

if __name__ == "__main__":  # メイン処理
    main()
