import apigpio.api_gpio as api_gpio
import config

def init_projector():
    api_gpio.init_pin(17)

def deinit_projector():
    api_gpio.deinit_pin(17)

def on_projector():
    api_gpio.on_pin(17)
    

def off_projector():
    api_gpio.off_pin(17)
    
def toggle_projector():
    if config.projector :
        off_projector()
        config.projector = False
    elif not config.projector:
        on_projector()
        config.projector = True
