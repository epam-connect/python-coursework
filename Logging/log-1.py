import logging

logging.basicConfig(
    # level=logging.WARNING, 
    # filename="log.log", 
    # filemode="a",
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     # logging.error("ZeroDivisionError", exc_info=True)
#     logging.exception("ZeroDivisionError")

# logging.info("Hello")
 