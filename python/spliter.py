import os
import shutil
import time
import config
import logging


def split_files(path="", number=4):
    with open(path, 'rb') as fp:
        path += "_new"
        if os.path.exists(path):
            shutil.rmtree(path)

        os.mkdir(path)

        while buf := bytearray(fp.read(number * config.BUFFER_SIZE)):
            buf2 = [bytearray() for _ in range(number)]
            # threads = []

            # 分离读取字节流
            t1 = time.time()
            # for i in range(number):
            #     th = threading.Thread(target=f, args=(buf, buf2, number, i))
            #     th.start()
            #     threads.append(th)
            n = 0
            while n < len(buf):
                try:
                    for i in range(number):
                        buf2[i] += buf[n:n+config.SLICE_SIZE]
                        n += config.SLICE_SIZE
                except Exception as e:
                    logging.error(e)
                    break

            # [thread.join() for thread in threads]
            logging.debug("split.append process time: %.2f s" % (time.time() - t1))

            t1 = time.time()
            for i in range(number):
                split_files_save(path, buf2[i], i)
            logging.debug("split.save process time: %.2f s" % (time.time() - t1))


def f(buf, buf2, number, i):
    tmp = bytearray(buf)
    buf2[i] = bytearray()
    index = i
    while True:
        try:
            buf2[i].append(tmp[index])
            index += number
        except:
            break


def split_files_save(path, buf, index):
    with open(path + "/" + str(index), 'ab+') as fp:
        fp.write(bytes(buf))
