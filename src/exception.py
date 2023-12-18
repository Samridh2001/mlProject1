
import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    #first 2 info useless so directly third info is extracted
    #will give the info about in which line exception has occured,file
    _,_,exc_tb=error_detail.exc_info()
    #file name:file in which exception occured
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occcured in python script name [{0}] line number[{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message



#error_detail tracked by sys
#exception is coming from sys
#super is inheriting
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    

    def __str__(self):
        return self.error_message




# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("divide by zero error")
#         raise CustomException(e,sys)