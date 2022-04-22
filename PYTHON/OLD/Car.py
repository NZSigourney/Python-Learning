class xe_Oto:
    loaixe = "Ô tô"
    def __init__(self, nhanhieu, mauxe, bienso):
        self.nhanhieu = nhanhieu
        self.mauxe = mauxe
        self.bienso = bienso
        
mer = xe_Oto("Mer", "Xám", "3456")
lamborghini = xe_Oto('Lamborghini', 'Vàng', '5210')
print("Xe {} có màu {}. biển số xe là {}. Là xe {}". format( mer.nhanhieu, mer.mauxe, mer.bienso, mer.__class__.loaixe))
print("Xe {} có màu {}. biển số xe là {}. Là xe {}". format(lamborghini.nhanhieu, lamborghini.mauxe, lamborghini.bienso, lamborghini.__class__.loaixe))