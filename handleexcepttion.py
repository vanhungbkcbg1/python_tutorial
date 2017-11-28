import traceback
import logging
def doSomething():
    try:
        print('hello')
        x=10/0

    except Exception as err:
        logger=logging.getLogger(__name__)
        logger.exception(err)
