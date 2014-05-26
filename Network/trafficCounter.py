import psutil
import datetime


class traffic_counter(object):
    """Counts system network traffic"""
    def __init__(self):
        self.sent = None
        self.recv = None
        self.last_check = None

    def get_total_traffic(self):
        counter = psutil.net_io_counters()
        if counter:
            sent, recv = counter.bytes_sent, counter.bytes_recv
            if self.sent and self.recv and self.last_check:
                delta_sent = sent - self.sent
                delta_recv = recv - self.recv
                now = datetime.datetime.now()
                delta_time = now - self.last_check

                speed_sent = (delta_sent / delta_time.seconds) / 1024
                speed_recv = (delta_recv / delta_time.seconds) / 1024

                self.sent = sent
                self.recv = recv
                self.last_check = now

                print("Total: {:f} kB/s".format(speed_recv + speed_sent))
                return speed_sent + speed_recv
            else:
                self.sent = sent
                self.recv = recv
                self.last_check = datetime.datetime.now()
                return None, None, None

