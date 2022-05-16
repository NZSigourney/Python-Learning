class SinhVien:
    def __int__(self, MaSo, HoTen, Diem):
        self.value = MaSo, HoTen, Diem
        self.nextval = None


class PointerLinked:
    def __init__(self):
        self.headval = None
        self.lastval = None

    def append(self, MaSo, HoTen, Diem):
        SV = SinhVien(MaSo, HoTen, Diem)
        if self.headval is None:
            self.headval = SV
            self.lastval = SV
        else:
            self.lastval.nextval = SV
            self.lastval = SV

    def printlist(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.value, end="")
            printvalue = printvalue.value.nextval


def nts():
    a = int(input(">> "))
    array = []
    for i in range(a):
        array.append(SinhVien(int(input("Mã số: ")), str(input("Họ Tên: ")), float(input("Điểm: "))))
    for j in array:
        for i in j:
            print(i)


nts()
