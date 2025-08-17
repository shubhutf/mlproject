import sys
import logging

def error_message_detail(error, error_detail: sys):
    # current exception ka traceback nikaalo
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "<unknown>"
    line_number = exc_tb.tb_lineno if exc_tb else -1
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):   # <-- yaha 'error' (Exception object) lo
        super().__init__(str(error))                # <-- base Exception ko string do
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


