# Create a logger object
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler and set level to debug
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Example function with logging
def divide(a, b):
    try:
        result = a / b
        logger.info(f'Divided {a} by {b}, result is {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero error')

# Test the function
divide(10, 2)
divide(10, 0)
