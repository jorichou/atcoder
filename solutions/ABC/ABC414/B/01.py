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
    n = i_single()
    length = 0
    s = ""
    ok = True
    for _ in range(n):
        c, l = i_multi(str)
        length += int(l)
        if length > 100:
            ok = False
            break

        else:
            s += c * int(l)

    if ok:
        print(s)
    else:
        print("Too Long")
    
if __name__ == "__main__":  # メイン処理
    main()
