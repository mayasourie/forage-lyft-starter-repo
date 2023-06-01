from engine import Engine
from battery import Battery


class Car:
    def __init__(self, engine, battery):
        self.engine = Engine(engine)
        self.battery = Battery(battery)

    def needs_service(self, engine, battery):
        pass
