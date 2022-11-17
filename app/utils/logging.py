import logging


def setup_logging(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setFormatter(
        logging.Formatter(
            "%(asctime)s : %(name)s: %(lineno)s : [%(levelname)s] -- %(message)s"
        )
    )
    sh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
