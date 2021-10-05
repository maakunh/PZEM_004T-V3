#pzem_004t_modify_poweralert.py
#Create: 05/10/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/PZEM_004T-V3

# For example of use modify_poweralert()
# Run as:
# python3 pzem_004t_modify_poweralert.py

#import original module
import pzem_004t_functions

def main():
    #Initialize
    cls = pzem_004t_functions.functions()
    port = "/dev/tty.usbserial-A50285BI"    #change this parameter by your environment

    #before reset energy
    cls.conn(port)
    cls.read_registers()
    print("power: ", cls.power)
    print("before: ", cls.alarm)

    #change power alert threshold
    cls.modify_poweralert(1000) #change this parameter[W]
    cls.close()

    #after connection closed, the rusult is reflected.
    cls.conn(port)
    cls.read_registers()
    print("power: ", cls.power)
    print("after: ", cls.alarm)


if __name__ == '__main__':
    main()

