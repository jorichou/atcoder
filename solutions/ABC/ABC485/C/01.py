# from collections import Counter
from ast import Tuple
import bisect
from cmath import sin
import fractions
import heapq
import itertools
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import pprint
import queue
from random import sample, seed
import re
import sys
from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations, product

# import numpy as np
from operator import itemgetter
from socket import AddressInfo

# from itertools import permutations # 順列を列挙する
from typing import Callable, Counter


# main ============================================================

def main():
    n = i_single()
    c = i_list()
    ans = []
    color_dic = defaultdict(list)
    c1 = c[0]
    left = [10 ** 6]
    diff = 10 ** 6
    for i in range(1, n):
        if c[i] != c1:
            diff = 1
            c1 = c[i]
        else:
            diff += 1
        left += [diff]
    right = [10 ** 6]
    c1 = c[-1]
    diff = 10 ** 6
    for i in range(1, n):
        if c[(n - 1) - i] != c1:
            diff = 1
            c1 = c[(n - 1) - i]
        else:
            diff += 1
        right += [diff]
    right.reverse()  
    for i in range(n):
        print(min(left[i], right[i]), end=' ')
    print()
    # for color c[1:]
    # for i, v in enumerate(c):
    #     color_dic[v].append(i)
    # for i, v in enumerate(c):
    #     index = bisect.bisect_left(color_dic[v], i)
    #     if index == len(color_dic):
    #         ans.append(abs(color_dic[v][-1] - i))
    #     elif index == 0:
    #         ans.append(abs(color_dic[v][0] - i))
    #     else:
    #         ans.append(min(abs(color_dic[v][index - 1] - i), abs(color_dic[v][index] - i)))
    # print(*ans)
    return

# ==============================================================


def i_single(input_type: type = int):  # 単一入力
    return input_type(input())


def i_multi(input_type: type = int, sep=" "):  # 複数入力
    return map(input_type, input().split(sep))


def i_list(input_type: type = int, sep=" "):  # リスト入力
    return list(map(input_type, input().split(sep)))


def o_judge(judge: bool):  # 判定出力
    print("Yes" if judge else "No")


def cumulative_sum(l: list[int]):  # 累積和を求める
    ans = [0] * (len(l) + 1)
    for i in range(1, len(l)):
        ans[i] = ans[i - 1] + l[i - 1]
    return ans


class SegmentTree:
    """
    点更新・区間取得を行う非再帰セグメント木
    """

    def __init__(
        self, size_or_arr: int | list[int], op: Callable[[int, int], int], identity: int
    ):
        self.op = op
        self.identity = identity

        if isinstance(size_or_arr, int):
            self.n = size_or_arr
            self.tree = [identity] * (2 * self.n)
        else:
            self.n = len(size_or_arr)
            self.tree = [identity] * (2 * self.n)
            # 初期データのセット
            for i in range(self.n):
                self.tree[self.n + i] = size_or_arr[i]
            # 構築
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        """位置 i の値を val に更新: O(log N)"""
        p = i + self.n
        self.tree[p] = val
        while p > 1:
            p >>= 1
            self.tree[p] = self.op(self.tree[2 * p], self.tree[2 * p + 1])

    def query(self, l, r):
        """半開区間 [l, r) のクエリ処理: O(log N)"""
        res_l = self.identity
        res_r = self.identity
        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.tree[r], res_r)
            l >>= 1
            r >>= 1

        return self.op(res_l, res_r)


# ===================================================

if __name__ == "__main__":  # メイン処理
    main()
