from .util.filehelper import collect_files
from .util.debug import log
from codegenhelper import debug
import os
from codegenhelper import create_folder_if_not_exists
from jinja2 import Template

def publish(template_root_path, data, target_root_path = os.getcwd()):
    def get_target_file_path(template_relative_path):
        return log(__name__)("target_file_path").debug(
            (lambda s:s[0:len(s)-2])(
                os.path.join(target_root_path, template_relative_path)
            )
        )

    def get_relative_path(template_file_path):
        return log(__name__)("relative_path").debug((lambda root_path, file_path: file_path[len(root_path) + 1: len(file_path)])(os.path.abspath(template_root_path), os.path.abspath(template_file_path)))
        
    def generate(template_file_path):
        def gen(template_relative_path):
            with open(create_folder_if_not_exists(get_target_file_path(template_relative_path)), 'w') as file:
                file.write( \
                Template(open(template_file_path, 'r').read()).render(data) \
                )

    
            
        gen(get_relative_path(template_file_path))
        
    def handle(template_files):
        list([generate(file) for file in template_files])

    handle(collect_files(template_root_path, "t"))

    
