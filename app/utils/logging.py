import logging
from app.utils.context import Context

def setup_logginng(name: str, context: Context):
    logger = logging.getLogger(name)
    logger.setLevel(context.settings.logging_level)
    
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter('%(asctime)s : %(name)s: %(lineno)s : [%(levelname)s] -- %(message)s'))
    sh.setLevel(logging.DEBUG)
    
    logger.addHandler(sh)
    

    