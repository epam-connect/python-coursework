import logging
import Employee

# logging.basicConfig(            #Employee basicConfig already done this will not overwrite the configuration
#     filename="math.log",
#     filemode="w",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG
# )

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler("Math.log")

stream_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def div(a, b):
    return a / b


try:
    div(10, 0)

except ZeroDivisionError as e:
    logger.error("ZeroDivision Error", exc_info=True)

logger.debug("This is debug message")