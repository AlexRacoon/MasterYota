import requests
import re


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
        creds.fillPayload(self.payloadAuth)

    def change_limit(self, offer_code):
        with requests.session() as session:
            session.post('https://login.yota.ru/UI/Login', data=self.payloadAuth, headers={'Content-Language': 'en-RU'})
            r = session.get('https://my.yota.ru/selfcare/devices')
            content = str(r.content)
            product = self._get_product(content)
            self.payloadChangeSpeed["product"] = product
            self.payloadChangeSpeed["offerCode"] = offer_code
            session.post('https://my.yota.ru/selfcare/devices/changeOffer', data=self.payloadChangeSpeed)

    @staticmethod
    def _get_product(content):
        match = re.findall(r'(?<=var sliderData = \{\").*?(?=\":)', content)
        for matchedtext in match:
            print(matchedtext)
            return matchedtext