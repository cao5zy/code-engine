import os
from util.debug import debug
import demjson

def get_value(filepath, key):
    return (lambda json: json[key]) \
        (demjson.decode_file(filepath))

def push_values(filepath, data):
    def updatedict(original, data):
        original.update(data)
        return original
    
    demjson.encode_to_file(filepath + ".staging", debug(updatedict(demjson.decode_file(filepath), {"variables": data})))
