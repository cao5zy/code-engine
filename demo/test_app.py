from nose import with_setup
from util.env import put_folder, remove, put_file, compose_dir
from assertpy import assert_that, contents_of
import os
import app

root = "./test"
outputpath = "./test/folder1/code.py"

def setup_test_app():
    put_file("code1.ce", put_folder(root), '''
{
    "subscribe_name": "test",
    "template_path": "./test/my.template",
    "output_path": "./test/folder1/code.py"
} ''')

    put_file("my.template", put_folder(root), '''
def {{name}}(){}
''')

    put_folder("folder1", put_folder(root))

def clear():
    remove(root)

@with_setup(setup_test_app, clear)    
def test_app():
    folderpath = root
    subscribe_name = "test"
    data = {
        "name": "main",
        "age": 38
        }
    app.publish(folderpath, subscribe_name, data)

    content = contents_of(outputpath)

    assert_that(content).contains("def main(){}")
