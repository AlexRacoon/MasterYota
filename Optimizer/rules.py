K = lambda x: x * 8
k = lambda x: x / 8
m = lambda x: x * 128


class Product(object):
    def __init__(self, speed, cost, id):
        self.speed = speed
        self.cost = cost
        self.id = id


ranges = {lambda x: x < k(320): Product(320, 300, "POS-MA6-0002"),
          lambda x: k(320) <= x < k(416): Product(416, 350, "POS-MA6-0003"),
          lambda x: k(416) <= x < k(512): Product(512, 400, "POS-MA6-0004"),
          lambda x: k(512) <= x < k(640): Product(640, 450, "POS-MA6-0005"),
          lambda x: k(640) <= x < k(768): Product(768, 500, "POS-MA6-0006"),
          lambda x: k(768) <= x < k(896): Product(896, 550, "POS-MA6-0007"),
          lambda x: k(896) <= x < m(1.0): Product(1.0, 550, "POS-MA6-0008"),
          lambda x: m(1.0) <= x < m(1.3): Product(1.3, 650, "POS-MA6-0009"),
          lambda x: m(1.3) <= x < m(1.7): Product(1.7, 700, "POS-MA6-0010"),
          lambda x: m(1.7) <= x < m(2.1): Product(2.1, 750, "POS-MA6-0011"),
          lambda x: m(2.1) <= x < m(3.1): Product(3.1, 800, "POS-MA6-0012"),
          lambda x: m(3.1) <= x < m(4.1): Product(4.1, 850, "POS-MA6-0013"),
          lambda x: m(4.1) <= x < m(5.0): Product(5.0, 900, "POS-MA6-0014"),
          lambda x: m(5.0) <= x < m(5.7): Product(5.7, 950, "POS-MA6-0015"),
          lambda x: m(5.7) <= x < m(6.4): Product(6.4, 1000, "POS-MA6-0016"),
          lambda x: m(6.4) <= x < m(7.1): Product(7.1, 1050, "POS-MA6-0017"),
          lambda x: m(7.1) <= x < m(7.8): Product(7.8, 1100, "POS-MA6-0018"),
          lambda x: m(7.8) <= x < m(8.5): Product(8.5, 1150, "POS-MA6-0019"),
          lambda x: m(8.5) <= x < m(9.2): Product(9.2, 1200, "POS-MA6-0020"),
          lambda x: m(9.2) <= x < m(10): Product(10, 1250, "POS-MA6-0021"),
          lambda x: m(10) <= x < m(12): Product(12, 1350, "POS-MA6-0022"),
          lambda x: m(12) <= x < m(15): Product(15, 1350, "POS-MA6-0023"),
          lambda x: m(15) <= x: Product(20, 1400, "POS-MA6-0024")}
