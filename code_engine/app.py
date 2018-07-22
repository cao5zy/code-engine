from .util.filehelper import collect_files
from codegenhelper import debug
from .code_engine_file import push_values, get_value, get_template_path, get_output_path
from .code_engine_core import gen
import os

def publish(folderpath, subscribe_name, data, target_path = os.getcwd()):
    debug(target_path, 'input target_path')
    def generate(definition_file_path):
        gen(get_template_path(os.path.split(definition_file_path)[0], get_value(definition_file_path, "template_path")), \
            get_value(definition_file_path, "variables"), \
            debug(get_output_path(target_path, get_value(definition_file_path, "output_path")), 'output target path') \
            )
        
    def handle(definition_files):
        list([generate(push_values(file, data)) for file in definition_files if get_value(file, "subscribe_name") == subscribe_name])

    handle(collect_files(folderpath, "ce"))

    
