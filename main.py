#! /usr/bin/env python3
# Used to test a file and a hash across multiple hashing algorithms
import hashlib
import argparse
import pathlib


def checker(filename, checksum, buffer_size):
    hashing_algorithms = [
        hashlib.sha1(),
        hashlib.sha224(),
        hashlib.sha256(),
        hashlib.sha384(),
        hashlib.sha512(),
        hashlib.md5()
    ]

    path = pathlib.Path(filename)

    if not path.exists():
        print('File not found!')
        quit(1)

    with open(path, 'rb') as f:  # read file once and apply data to multiple algorithms
        data = f.read(buffer_size)

        while data != b'':
            for algorithm in hashing_algorithms:
                algorithm.update(data)

            data = f.read(buffer_size)

    for algorithm in hashing_algorithms:  # For-else Checks for a match if there are none, complain!
        if algorithm.digest().hex() == checksum:
            print(algorithm.name + ' - MATCH')
            break
    else:
        print("No match found!")
        quit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checks a checksum across multiple hashing algorithms')
    parser.add_argument('filename', help='Name of file')
    parser.add_argument('checksum', help='Checksum')
    parser.add_argument('--buffer_size', help='Buffer size default(4096)', type=int, default=4096)

    args = parser.parse_args()

    checker(args.filename, args.checksum, args.buffer_size)
