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

def cumulative_sum(l: list[int]): # 累積和を求める
    ans = [l[0]]
    for i in range(1, len(l)):
        ans[i] = ans[i - 1] + l[i]
    return ans

def main():
    s = input()
    d = defaultdict(int)
    count = defaultdict(int)
    max_i = len(s)

    for t in s:
        d[t] += 1

    for i in range(max_i + 1):
        for v in d.values():
            if v == i:
                count[i] += 1

    flag = True
    for v in count.values():
        if v != 2 and v != 0:
            flag = False
            break

    o_judge(flag)

if __name__ == "__main__":  # メイン処理
    main()
