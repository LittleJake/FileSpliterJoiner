import time
import logging
import joiner
import spliter
import utils

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s - %(filename)s(%(lineno)s): %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

if __name__ == '__main__':
    t1 = time.time()
    spliter.split_files("D:\\Desktop\\output_merged.mp4", 10)
    logging.debug("*split process time: %.2f s" % (time.time() - t1))

    utils.generate_digest("D:\\Desktop\\output_merged.mp4_new\\")

    t1 = time.time()
    joiner.join_files("D:\\Desktop\\output_merged.mp4_new\\")
    logging.debug("*join process time: %.2f s" % (time.time() - t1))
