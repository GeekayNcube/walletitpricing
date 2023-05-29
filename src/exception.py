import sys


def error_mesage(message, error_detail:sys):
    _,_,exp = error_detail.exc_info()
    error_mesage = "error occured in python script [{0}]: Line number [{1}] error message [{2}]".format(exp.tb_frame.f_code.co_filename, exp.lineno, message)
    return error_mesage

class CustomException(Exception):
    def __init__(self, message, error_detail:sys):
        super.__init__(message)
        self.error_message = error_mesage(message, error_detail)

    def __str__(self):
        return self.error_message
    



