import json,math,random
from distributions import distributions

class device:
    def __init__(self, ID, status, battery, charging,
                 free_memory, processor_speed):
        """
        id - uniquely identify a device (Android has Android ID)
        status - whether user is currently using it right now (0/1)
        battery - battery percentage (0 to 100)
        charging - whether the device is being charged right now (0/1)
        free_memory - RAM available in MB (variable)
        processor_speed - processor speed in MHz (variable)
        """
        self.id = ID
        self.status = status
        self.battery = battery
        self.charging = charging
        self.free_memory = free_memory
        self.processor_speed = processor_speed

    def get_info(self, json_response=False):
        """
        json_response - specify whether the response should be a json string
                        or a python dictionary
        """
        info_dict = {'id': self.id, 'status': self.status,
                     'battery': self.battery, 'charging': self.charging,
                     'free_memory': self.free_memory,
                     'processor_speed': self.processor_speed}
        if(json_response):
            return(json.dumps(info_dict))
        return(info_dict)
    
    @staticmethod
    def get_dummy_vals():
        """
        static method to return a list of dummy values, following the specified distribution
        """
        dummy = device(random.randint(0,1000),
                distributions.custom_30_70(),
                random.randint(0,100),
                distributions.custom_30_70(),
                random.randint(50,400),
                random.randint(800,2400))
        return(dummy.get_info(True))
