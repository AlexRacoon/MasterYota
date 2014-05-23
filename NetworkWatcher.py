import sys
import time
from Network import trafficCounter


class network_watcher(object):
    def __init__(self, refreshPeriod = 5):
        self.refreshPeriod = refreshPeriod
        self.tryStop = False
        counter = trafficCounter.traffic_counter(self.refreshPeriod, True)

        while not self.tryStop:
            counter.get_total_traffic()
            time.sleep(self.refreshPeriod)


if __name__ == '__main__':
    print('-= Welcome to Network Watcher =-')
    for arg in sys.argv:
        print(arg)

    watcher = network_watcher()



