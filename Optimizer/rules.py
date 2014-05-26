K = lambda x: x * 8
k = lambda x: x / 8
m = lambda x: x * 128


class products(object):
    def __init__(self, speed, cost, id):
        self.speed = speed
        self.cost = cost
        self.id = id

ranges = {}

ranges[lambda x: x < k(416)] = products(320, 300, "POS-MA6-0002")
ranges[lambda x: k(416) < x <= k(512)] = products(416, 350, "POS-MA6-0003")
ranges[lambda x: k(512) < x <= k(640)] = products(512, 400, "POS-MA6-0004")
ranges[lambda x: k(640) < x <= k(768)] = products(640, 450, "POS-MA6-0005")
ranges[lambda x: k(768) < x <= k(896)] = products(768, 500, "POS-MA6-0006")
ranges[lambda x: k(896) < x <= m(1)]   = products(896, 550, "POS-MA6-0007")
ranges[lambda x: m(1) < x <= m(1.3)]   = products(1.0, 550, "POS-MA6-0008")
ranges[lambda x: m(1.3) < x <= m(1.7)] = products(1.3, 650, "POS-MA6-0009")
ranges[lambda x: m(1.7) < x <= m(2.1)] = products(1.7, 700, "POS-MA6-0010")
ranges[lambda x: m(2.1) < x <= m(3.1)] = products(2.1, 750, "POS-MA6-0011")
ranges[lambda x: m(3.1) < x <= m(4.1)] = products(3.1, 800, "POS-MA6-0012")
ranges[lambda x: m(4.1) < x <= m(5.1)] = products(4.1, 850, "POS-MA6-0013")
ranges[lambda x: m(5.0) < x <= m(5.7)] = products(5.0, 900, "POS-MA6-0014")
ranges[lambda x: m(5.7) < x <= m(6.4)] = products(5.7, 950, "POS-MA6-0015")
ranges[lambda x: m(6.4) < x <= m(7.1)] = products(6.4, 1000, "POS-MA6-0016")
ranges[lambda x: m(7.1) < x <= m(7.8)] = products(7.1, 1050, "POS-MA6-0017")
ranges[lambda x: m(7.8) < x <= m(8.5)] = products(7.8, 1100, "POS-MA6-0018")
ranges[lambda x: m(8.5) < x <= m(9.2)] = products(8.5, 1150, "POS-MA6-0019")
ranges[lambda x: m(9.2) < x <= m(10)] = products(9.2, 1200, "POS-MA6-0020")
ranges[lambda x: m(10) < x <= m(15)] = products(10, 1250, "POS-MA6-0021")
ranges[lambda x: m(12) < x <= m(15)] = products(12, 1350, "POS-MA6-0022")
ranges[lambda x: m(15) < x <= m(20)] = products(15, 1350, "POS-MA6-0023")
ranges[lambda x: x > m(20)] = products(20, 1400, "POS-MA6-0024")