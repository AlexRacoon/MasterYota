#!/usr/bin/python

import time
from Network import trafficCounter


class NetworkManager(object):
    def __init__(self, refresh=10):
        self.refresh = refresh
        self.tryStop = False
        counter = trafficCounter.traffic_counter(self.refresh, True)

        while not self.tryStop:
            recv, sent, total = counter.get_total_traffic()
#            optimizer.optimize(total)
            time.sleep(self.refresh)

    def trystop(self):
         self.tryStop = True

if __name__ == '__main__':
    print('-= Welcome to Network Watcher =-')
    watcher = NetworkManager()



