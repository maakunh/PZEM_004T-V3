#pzem_004t_read_registers.py
#Create: 10/05/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/PZEM_004T-V3

# For example of use read_registers()
# Run as:
# python3 pzem_004t_read_registers.py


#import original module
import pzem_004t_functions
import sys

def main():
    if (len(sys.argv) < 1):
        print("Usage: pzem_004t_reset_energy.py <port>")
        sys.exit(0)
    else:
        port = sys.argv[1]  # Windows -> COM*, Linux -> /dev/ttyUSB*, Mac -> /dev/tty.usb*

    #Initialize
    cls = pzem_004t_functions.functions()
    #port = "/dev/tty.usbserial-1410"    #change this parameter by your environment

    cls.conn(port)
    cls.read_registers()
    print('voltage [v]: ', cls.voltage)
    print('current [a]: ', cls.current)
    print('power [w]: ', cls.power)  # active power (v * i * power factor)
    print('energy [wh]: ', cls.energy)
    print('frequency [hz]: ', cls.frequency)
    print('power factor []: ', cls.powerfactor)
    print('alarm : ', cls.alarm)
    cls.close()

if __name__ == '__main__':
    main()

