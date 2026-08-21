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
    s, a, b, x = i_multi()
    next_run = True
    ans = 0
    while x > 0:
        if next_run:
            ans += s * a
            x -= a
            next_run = False
        else:
            x -= b
            next_run = True

    if x < 0 and not(next_run):
        ans += x * s

    print(ans)

if __name__ == "__main__":  # メイン処理
    main()
