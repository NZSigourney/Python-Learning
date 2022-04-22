import array as arr

a = arr.array('i', [])
b = arr.array('i', [1, 5, 3, 8, 7, 6])
def DanhSach():
    n = int(input('Nhập số phần tử: '))
    for i in range(n):
        a.append(int(input('Nhập Số thứ ' + str(i+1) + ': ')))
    print(a)
DanhSach()

# Bài 1:
def append(n):
    #n = int(input('Nhập số: '))
    a.append(n)
    print(a)

n = int(input('Nhập số muốn thêm: '))
append(n)

# Bài 2:
def insert(data, value):
    a.insert(data, value)
    print(a)

n1 = int(input('Nhập vị trí cần chèn: '))
n1_2 = int(input('Nhập số cần chèn: '))
insert(n1, n1_2)

# Bài 3:
def remove(n):
    a.remove(n)
    print(a)

n2 = int(input('Nhập số muốn xóa: '))
remove(n2)

# Bài 4:
def cuts(data, value):
    print(a[data:value])

n3 = int(input('Nhập số (data): '))
n3_1 = int(input('Nhập số (Value): '))
cuts(n3, n3_1)

# Bài 5:
c = a+b
print('Array =', c)