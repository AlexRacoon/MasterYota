import requests
import re


class reqman(object):
    """sends requests to change the speed"""

    payloadAuth = {
        'goto': 'https://my.yota.ru:443/selfcare/loginSuccess',
        'gotoOnFail': 'https://my.yota.ru:443/selfcare/loginError',
        'org': 'customer',
        'old-token': 'alexbecoon@gmail.com',
        'IDToken2': 'xtoxphcxlx',
        'IDToken1': '6034675940'
    }

    payloadChangeSpeed = {
        'product': '',
        'offerCode': '',
        'resourceId': '88014285',
        'areOffersAvailable': 'false',
        'status': 'custom',
        'autoprolong': '1',
        'isSlot': 'false',
        'currentDevice': '1',
        'username': '',
        'isDisablingAutoprolong': 'false'
    }

    def __init__(self, user, passw, account, beVerbose = True):
        self.beVerbose = beVerbose
        self.user = user
        self.passw = passw
        self.account = account

    def change_limit(self, offerCode):
        self.payloadAuth["old-token"] = self.user
        self.payloadAuth["IDToken2"] = self.passw
        self.payloadAuth["IDToken1"] = self.account

        with requests.session() as session:
            session.post('https://login.yota.ru/UI/Login', data=self.payloadAuth, headers={'Content-Language': 'en-RU'})
            r = session.get('https://my.yota.ru/selfcare/devices')
            content = str(r.content)
            product = self.get_product(content)
            if self.beVerbose:
                print("Trying to send the request")
            self.payloadChangeSpeed["product"] = product
            self.payloadChangeSpeed["offerCode"] = offerCode

            session.post('https://my.yota.ru/selfcare/devices/changeOffer', data=self.payloadChangeSpeed)

    def get_product(self, content):
        match = re.findall(r'(?<=var sliderData = \{\").*?(?=\":)', content)
        for matchedtext in match:
            print(matchedtext)
            return matchedtext