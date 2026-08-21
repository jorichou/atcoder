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


def i_single(input_type: type = int):  # 単一入力
    return input_type(input())


def i_multi(input_type: type = int, sep=" "):  # 複数入力
    return map(input_type, input().split(sep))


def i_list(input_type: type = int, sep=" "):  # リスト入力
    return list(map(input_type, input().split(sep)))


def o_judge(judge: bool):  # 判定出力
    print("Yes" if judge else "No")

def main():
    h, w = i_multi()
    r, c = i_multi()
    edge = [(1, 1), (1, w), (h, 1), (h, w)]

    if h == 1 and w == 1:
        print(0)
    elif w == 1 or h == 1:
        if (r, c) in edge:
            print(1)
        else:
            print(2)
    else:
        if 1 < r < h and 1 < c < w:
            print(4)
        elif (r, c) in edge:
            print(2)
        else:
            print(3)

if __name__ == "__main__":  # メイン処理
    main()
