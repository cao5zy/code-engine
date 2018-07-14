import os
from .util.debug import debug
import demjson

def get_value(filepath, key):
    return (lambda json: json[key]) \
        (demjson.decode_file(filepath))

def push_values(filepath, data):
    def updatedict(original, data):
        original.update(data)
        return original

    def push(outputpath):
        demjson.encode_to_file(outputpath, debug(updatedict(demjson.decode_file(filepath), {"variables": data})))

        return outputpath

    return push(filepath + ".staging")
