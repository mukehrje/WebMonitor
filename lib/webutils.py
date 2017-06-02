# 
# AUTHOR:  SUMAN KUMAR MUKHERJEE <sumanmukherjee1981@gmail.com>
#
# MANAGES WEB OPERATIONS
# ----------------------------------------------------------------------------

# STANDARD LIBRARIES
import urllib2, re


class WebUtils(object):
    """
        Class WebUtils to manage web operations
    """

    def __init__(self):
        """
            Init method
        """
        pass


    def is_text(self, html, txt):
        """
            Returns True if text found in html source, False otherwise
        """
        if re.search(txt, html, re.IGNORECASE):
            return True
        return False

        
    def is_accessible(self, url):
        """
            Returns True with HTTP status code and HTML source if specified url is accessible,
            otherwise returns False with appropriate error message
        """
        try:
            req  = urllib2.Request(url)
            resp = urllib2.urlopen(req)
            html = resp.read()
        except urllib2.URLError as err:
            return False, err.reason
        return True, (resp.getcode(), html)
        



