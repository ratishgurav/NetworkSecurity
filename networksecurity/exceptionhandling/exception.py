import sys
from networksecurity.logging import logger



class NetworkException(Exception):
    def __init__(self, message, error_details=sys):
        self.message = message
        _,_,exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno 
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error in file: {}, line: {}, message: {}".format(self.file_name, self.line_number, self.message)

if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log message")
        a=1/0
        print(a)
    except Exception as e:
        logger.logging.error("An error occurred: {}".format(e))
        raise NetworkException("An error occurred in the network security module", sys)