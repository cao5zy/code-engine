import os
import shutil

def compose_dir(parent, name):
    return os.path.join(parent or os.getcwd(), name)

def remove(dir):
    shutil.rmtree(dir)

def put_folder(name, parent = None):
    def create(dir):
        os.makedirs(dir)
        return dir
    return create(compose_dir(parent, name)) \
        if not os.path.exists(compose_dir(parent, name)) \
                       else compose_dir(parent, name)

def put_file(name, parent = None, content = None):
    with open(compose_dir(parent, name), 'w') as file:
                       file.write(content)
