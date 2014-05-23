k = lambda x: x / 8
m = lambda x: x * 128

class speed_cost(object):
    def __init__(self, speed, cost):
        self.speed = speed
        self.cost = cost

ranges = {}


ranges[lambda x: x < k(416)] = speed_cost(320, 300)
ranges[lambda x: x > k(416) and x <= k(512)] = speed_cost(416, 350)
ranges[lambda x: x > k(512) and x <= k(640)] = speed_cost(512, 400)
ranges[lambda x: x > k(640) and x <= k(768)] = speed_cost(640, 450)
ranges[lambda x: x > k(768) and x <= k(896)] = speed_cost(768, 500)
ranges[lambda x: x > k(896) and x <= m(1)] = speed_cost(896, 550)
ranges[lambda x: x > m(1) and x <= m(1.3)] = speed_cost(1.0, 550)
ranges[lambda x: x > m(1.3) and x <= m(1.7)] = speed_cost(1.3, 650)
ranges[lambda x: x > m(1.7) and x <= m(2.1)] = speed_cost(1.7, 700)
ranges[lambda x: x > m(2.1) and x <= m(3.1)] = speed_cost(2.1, 750)
ranges[lambda x: x > m(3.1) and x <= m(4.1)] = speed_cost(3.1, 800)
ranges[lambda x: x > m(4.1) and x <= m(5.1)] = speed_cost(4.1, 850)
ranges[lambda x: x > m(5.1) and x <= m(5.7)] = speed_cost(5.1, 900)
ranges[lambda x: x > m(5.7) and x <= m(6.4)] = speed_cost(5.7, 950)
ranges[lambda x: x > m(6.4) and x <= m(7.1)] = speed_cost(6.4, 1000)
ranges[lambda x: x > m(7.1) and x <= m(7.8)] = speed_cost(7.1, 1050)
ranges[lambda x: x > m(7.8) and x <= m(8.5)] = speed_cost(7.8, 1100)
ranges[lambda x: x > m(8.5) and x <= m(9.2)] = speed_cost(8.5, 1150)
ranges[lambda x: x > m(9.2) and x <= m(10)] = speed_cost(9.2, 1200)
ranges[lambda x: x > m(10) and x <= m(15)] = speed_cost(10, 1250)
ranges[lambda x: x > m(15) and x <= m(20)] = speed_cost(15, 1350)
ranges[lambda x: x > m(20)] = speed_cost(20, 1400)