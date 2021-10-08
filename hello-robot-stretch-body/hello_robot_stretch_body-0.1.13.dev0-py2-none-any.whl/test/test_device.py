import unittest
import stretch_body.device

import time


class TestDevice(unittest.TestCase):

    def test_disable_existing_loggers(self):
        """Test multiple instances of device class all have enabled loggers.

        The logging param 'disable_existing_loggers' is set True so that loggers
        from imported python libraries don't print to the console. However, this
        means stretch_body classes can only initialize loggers after the config
        is loaded. We initialize config as class variables of Device for this.
        """
        d1 = stretch_body.device.Device('wrist_yaw') # loads logging config
        d2 = stretch_body.device.Device('stretch_gripper')
        d1.logger.info('hi')
        d2.logger.info('hi')
        # TODO: capture logging with https://testfixtures.readthedocs.io/en/latest/logging.html
        #       verify output is '[INFO][wrist_yaw]hi\n[INFO][stretch_gripper]hi\n'

    def test_threaded(self):
        class SometimesThreadedDevice(stretch_body.device.Device):
            def __init__(self):
                stretch_body.device.Device.__init__(self)
            def startup(self, threaded=False):
                self.pulling_status = False
                stretch_body.device.Device.startup(self, threaded=threaded)
            def pull_status(self):
                self.pulling_status = True

        # not threaded
        d = SometimesThreadedDevice()
        d.startup()
        time.sleep(0.1)
        self.assertFalse(d.pulling_status)
        time.sleep(0.1)
        self.assertFalse(d.pulling_status)
        d.stop()

        # threaded
        d.startup(threaded=True)
        time.sleep(0.1)
        self.assertTrue(d.pulling_status)
        time.sleep(0.1)
        self.assertTrue(d.pulling_status)
        d.stop()

        # not threaded
        d.startup()
        time.sleep(0.1)
        self.assertFalse(d.pulling_status)
        time.sleep(0.1)
        self.assertFalse(d.pulling_status)
        d.stop()
