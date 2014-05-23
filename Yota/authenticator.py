import random
#See http://wwwsearch.sourceforge.net/mechanize/
class authman(object):
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
        
        if self.isAuth():
            if self.beVerbose:
                print("Already authenticated");
            return True;

        success = bool(random.getrandbits(1))

        if self.beVerbose:
            print("Success :)") if success else print("Fail :(") 
        return success
    
    def isAuth(self):
        return bool(random.getrandbits(1)) 