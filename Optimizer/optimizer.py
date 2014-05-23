from Yota import authenticator
from Yota import requester


def optimize(reqman, totalSpeed):
    if not totalSpeed:
        return
#TODO: make dictionary with constants
    elif totalSpeed < 300:
        _switchTo(350, reqman)
    elif totalSpeed < 600:
        _switchTo(650, reqman)
    elif totalSpeed < 1000:
        _switchTo(1150, reqman)
    elif totalSpeed < 1500:
        _switchTo(1350, reqman)
    else:
        pass

def _switchTo(speed, reqman):
    print("Switching to {:d}".format(speed))
    reqman.changeLimit(speed)
        
