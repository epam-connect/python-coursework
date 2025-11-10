import logging

logging.basicConfig(
    level= logging.DEBUG
)

logger = logging.getLogger("mylogger") #convention __name__

handler = logging.FileHandler('test_log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("info")