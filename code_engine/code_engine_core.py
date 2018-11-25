from jinja2 import Template
from codegenhelper import create_folder_if_not_exists

def gen(template_relative_path, data, output_root_path):
    with open(create_folder_if_not_exists(output_root_path), 'w') as file:
        file.write( \
            Template(open(template_relative_path, 'r').read()).render(data) \
        )
    return output_root_path
        
