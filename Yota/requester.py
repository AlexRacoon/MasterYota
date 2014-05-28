import re
import requests
from Optimizer import rules
from Common.exceptions import catch_exception
from Common.exceptions import YotaError

class reqman(object):
    """sends requests to change the speed"""

    payloadAuth = {
        'goto': 'https://my.yota.ru:443/selfcare/loginSuccess',
        'gotoOnFail': 'https://my.yota.ru:443/selfcare/loginError',
        'org': 'customer',
        'old-token': '',
        'IDToken2': '',
        'IDToken1': ''
    }

    payloadChangeSpeed = {
        'product': '',
        'offerCode': '',
        #TODO: gather resource id from the html responce
        'resourceId': '88014285',
        'areOffersAvailable': 'false',
        'status': 'custom',
        'autoprolong': '1',
        'isSlot': 'false',
        'currentDevice': '1',
        'username': '',
        'isDisablingAutoprolong': 'false'
    }

    def __init__(self, creds):
        creds.fill_payload(self.payloadAuth)

    @catch_exception
    def change_limit(self, product):
        offer_code = product.code
        with requests.session() as session:
            session.post('https://login.yota.ru/UI/Login', data=self.payloadAuth, headers={'Content-Language': 'en-RU'})
            r = session.get('https://my.yota.ru/selfcare/devices')
            content = str(r.content)
            if not content:
                raise YotaError("No content received from the web UI")

            product = self._get_product(content)
            self.payloadChangeSpeed["product"] = product
            self.payloadChangeSpeed["offerCode"] = offer_code
            session.post('https://my.yota.ru/selfcare/devices/changeOffer', data=self.payloadChangeSpeed)

    @staticmethod
    def _get_product(content):
        match = re.findall(r'(?<=var sliderData = \{\").*?(?=\":)', content)
        for matchedtext in match:
            return matchedtext
        raise YotaError("Cannot obtain the product")

    @catch_exception
    def parse_selected_product(self):
        product = None
        with requests.session() as session:
            session.post('https://login.yota.ru/UI/Login', data=self.payloadAuth, headers={'Content-Language': 'en-RU'})
            r = session.get('https://my.yota.ru/selfcare/devices')
            content = str(r.content)
            costs = re.findall(r'(?<=<div class=\"cost\"><strong>)\d\d\d(?=</strong>)', content)
            if not costs:
                raise Exception("Unable to login or parse current product. \n Please, check the credentials")

            cost = list(costs)[0]
            for rule, prod in rules.ranges.items():
                if prod.cost == cost:
                    product = prod
                    break
        return product
