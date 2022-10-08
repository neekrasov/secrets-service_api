import logging
from .settings import Settings

def init_logginng(name: str, settings: Settings):
    logger = logging.getLogger(name)
    logger.setLevel(settings.logging_level)
    
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter('%(asctime)s : %(name)s: %(lineno)s : [%(levelname)s] -- %(message)s'))
    sh.setLevel(logging.DEBUG)
    
    logger.addHandler(sh)
    

    