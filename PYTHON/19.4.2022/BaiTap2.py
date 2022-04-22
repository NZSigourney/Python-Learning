import array as arr

number_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
a = arr.array('d', number_list)
r = int(input('Vị trí bạn muốn thay thế: '))
n = float(input('Nhập số nguyên muốn nhập: '))
a.insert(r, n)
print('Trước khi chèn: \n\t', number_list)
print('Sau khi chèn: \n\t', a)