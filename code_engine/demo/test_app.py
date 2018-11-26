from nose import with_setup
from codegenhelper import put_folder, remove, put_file, compose_dir, test_root, init_test_folder, remove_test_folder
from assertpy import assert_that, contents_of
import os
from code_engine import app
import logging

logging.basicConfig(level = logging.DEBUG)

outputpath = os.path.join(test_root(), "folder1")
template_path = os.path.join(test_root(), "folder2")

def setup_test_app():

    put_file("my.py.t", put_folder(template_path), '''
def {{name}}(){}
''')

@with_setup(setup_test_app, remove_test_folder)    
def test_app():
    data = {
        "name": "main",
        "age": 38
        }
    app.publish(template_path, data, outputpath)

    content = contents_of(os.path.join(outputpath, "my.py"))

    assert_that(content).contains("def main(){}")
