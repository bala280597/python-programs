import subprocess
import optparse

parser= optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface to change MAC address")
parser.add_option("-m","--mac",dest="mac",help="Resultant MAC address")
parser.parse_args()

interface = input("Enter the interface")
mac = input("Enter MAC")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])
print(f"Changing MAC address of {interface} to {mac}")
