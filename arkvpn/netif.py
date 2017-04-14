"""This class helps validate the network interface status"""
import netifaces

class NetIf(object):
    def __init__(self, interface):
        self.interface = interface

    def is_interface_up(interface):
        addr = netifaces.ifaddresses(interface)
        return netifaces.AF_INET in addr
