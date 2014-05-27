from Optimizer import rules
from Yota import requester


class optimizer(object):
    def __init__(self, nw):
        self.nw = nw

    def optimize(self, totalSpeed, creds):
        if not totalSpeed:
            return
        product = None
        for rule, prod in rules.ranges.items():
            if rule(totalSpeed):
                product = prod
                break

        if product != self.nw.product:
            self._switch(product, creds)
            self.nw.product = product
        else:
            print("Already on the needed product")

    @staticmethod
    def _switch(speed, creds):
        print("Switching to {:f} speed, {:d}R/month".format(speed.speed, speed.cost))
        reqman = requester.reqman(creds)
    #    reqman.change_limit(speed.id)
