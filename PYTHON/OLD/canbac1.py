class CanBac1:
    def ketQua(self, a, b):
        if a == 0:
            print('Vui lòng nhập số khác 0!')
            a = int(input('Nhập A: '))
        else:
            c = (-b/a)
            print('Can Bac 1 cua ax + b = 0 là', c)

# def giaiPT(a, b):
#    c = CanBac1.ketQua(a, b)
#    print(c)

a = int(input('Nhập A: '))
b = int(input('Nhập B: '))
print(giaiPT(a, b))