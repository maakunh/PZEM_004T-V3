#pzem_004t_modify_poweralert.py
#Create: 10/05/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/PZEM_004T-V3

# For example of use modify_poweralert()
# Run as:
# python3 pzem_004t_modify_poweralert.py

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
    #port = "/dev/tty.usbserial-A50285BI"    #change this parameter by your environment

    #before reset energy
    cls.conn(port)
    cls.read_registers()
    print("power: ", cls.power)
    print("before: ", cls.alarm)

    #change power alert threshold
    cls.modify_poweralert(1000) #change this parameter[W]

    cls.wait(sec=2)

    cls.read_registers()
    print("power: ", cls.power)
    print("after: ", cls.alarm)


if __name__ == '__main__':
    main()

