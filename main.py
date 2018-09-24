# main.py -- put your code here!
from pyb import Pin, ADC, UART
adc = ADC(Pin('X1'))
while True:
    uart = UART(1, 9600)
    x = adc.read()
    if x > 100:
            uart.write(str(x))
            uart.write('\n')
            pyb.delay(100)
    else:
            uart.write('0')
            uart.write('\n')
            pyb.delay(10)


