from Yota import authenticator
from Yota import requester
from Optimizer import rules

def optimize(reqman, totalSpeed):
    if not totalSpeed:
        return

    if speed:
        _switchTo(speed, reqman)

def _switchTo(speed, reqman):
    print("Switching to {:d} speed, {:d} a day".format(speed.speed, speed.cost))
    reqman.changeLimit(speed)
        
