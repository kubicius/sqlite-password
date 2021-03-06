import logging
import config as cfg
import command
import database
import test.test_validation as tv

if __name__ == '__main__':
    logging.basicConfig(filename=cfg.log["output"], level=logging.DEBUG, format=cfg.log["format"])
    db = database.Database()
    if(db.connect(file=cfg.db["file"])):
        cl = command.Command(db)
        cl.run()
    else:
        print(f"Database error occurred. Check {cfg.log['output']} file.")

