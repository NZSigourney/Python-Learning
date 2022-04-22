class SinhVien:
    def __init__(self, maSO, HoTen, Diem):
        self.maSO = maSO
        self.HoTen = HoTen
        self.Diem = Diem

HSG = SinhVien('SV01', 'Thái Duy Vũ', 10)
print('Mã số Sinh Viên {}, Họ tên {}, Số điểm Tổng là {}' . format(HSG.maSO, HSG.HoTen, HSG.Diem))