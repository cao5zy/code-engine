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
                return self.logger.debug(val)

            def info(self, val):
                return self.logger.info(val)

            def error(self, val):
                return self.logger.error(val)

        return GetLogger()

    return title
