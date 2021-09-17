# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for i in course:
        ord_com = []
        for order in orders:
            ord_com += combinations(sorted(order), i)
        most_ordered = Counter(ord_com).most_common()
        result += [ combi for combi, num in most_ordered if num > 1 and num == most_ordered[0][1]]
    return [ ''.join(i) for i in sorted(result)]

'''
orders	                                          course	result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	  [2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                            [2,3,4]	["WX", "XY"]
'''
