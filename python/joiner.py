import time
import config
import logging


def join_files(path=""):
    fps = []
    i = 0
    while True:
        try:
            fps.append(open(path + str(i), 'rb'))
            i += 1
        except:
            break

    with open("d:\\2.mp4", 'wb') as dst:
        while True:
            buf2 = []
            buf = bytearray()

            t1 = time.time()
            # 读取分片文件
            for fp in fps:
                buf2.append(bytearray(fp.read(config.BUFFER_SIZE)))
            logging.debug("join.read process time: %.2f s" % (time.time() - t1))

            # 读取完成
            count = sum(len(e) for e in buf2)
            if count == 0:
                break

            # 写入
            t1 = time.time()
            n = 0
            while n < config.BUFFER_SIZE:
                try:
                    for i in range(len(buf2)):
                        buf += buf2[i][n:n+config.SLICE_SIZE]
                    n += config.SLICE_SIZE
                except Exception as e:
                    logging.error(e)
                    break
            logging.debug("join.append process time: %.2f s" % (time.time() - t1))

            dst.write(buf)

    [fp.close() for fp in fps]
