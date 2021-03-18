import logging
import config as cfg
import console
import database

if __name__ == '__main__':
    logging.basicConfig(filename=cfg.log["output"], level=logging.DEBUG, format=cfg.log["format"])
    db = database.Database(logging)
    db.connect(file=cfg.db["file"])
