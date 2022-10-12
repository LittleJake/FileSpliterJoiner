import os
import hashlib


def generate_digest(path):
    lines = []
    for file in os.listdir(path):
        lines += file + ":" + sha512_file(path + file) + "\n"

    with open(path + "digest", 'wt') as fp:
        fp.writelines(lines)


def sha512_file(file_path, buffers=1024):
    sha512 = hashlib.sha512()
    with open(file_path, 'rb') as f:
        while data := f.read(buffers):
            sha512.update(data)
    return sha512.hexdigest()
