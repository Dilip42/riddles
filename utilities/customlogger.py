import inspect
import logging
import time
import os
path = os.getcwd()


class custologger:
    @staticmethod
    def cuslog(logLevel=logging.DEBUG):
        logger_name= inspect.stack()[1][3]

        logger=logging.getLogger(logger_name)

        logger.setLevel(logLevel)
        ch = logging.StreamHandler()
        #unique_filename = str(uuid.uuid4())
        withtime = time.strftime("%d_%m_%Y_%H-%MM-%SS")

        fh = logging.FileHandler(f"{path}\\log\\"+"FST"+withtime+".log")
        #current_date_and_time = datetime.datetime.now()
        #current_date_and_time_string = str(current_date_and_time)
        #fh= logging.FileHandler(f"E:\\pomventas\\pomprograms\\logfiles\\automationLog4 .log")
        formattter=logging.Formatter('%(asctime)s  -: %(levelname)s:  -%(message)s' , datefmt= '%d-%m-%Y %H:%M:%S %p')
        fh.setFormatter(formattter)
        ch.setFormatter(formattter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger