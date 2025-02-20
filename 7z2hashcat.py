#!/usr/bin/env python3

import sys
import struct

def extract_hash(zip_filename):
    with open(zip_filename, "rb") as f:
        data = f.read()
    if data[:2] != b'PK':
        print("Not a valid ZIP file")
        return None
    hash_format = "$zip2$"
    crc = struct.unpack("<I", data[14:18])[0]
    compressed_size = struct.unpack("<I", data[18:22])[0]
    uncompressed_size = struct.unpack("<I", data[22:26])[0]
    hash_string = f"{hash_format}${crc}${compressed_size}${uncompressed_size}"
    return hash_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 7z2hashcat.py <zip_file>")
        sys.exit(1)
    
    zip_file = sys.argv[1]
    hash_result = extract_hash(zip_file)
    if hash_result:
        print(hash_result)

