import requests


class AuthMan(object):
    """authenticates at yota profile"""

#hard-coded yet
    payload = {
        'goto': 'https://my.yota.ru:443/selfcare/loginSuccess',
        'gotoOnFail': 'https://my.yota.ru:443/selfcare/loginError',
        'org': 'customer',
        'old-token': 'alexbecoon@gmail.com',
        'IDToken2': 'xtoxphcxlx',
        'IDToken1': '6034675940'
    }

    def __init__(self, user, passw, beVerbose = True):
        self.beVerbose = beVerbose

    def authenticate(self):
        success = False
        if self.beVerbose:
            print("Trying to authenticate")
        
        if self.isAuth():
            if self.beVerbose:
                print("Already authenticated")
            return True

        success = self._doauthentication(self.user, self.passw)

        if self.beVerbose:
            print("Success :)") if success else print("Fail :(") 
        return success
    
    def isAuth(self):
        return True

    def _doauthentication(self, user, passw):
        with requests.Session() as c:
            c.post('https://login.yota.ru/UI/Login', data=self.payload)
            r = c.get('https://my.yota.ru/selfcare/devices')
            print(r.content)

