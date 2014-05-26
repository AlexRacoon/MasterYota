#!/usr/bin/python

__author__ = "Chad J. Schroeder"
__revision__ = "$Id$"
__version__ = "0.2"

import time
import sys
import getopt
from Network import trafficCounter
from Optimizer import optimizer


class Credentials(object):
    def __init__(self):
        self.login = None
        self.passw = None
        self.account = None

    def __init__(self, login, passw, account):
        self.login = login
        self.passw = passw
        self.account = account

    def fill_payload(self, payload):
        if self.login and self.passw and self.account:
            payload['IDToken1'] = self.account
            payload['old-token'] = self.login
            payload['IDToken2'] = self.passw
        else:
            raise ValueError


class NetworkManager(object):
    def __init__(self, creds, refresh=10):
        self.refresh = refresh
        self.interrupt = False
        self.counter = trafficCounter.traffic_counter()
        self.creds = creds

    def start(self):
        while not self.interrupt:
            total = self.counter.get_total_traffic()
            optimizer.optimize(total, self.creds)
            time.sleep(self.refresh)

    def stop(self):
        self.interrupt = True


def main(argv):
    creds = Credentials()
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["email=", "account=", "passw="])
    except getopt.GetoptError:
        print('test.py --email <email> --account <account> --passw <passw>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py --email <email> --account <account> --passw <passw>')
            sys.exit()
        elif opt in ("-e", "--email"):
            creds.login = arg
        elif opt in ("-p", "--passw"):
            creds.passw = arg
        elif opt in ("-a", "account"):
            creds.account = arg

    watcher = NetworkManager(creds)
    watcher.start()


if __name__ == '__main__':
    print('-= Welcome to Network Watcher =-')
    main(sys.argv[:1])