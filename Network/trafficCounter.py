import psutil

class traffic_counter(object):
    """Counts system network traffic"""
    def __init__(self, updatePeriod, beVerbose = True):
        self.updatePeriod = updatePeriod
        self.sent = None
        self.recv = None
        self.beVerbose = beVerbose

    def get_total_traffic(self):
        counter = psutil.net_io_counters()
        if counter:
            sent, recv = counter.bytes_sent, counter.bytes_recv
            if self.sent and self.recv:
                deltaSent = sent - self.sent
                deltaRecv = recv - self.recv
                speedSent = (deltaSent / self.updatePeriod) / 1024
                speedRecv = (deltaRecv / self.updatePeriod) / 1024
                if self.beVerbose:
                    print("Recv: {:f} kB/s".format(speedRecv))
                    print("Sent: {:f} kB/s".format(speedSent))
                    print("Total: {:f} kB/s".format(speedRecv + speedSent))
                    return speedRecv, speedSent, (speedSent + speedRecv)


            self.sent = sent
            self.recv = recv
