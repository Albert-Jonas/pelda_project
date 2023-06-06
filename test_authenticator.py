import pytest
from authenticator import *

class DatabaseHandlerTest(IDatabaseHandler):
    def get_user_credentials(self, userName):
        return "Almafa"



def testAuthenticator():
    auth = Authenticator()
    result = auth.authenticate("Jóska","Almafa")
    assert result == True


def testAuthenticatorTestable():
    databaseHandler = DatabaseHandlerTest()
    auth = AuthenticatorTestable(databaseHandler)

    result = auth.authenticate("Jóska","Almafa")
    assert result == True