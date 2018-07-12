from jinja2 import Template

def gen(templatepath, data, outputpath):
    with open(outputpath, 'w') as file:
        file.write( \
            Template(open(templatepath, 'r').read()).render(data) \
        )
    return outputpath
        
