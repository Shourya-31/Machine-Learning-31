from logger import logging

def add(a,b):

    logging.debug("Addition is taking place")
    return a+b

logging.debug("Addition is called")
add(10,21)
 