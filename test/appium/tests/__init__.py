import asyncio
import logging
from datetime import datetime

from support.appium_container import AppiumContainer
from support.test_data import TestSuiteData


@asyncio.coroutine
def start_threads(quantity: int, func: type, returns: dict, *args):
    loop = asyncio.get_event_loop()
    for i in range(quantity):
        returns[i] = loop.run_in_executor(None, func, *args)
    for k in returns:
        returns[k] = yield from returns[k]
    return returns


def get_current_time():
    return datetime.now().strftime('%-m%-d%-H%-M%-S')


def debug(text: str):
    logging.debug(text)

pytest_config_global = dict()
test_suite_data = TestSuiteData()
appium_container = AppiumContainer()

common_password = 'qwerty'
unique_password = 'unique' + get_current_time()

bootnode_address = "enode://436cc6f674928fdc9a9f7990f2944002b685d1c37f025c1be425185b5b1f0900feaf1ccc2a6130268f9901be4a7d252f37302c8335a2c1a62736e9232691cc3a@178.128.138.128:443"
mailserver_address = "enode://ee2b53b0ace9692167a410514bca3024695dbf0e1a68e1dff9716da620efb195f04a4b9e873fb9b74ac84de801106c465b8e2b6c4f0d93b8749d1578bfcaf03e@104.197.238.144:443"
staging_fleet = 'eth.staging'
prod_fleet = 'eth.prod'
mailserver_ams = 'mail-01.do-ams3'
mailserver_hk = 'mail-01.ac-cn-hongkong-c'
mailserver_gc = 'mail-01.gc-us-central1-a'
mailserver_ams_01 = 'mail-01.do-ams3.eth.prod'
camera_access_error_text = "To grant the required camera permission, please go to your system settings " \
                           "and make sure that Status > Camera is selected."

photos_access_error_text = "To grant the required photos permission, please go to your system settings " \
                           "and make sure that Status > Photos is selected."

connection_not_secure_text = "Connection is not secure! " \
                             "Do not sign transactions or send personal data on this site."
connection_is_secure_text = "Connection is secure. Make sure you really trust this site " \
                            "before signing transactions or entering personal data."

test_dapp_url = 'status-im.github.io/dapp'
test_dapp_name = 'status-im.github.io'
