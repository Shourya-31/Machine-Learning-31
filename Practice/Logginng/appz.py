import logging

# logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app11.log", mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def substract(a, b):
    result = a - b
    logger.debug(f"Substract {a}-{b}={result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a}x{b}={result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(1, 8)
substract(12, 4)
multiply(3, 5)
divide(4, 2)
