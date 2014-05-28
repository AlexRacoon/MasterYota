#!/usr/bin/python

__author__ = "Chad J. Schroeder"
__revision__ = "$Id$"
__version__ = "0.2"

import time
from Network import trafficCounter
from Optimizer import optimizer
import argparse
from Yota import requester


class Credentials(object):
    def __init__(self):
        self.email = None
        self.passw = None
        self.account = None

    def fill_payload(self, payload):
        if self.email and self.passw and self.account:
            payload['IDToken1'] = self.account
            payload['old-token'] = self.email
            payload['IDToken2'] = self.passw
        else:
            raise ValueError


class NetworkManager(object):
    def __init__(self, creds, refresh=10):
        self.refresh = refresh
        self.interrupt = False
        self.counter = trafficCounter.TrafficCounter()
        self.creds = creds
        self.product = self._get_product()

    def start(self):
        while not self.interrupt:
            total = self.counter.get_total_traffic()
            opt = optimizer.optimizer(self)
            opt.optimize(total, self.creds)
            time.sleep(self.refresh)

    def stop(self):
        self.interrupt = True

    def _get_product(self):
        req = requester.reqman(self.creds)
        return req.parse_selected_product()



def main(argv):
    creds = Credentials()
    creds.account = argv["account"]
    creds.passw = argv["password"]
    creds.email = argv["email"]
    watcher = NetworkManager(creds)
    watcher.start()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Yota traffic optimizer')
    p.add_argument('-a', '--account', type=str, help='Account#')
    p.add_argument('-e', '--email', type=str, help='Email')
    p.add_argument('-p', '--password', type=str, help='Password')
    args = p.parse_args()
    main(vars(args))