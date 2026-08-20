# from collections import Counter
import bisect
import fractions
import heapq
import itertools
import math
import pprint
import queue
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
    n, w, m = i_multi()
    membs = [i_list() for _ in range(n)]
    camp = {i: 0 for i in range(1, 8)}
    if m == 0:
        for memb in membs:
            g = []
            i = memb[0]
            while True:
                g.append(i)
                if i == memb[1]:
                    break
                i = (i % 7) + 1
    
            ans = len(g) * w
            print(ans)
    else:
        for _ in range(m):
            s, e = i_multi()
            i = ((s - 1) % 7) + 1
            j = ((e - 1) % 7) + 1
            for x in range(i, 8):
                camp[x] += 1
    
            for y in range(1, j + 1):
                camp[y] += 1
            for z in range(1, 8):
                camp[z] += (e - s + 1 - (7 - i + 1) - j) // 7
    
        for memb in membs:
            g = []
            i = memb[0]
            while True:
                g.append(i)
                if i == memb[1]:
                    break
                i = (i % 7) + 1
    
            ans = len(g) * w
            for d in g:
                ans += camp[d]
    
            print(ans)
    

    
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
