# Tìm kiếm nhị phân
# Thuật toán lập


import array as arr

arr = arr.array("i", [])
n = int(input("Nhập số phần tử: "))
for i in range(n):
    arr.append(int(input('nhập phần tử thứ %d: ' % (i + 1))))


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:  # condition
        mid = (high + low) // 2  # lần 1
        # print(mid)
        if arr[mid] < x:
            low = mid + 1  # lần 2
            # print(low)
        elif arr[mid] > x:
            high = mid - 1  # lần 3
            # print(high)
        else:
            return mid
    return -1


x = 10

print(binary_search(arr, x))
