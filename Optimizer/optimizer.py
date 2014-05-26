from Optimizer import rules
from Yota import requester


def optimize(totalSpeed, creds):
    if not totalSpeed:
        return
    product = None
    for rule, prod in rules.ranges.items():
        if rule(totalSpeed):
            product = prod
            break

    if product:
        switch(product, creds)


def switch(speed, creds):
    print("Switching to {:f} speed, {:d}R/month".format(speed.speed, speed.cost))
    reqman = requester.reqman(creds)
#    reqman.change_limit(speed.id)
