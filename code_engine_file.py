import os
from util.debug import debug
import demjson

def get_subscribe_name(filepath):
    return (lambda json: {"subscribe_name": json["subscribe_name"]}) \
        (demjson.decode_file(filepath))

