import logging
import os
import sys
from optparse import OptionParser

def log(moduleName):
    def title(title = None):
        class GetLogger:
            def __init__(self):

                def has_config_file():
                    return os.path.exists("logger.conf")

                def get_std_logger():
                    return logging.getLogger(moduleName + "--%s" % title if title else "")

                def get_configured_logger():
                    pass
                
                self.logger = get_configured_logger() if has_config_file() else get_std_logger()                
            def debug(self, val):
                self.logger.debug(val)
                return val

            def info(self, val):
                self.logger.info(val)
                return val

            def error(self, val):
                self.logger.error(val)
                return val

        return GetLogger()

    return title
