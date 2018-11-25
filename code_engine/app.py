from .util.filehelper import collect_files
from .util.debug import log
from codegenhelper import debug
import os
from codegenhelper import create_folder_if_not_exists
from jinja2 import Template

def publish(template_root_path, data, target_root_path = os.getcwd()):
    log(__name__)("target_path").debug(target_path)

    def get_target_file_path(template_relative_path):
        return (lambda s:s[0:len(s)-2])(os.path.join(target_root_path, template_relative_path))
    
    def generate(template_file_path):
        def gen(template_relative_path):
            with open(create_folder_if_not_exists(get_target_file_path(template_relative_path)), 'w') as file:
                file.write( \
                Template(open(template_file_path, 'r').read()).render(data) \
                )
            return output_root_path
    
            
        gen(get_relative_path(template_root_path, template_file_path))
        
    def handle(template_files):
        list([generate(file) for file in template_files])

    handle(collect_files(template_root_path, "t"))

    
