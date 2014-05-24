from Optimizer import rules


def optimize(reqman, totalSpeed):
    if not totalSpeed:
        return

    speed = None

    for rule, sp in rules.ranges.items():
        if rule(totalSpeed):
            speed = sp

    if speed:
        switchTo(speed, reqman)


def switchTo(speed, reqman):
    print("Switching to {:f} speed, {:d} a day".format(speed.speed, speed.cost))
    reqman.changeLimit(speed)
