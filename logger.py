import logging

"""
    using logging we are able to save a log file to a location that we chose, by the given level that we chose, we can control if the logfile is overwritten or not and we control the format when using the simple basicConfig method from the logging module
"""

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "g:\\logfile.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w' )

logger = logging.getLogger()

def string_validation(word):
    #return a boolean for each string validation
    #check constraints
    logger.info("The word we are checking is") , word
    if(0 < len(word) < 1000):
        """
            the any built in will return a boolean for any iterable
        """
        logger.debug("check if it contains alphanumeric")
        print any(c.isalpha() for c in word)
        logger.debug("check if it contains digits")
        print any(c.isdigit() for c in word)
        logger.debug("check if it contains numbers")
        print any(c.isalnum() for c in word)
        logger.debug("check if it contains lowercase")
        print any(c.islower() for c in word)
        logger.debug("check if it contains uppercase")
        print any(c.isupper() for c in word)


string_validation("123dwimn")
