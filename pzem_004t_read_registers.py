#pzem_004t_read_registers.py
#Create: 10/05/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/PZEM_004T-V3

# For example of use read_registers()
# Run as:
# python3 pzem_004t_read_registers.py


#import original module
import pzem_004t_functions

def main():
    #Initialize
    cls = pzem_004t_functions.functions()
    port = "/dev/tty.usbserial-A50285BI"    #change this parameter by your environment

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

