import pytest
from authenticator import *

def testAuthenticator():
    auth = Authenticator()
    result = auth.authenticate("Jóska","Almafa")
    assert result == True




