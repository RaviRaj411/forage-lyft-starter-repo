from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from Battery.spindler_battery import SpindlerBattery

class Glissade(SpindlerBattery,WilloughbyEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        WilloughbyEngine.__init__(self, current_mileage, last_service_mileage)
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
