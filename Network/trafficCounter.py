import psutil
import datetime

class traffic_counter(object):
    """Counts system network traffic"""
    def __init__(self, updatePeriod, beVerbose = True):
        self.updatePeriod = updatePeriod
        self.sent = None
        self.recv = None
        self.beVerbose = beVerbose
        self.lastCheck = None

    def get_total_traffic(self):
        counter = psutil.net_io_counters()
        if counter:
            sent, recv = counter.bytes_sent, counter.bytes_recv
            if self.sent and self.recv and self.lastCheck:
                deltaSent = sent - self.sent
                deltaRecv = recv - self.recv
                now = datetime.datetime.now()
                deltaTime = now - self.lastCheck

                speedSent = (deltaSent / deltaTime.seconds) / 1024
                speedRecv = (deltaRecv / deltaTime.seconds) / 1024

                self.sent = sent
                self.recv = recv
                self.lastCheck = now

                if self.beVerbose:
                    print("Recv: {:f} kB/s".format(speedRecv))
                    print("Sent: {:f} kB/s".format(speedSent))
                    print("Total: {:f} kB/s".format(speedRecv + speedSent))

                return speedRecv, speedSent, (speedSent + speedRecv)
            else:
                self.sent = sent
                self.recv = recv
                self.lastCheck = datetime.datetime.now()
                return None, None, None

