import logging
class log:
    def intializeLogger(self):
        fileName = self + ".log"
        logging.basicConfig(filename=fileName, level=logging.DEBUG, format='%(asctime)s %(message)s')
        pass
