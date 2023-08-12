from datetime import datetime

from engine.capulet_engine import CapuletEngine
from Battery.nubbin_battery import NubbinBattery

class Thovex(NubbinBattery,CapuletEngine):
    
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        CapuletEngine.__init__(self, current_mileage, last_service_mileage)
    
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False

