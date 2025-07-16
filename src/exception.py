import sys
import os
from src.logger import logging
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_detail)

    def error_message_detail(self, error, error_detail):
        exc_type, exc_obj, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename 
        error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}]: {error}"
        return error_message

    def __str__(self):  
        return self.error_message
