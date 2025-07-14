import sys
from src.logger import logging

def error_message_detail(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occurred in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):  
        return self.error_message
    
if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("divide by zero")
        raise Exception(e)