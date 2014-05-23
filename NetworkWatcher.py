import sys
import time
from Network import trafficCounter
from Optimizer import optimizer
from Yota import authenticator
from Yota import requester

class network_watcher(object):
    def __init__(self, refreshPeriod = 5):
        self.refreshPeriod = refreshPeriod
        self.tryStop = False
        counter = trafficCounter.traffic_counter(self.refreshPeriod, True)

        while not self.tryStop:
            recv, sent, total = counter.get_total_traffic()
            #TODO: get user and pass from command-line params on config
            authman = authenticator.authman("user", "pass", True)
            reqman = requester.reqman(authman, True)
            optimizer.optimize(reqman, total)
            time.sleep(self.refreshPeriod)

    def trystop(self):
         self.tryStop = True

if __name__ == '__main__':
    print('-= Welcome to Network Watcher =-')
    for arg in sys.argv:
        print(arg)

    watcher = network_watcher()



