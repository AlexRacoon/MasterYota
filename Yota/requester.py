from Yota import authenticator

class reqman(object):
    """sends requests to change the speed"""

    def __init__(self, authman, beVerbose = True):
        self.authman = authman
        self.beVerbose = beVerbose

    def changeLimit(self, speed):
        successAuth = False
        if not self.authman.isAuth():
            successAuth = self.authman.authenticate()
        if successAuth:
           if self.beVerbose:
                print("Trying to send the request")
        else:
            print("Unable to authenticate")