from datetime import date
from dateutil.relativedelta import relativedelta


class Battery:

    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date + relativedelta(years=+2) >= self.current_date:
            return True
        else:
            return False


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date + relativedelta(years=+4) >= self.current_date:
            return True
        else:
            return False

