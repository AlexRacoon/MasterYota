import requests
import re

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
    'offerCode': 'POS-MA6-0002',
    'resourceId': '88014285',
    'areOffersAvailable': 'false',
    'status': 'custom',
    'autoprolong': '1',
    'isSlot': 'false',
    'currentDevice': '1',
    'username': '',
    'isDisablingAutoprolong': 'false'
}


def get_product(content):
    match = re.findall(r'(?<=var sliderData = \{\").*?(?=\":)', content)
    for matches in match:
        return matches

with requests.Session() as c:
    c.post('https://login.yota.ru/UI/Login', data=payloadAuth, headers={'Content-Language': 'en-RU'})
    r = c.get('https://my.yota.ru/selfcare/devices')
    content = str(r.content)
    productId = get_product(content)
    payloadChangeSpeed["product"] = productId
    c.post('https://my.yota.ru/selfcare/devices/changeOffer', data=payloadChangeSpeed)
    r2 = c.get('https://my.yota.ru/selfcare/devices')
    content = r2.content