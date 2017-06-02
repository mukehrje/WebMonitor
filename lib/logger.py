# 
# AUTHOR:  SUMAN KUMAR MUKHERJEE <sumanmukherjee1981@gmail.com> 
#
# APPLICATION LOGGER
# ----------------------------------------------------------------------------

# STANDARD LIBRARIES
import os, time
import logging
import logging.config

# read log config
lib_dir=os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(os.path.join(lib_dir, 'logging.conf'))
logs_dir=os.path.abspath(os.path.join(lib_dir, os.pardir, 'logs'))

# create logger
logger = logging.getLogger('webmonitor')

# create file handler which logs even debug messages
timestamp = int(time.time())
LOG_FILENAME=os.path.join(logs_dir, 'debug_'+str(timestamp)+'.log')
fh = logging.FileHandler(LOG_FILENAME)
fh.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)


class Logger(object):
    """
        Logger for Troubleshooting
    """
    
    def report(self, mode, msg):
        """
            log messages
        """
        if mode == 'debug':
            logger.debug(msg)
        if mode == 'info':
            logger.debug(msg)
        if mode == 'warn':
            logger.warn(msg)
        if mode == 'error':
            logger.error(msg)
        if mode == 'critical':
            logger.critical(msg)
            

