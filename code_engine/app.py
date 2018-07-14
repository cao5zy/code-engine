from .util.filehelper import collect_files
from .code_engine_file import get_value
from .code_engine_file import push_values
from .code_engine_core import gen

def publish(folderpath, subscribe_name, data):

    def generate(template_path):
        gen(get_value(template_path, "template_path"), \
            get_value(template_path, "variables"), \
            get_value(template_path, "output_path") \
            )
        
    def handle(files):
        list([generate(push_values(file, data)) for file in files if get_value(file, "subscribe_name") == subscribe_name])

    handle(collect_files(folderpath, "ce"))

    
