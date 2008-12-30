#!/usr/bin/env python

__author__ = "Abhinav Sarkar <abhinav@abhinavsarkar.net>"
__version__ = "0.2"
__license__ = "GNU Lesser General Public License"

class BaseError(Exception):
    """Base class for Lastfm errors"""
    def __init__(self,                 
                 message = None,
                 code = None):
        super(BaseError, self).__init__()
        self.__code = code
        self.__message = message

    @property
    def code(self):
        return self.__code

    @property
    def message(self):
        return self.__message
    
    def __str__(self):
        return "%s" % self.message
class Error(BaseError):
    pass

class InvalidServiceError(BaseError):#2
    pass

class InvalidMethodError(BaseError):#3
    pass

class AuthenticationFailedError(BaseError):#4
    pass

class InvalidFormatError(BaseError):#5
    pass

class InvalidParametersError(BaseError):#6
    pass

class InvalidResourceError(BaseError):#7
    pass

class OperationFailedError(BaseError):#8
    pass

class InvalidSessionKeyError(BaseError):#9
    pass

class InvalidApiKeyError(BaseError):#10
    pass

class ServiceOfflineError(BaseError):#11
    pass

class SubscribersOnlyError(BaseError):#12
    pass

class TokenNotAuthorizedError(BaseError):#14
    pass

class TokenExpiredError(BaseError):#15
    pass

errorMap = {
            1: Error,
            2: InvalidServiceError,
            3: InvalidMethodError,
            4: AuthenticationFailedError,
            5: InvalidFormatError,
            6: InvalidParametersError,
            7: InvalidResourceError,
            8: OperationFailedError,
            9: InvalidSessionKeyError,
            10: InvalidApiKeyError,
            11: ServiceOfflineError,
            12: SubscribersOnlyError,
            14: TokenNotAuthorizedError,
            15: TokenExpiredError
           }    