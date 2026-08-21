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
    n, m = i_multi()
    h = i_list()
    count = 0
    for i in range(n):
        m -= h[i]
        if m < 0:
            break
        else:
            count += 1

    print(count)

if __name__ == "__main__":  # メイン処理
    main()
