from jinja2 import Template
from codegenhelper import create_folder_if_not_exists

def gen(templatepath, data, outputpath):
    with open(create_folder_if_not_exists(outputpath), 'w') as file:
        file.write( \
            Template(open(templatepath, 'r').read()).render(data) \
        )
    return outputpath
        
