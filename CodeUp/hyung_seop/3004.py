#나의 풀이 : 
# 1. 일단 데이터를 받고 그 데이터를 리스트로 구성한다
# 2. 리스트로 구성한 데이터를 정렬한 후
# 3. 원래의 데이터의 리스트의 값을 이진탐색하여 그 때의 인덱스를 출력.

import bisect

def binary_search(L, data):
    start_index = 0
    end_index = len(L) - 1
    while start_index <= end_index: ### 중요 (<=)
        mid_index = (start_index+end_index)//2
        if data == L[mid_index]:
            return mid_index
        elif data < L[mid_index]:
            end_index = mid_index - 1
        else: #data > L[mid_index]
            start_index = mid_index + 1

n = int(input())
data_list = []
data_sort = []
data_list = list(map(int, input().split()))
data_sort = sorted(data_list) # sorted 는 새로운 개체로 생성시킴
# for i in data_list:
#     pos = bisect.bisect(data_sort, i)
#     print(pos, end=' ')
for i in data_list:
    index = binary_search(data_sort, i)
    print(index, end=' ')