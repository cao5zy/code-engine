from .util.filehelper import collect_files
from .code_engine_file import get_value
from .code_engine_file import push_values
from .code_engine_core import gen

def publish(folderpath, subscribe_name, data, output_path = None):

    def generate(definition_file_path):
        gen(get_value(definition_file_path, "template_path"), \
            get_value(definition_file_path, "variables"), \
            get_value(definition_file_path, "output_path") \
            )
        
    def handle(definition_files):
        list([generate(push_values(file, data)) for file in definition_files if get_value(file, "subscribe_name") == subscribe_name])

    handle(collect_files(folderpath, "ce"))

    
