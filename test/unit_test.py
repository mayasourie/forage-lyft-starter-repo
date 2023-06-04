import unittest
import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class UnitTests(unittest.TestCase):

    def test_capulet_needs_service(self):
        capulet = CapuletEngine(40000, 9000)
        self.assertTrue(CapuletEngine.needs_service(capulet))

    def test_capulet_needs_service_false(self):
        capulet = CapuletEngine(23000, 9000)
        self.assertFalse(CapuletEngine.needs_service(capulet))

    def test_sternman_needs_service(self):
        sternman = SternmanEngine(True)
        self.assertTrue(SternmanEngine.needs_service(sternman))

    def test_sternman_needs_service_false(self):
        sternman = SternmanEngine(False)
        self.assertFalse(SternmanEngine.needs_service(sternman))

    def test_willoughby_needs_service(self):
        willoughby = WilloughbyEngine(80000, 15000)
        self.assertTrue(WilloughbyEngine.needs_service(willoughby))

    def test_willoughby_needs_service_false(self):
        willoughby = WilloughbyEngine(55000, 15000)
        self.assertFalse(WilloughbyEngine.needs_service(willoughby))


class BatteryUnitTests(unittest.TestCase):

    def test_nubbin_needs_service(self):
        nubbin = NubbinBattery(datetime.datetime(2023, 3, 18), datetime.datetime(2015, 5, 11))
        self.assertTrue(NubbinBattery.needs_service(nubbin))

    def test_nubbin_needs_service_false(self):
        nubbin = NubbinBattery(datetime.datetime(2023, 3, 18), datetime.datetime(2020, 8, 9))
        self.assertFalse(NubbinBattery.needs_service(nubbin))

    def test_spindler_needs_service(self):
        spindler = SpindlerBattery(datetime.datetime(2023, 5, 21), datetime.datetime(2020, 9, 15))
        self.assertTrue(SpindlerBattery.needs_service(spindler))

    def test_spindler_needs_service_false(self):
        spindler = SpindlerBattery(datetime.datetime(2023, 6, 2), datetime.datetime(2022, 10, 21))
        self.assertFalse(SpindlerBattery.needs_service(spindler))


if __name__ == '__main__':
    unittest.main()
