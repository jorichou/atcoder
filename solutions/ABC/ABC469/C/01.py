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
    s = input()
    no = [i for i in range(n) if s[i] == 'x']
    n_l = len(no)

    # def eat(g, eaten, next):
    #     if s[eaten] == 'o':
    #         g += 1
        
    #     if g == 0 or next >= n:
    #         return eaten
    #     else:
    #         return eat(g - 1, eaten + 1, next + 1)
            # if :
            #     return eat(g, eaten + 1, next + 1)
            # else:
            #     return eat(g - 1, eaten + 1, next + 1)

 
    
    for k in range(n):
        if n_l < k + 1:
            print(n)
        else:
            print(no[k] + 1)
        

if __name__ == "__main__":  # メイン処理
    main()
