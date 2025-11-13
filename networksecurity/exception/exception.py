import sys


class NetworkSecuirtyException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))