import unittest

from mdssdk.vsan import Vsan
from mdssdk.zone import Zone
from tests.test_zone.vars import *

log = logging.getLogger(__name__)


class TestZoneAttrFulldbZoneCount(unittest.TestCase):
    def __init__(self, testName, sw):
        super().__init__(testName)
        self.switch = sw

    def setUp(self) -> None:
        log.debug(self.switch.version)
        log.debug(self.switch.ipaddr)
        self.vsandb = self.switch.vsans
        while True:
            self.id = get_random_id()
            if self.id not in self.vsandb.keys():
                break
        self.v = Vsan(switch=self.switch, id=self.id)
        self.v.create()
        self.z = Zone(self.switch, "test_zone", self.id)

    def test_fulldb_zone_count_read(self):
        self.z.create()
        log.debug("Full DB Zone Count : " + str(self.z.fulldb_zone_count))
        self.assertEqual(1, self.z.fulldb_zone_count)

    def test_fulldb_zone_count_read_nonexisting(self):
        log.debug("Full DB Zone Count(nonexisting) : " + str(self.z.fulldb_zone_count))
        self.assertEqual(0, self.z.fulldb_zone_count)

    def test_fulldb_zone_count_write_error(self):
        with self.assertRaises(AttributeError) as e:
            self.z.fulldb_zone_count = "asdf"
        self.assertEqual("can't set attribute", str(e.exception))

    def tearDown(self) -> None:
        self.v.delete()
