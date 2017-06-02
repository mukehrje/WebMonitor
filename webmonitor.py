# 
# AUTHOR:  SUMAN KUMAR MUKHERJEE <sumanmukherjee1981@gmail.com> 
#
# MANAGES WEB OPERATIONS
# ----------------------------------------------------------------------------

# STANDARD LIBRARIES
import os, datetime, time

# USERDEFINED LIBRARIES
from lib.webutils import WebUtils
from lib.logger import Logger
from config import URLS, MONITOR, THRESHOLD

# Read Log Config
curr_dir=os.path.dirname(os.path.abspath(__file__))


def sleep(seconds):
    """
        sleep for desired seconds
    """
    time.sleep(seconds)


def monitor_websites(web, log):
    """
        Monitor websites
    """
    log.report('debug', '-'*79)
    log.report('debug', '\t\t\t\tWEB MONITORING INFO')
    log.report('debug', '-'*79)    
    for index, info in enumerate(URLS):
        url = info[0]
        txt = info[1]
        log.report('debug', '['+str(index+1)+']. Website: '+url+' | '+\
                   str('Search String: '+txt))
        start =  datetime.datetime.now()
        log.report('debug','Trying to access url '+url)
        status, msg = web.is_accessible(url)
        if status:
            http_code = msg[0]
            html_src  = msg[1]
            log.report('info', 'HTML STATUS: '+str(http_code))
            log.report('info', 'Website - '+url+' - is accessible')
            if web.is_text(html_src, txt):
                log.report('info', 'Search string - '+txt+' - '+\
                           str('found in url - '+url))
            else:
                log.report('error', 'Search string - '+txt+' - '+\
                           str('not found in url - '+url))
        else:
            log.report('error', 'Website - '+url+' - is not accessible. '+\
                       str('Please check...'))  
            log.report('error', msg)  
        end = datetime.datetime.now()
        diff = end - start
        log.report('debug', 'Time taken in microseconds - '+\
                   str(int(round(diff.microseconds / 1000))))
        log.report('debug', '-'*79)

if __name__ == "__main__":
    # Instantiate webutils and logger object
    web = WebUtils()
    log = Logger()

    start_monitor =  datetime.datetime.now()
    start_threshold =  datetime.datetime.now()
    counter=0
    while True:
        counter += 1
        log.report('info', 'MONITOR CYCLE: '+str(counter))
        monitor_websites(web, log)
        end_monitor =  datetime.datetime.now()
        monitor_elapsed = end_monitor - start_monitor
        monitor_threshold = end_monitor - start_threshold
        if (monitor_threshold.seconds >= THRESHOLD):
            break        
        if (monitor_elapsed.seconds < MONITOR):
            sleep(MONITOR - monitor_elapsed.seconds)
        start_monitor =  datetime.datetime.now()
            
