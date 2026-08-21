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
from typing import Callable, Counter


# ====================================================================
def main():
    n, m = i_multi()
    s = input()
    cal = list(s.split('0'))
    need = 0
    
    need_no = []
    need_logo = []
    need_shirt = []

    for c in cal:
        no = 0
        logo = 0
        for i in range(len(c)):
            if c[i] == '1':
                no += 1
            elif c[i] == '2':
                logo += 1

        need_logo.append(logo)
        need_no.append(no)
        need_shirt.append(logo + no)

    max_no = max(need_no)
    max_logo = max(need_logo)
    max_shirt = max(need_shirt)

    if max_no > m:
        need = max_no - m

    need = max(need, max_logo)

    if max_shirt > need + m:
        need = max_shirt - m

    print(need)
    
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
    ans = [l[0]]
    for i in range(1, len(l)):
        ans[i] = ans[i - 1] + l[i]
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
