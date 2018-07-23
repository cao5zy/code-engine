import os
from codegenhelper import debug, remove_file_if_exists
import demjson

def get_value(filepath, key):
    return (lambda json: json[key]) \
        (demjson.decode_file(filepath))

def push_values(filepath, data):
    def updatedict(original, data):
        original.update(data)
        return original

    def push(outputpath):
        demjson.encode_to_file(remove_file_if_exists(outputpath), debug(updatedict(demjson.decode_file(filepath), {"variables": data})))

        return outputpath

    return push(filepath + ".staging")

def get_template_path(definition_file_folder, template_path):
    return template_path if os.path.isabs(template_path) else os.path.join(definition_file_folder, template_path)

def get_output_path(target_path, output_path):
    return output_path if os.path.isabs(output_path) \
             else os.path.join(target_path, output_path)
