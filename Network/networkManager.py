import psutil

class network_manager(object):
    def __init__(self):
        pass

    def get_network_devices(self):
        devices = psutil.net_connections()
