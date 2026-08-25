# from collections import Counter
from ast import increment_lineno
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
    h, w, k = i_multi()
    grid = [input() for _ in range(h)]
    reach = [[k + 1 for _ in range(w)] for _ in range(h)]
    # print(reach)
    count = 0
    safe_w = [True] * w
    safe_h = [True] * h
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                safe_h[i] = False
                safe_w[j] = False
    # print(safe_h)
    # print(safe_w)
    safe = [(i, j, 0) for j in range(w) for i in range(h) if safe_h[i] and safe_w[j]]
    # print(safe)
    reached = [[False for _ in range(w)] for _ in range(h)]
    for i, j, _ in safe:
        reached[i][j] = True
    # print(safe)
    q = deque(safe)
    while q:
        t = q.popleft()
        x, y, l = t
        reach[x][y] = min(l, reach[x][y])
        if l < k:
            if x > 0:
                if not(reached[x - 1][y]) and grid[x - 1][y] == ".":
                    q.append((x - 1, y, l + 1))
                    reached[x - 1][y] = True
                    
            if x < h - 1:
                if not(reached[x + 1][y]) and grid[x + 1][y] == ".":
                    q.append((x + 1, y, l + 1))
                    reached[x + 1][y] = True
                    
            if y > 0:
                if not(reached[x][y - 1]) and grid[x][y - 1] == ".":
                    q.append((x, y - 1, l + 1))
                    reached[x][y - 1] = True
                    
            if y < w - 1:
                if not(reached[x][y + 1]) and grid[x][y + 1] == ".":
                    q.append((x, y + 1, l + 1))
                    reached[x][y + 1] = True
                    
        # print(reach)
    for i in range(h):
        for j in range(w):
            if reach[i][j] <= k:
                count += 1
    # print(reach)        
    print(count)
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
