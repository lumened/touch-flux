#!/usr/bin/python
# This file provides an interface for GPIO pins

def init_pin(pin):
    
    try:
        f= open ('/sys/class/gpio/unexport','w')
        f.write(str(pin))
        f.close()
    except:
        pass
    
    f= open ('/sys/class/gpio/export','w')
    f.write(str(pin))
    f.close()
    
    path = '/sys/class/gpio/gpio' + str(pin) + '/direction'
    f= open (path,'w')
    f.write('out')
    f.close()


def on_pin(pin):
    path = '/sys/class/gpio/gpio' + str(pin) + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    
def off_pin(pin):
    path = '/sys/class/gpio/gpio' + str(pin) + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    

def deinit_pin(pin):
    try:
        f= open ('/sys/class/gpio/unexport','w')
        f.write(str(pin))
        f.close()
    except:
        pass


    
init_pin(17)
off_pin(17)
