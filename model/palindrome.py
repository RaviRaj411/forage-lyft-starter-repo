from datetime import datetime

from engine.sternman_engine import SternmanEngine
from Battery.spindler_battery import SpindlerBattery

class Palindrome(SpindlerBattery,SternmanEngine):
    def __init__(self, last_service_date, warning_light_is_on ):
        super().__init__(last_service_date)
        SternmanEngine.__init__(self, warning_light_is_on)
    
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
