from Optimizer import rules
from Yota import requester


def optimize(totalSpeed):
    if not totalSpeed:
        return
    product = None
    for rule, prod in rules.ranges.items():
        if rule(totalSpeed):
            product = prod
            if prod.speed > 30:
                print("Product speed converted: {:f}".format(rules.k(prod.speed)))
            else:
                print("Product speed converted: {:f}".format(rules.m(prod.speed)))
            break

    if product:
        switchTo(product)


def switchTo(speed):
    print("Switching to {:f} speed, {:d}R/month".format(speed.speed, speed.cost))
    reqman = requester.reqman("alexbecoon@gmail.com", "xtoxphcxlx", "6034675940", True)
    reqman.change_limit(speed.id)
