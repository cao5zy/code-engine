import os
from util.debug import debug
import demjson

def get_subscribe_name(filepath):
    return (lambda json: {"subscribe_name": json["subscribe_name"]}) \
        (demjson.decode_file(filepath))

def push_values(filepath, data):
    def updatedict(original, data):
        original.update(data)
        return original
    
    demjson.encode_to_file(filepath + ".staging", debug(updatedict(demjson.decode_file(filepath), {"variables": data})))
