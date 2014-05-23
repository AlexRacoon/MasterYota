class authenticator(object):
    """authenticates at yota profile"""
    def __init__(self, user, passw, beVerbose = True):
        self.user = user
        self.passw = passw
        self.beVerbose = beVerbose

    def authenticate(self):
#It's a stub for now
        success = False
        if self.beVerbose:
            print("Trying to authenticate")
            success = True
        return success
        