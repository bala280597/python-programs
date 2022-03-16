import subprocess
import optparse

def mac_changer(interface,mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"Changing MAC address of {interface} to {mac}")

def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change MAC address")
    parser.add_option("-m","--mac",dest="mac",help="Resultant MAC address")
    (options,arguments) = parser.parse_args()
    if not options.mac:
        parser.error('Please specifyy the mac address')
    elif not options.interface:
        parser.error('Please specifyy the Interface name')
    else:
        return options

options = get_arguments()
mac_changer(mac=options.mac,interface=options.interface)
