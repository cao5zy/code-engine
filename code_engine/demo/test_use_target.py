from nose import with_setup
from code_engine.util.env import put_folder, remove, put_file, compose_dir
from assertpy import assert_that, contents_of
from code_engine import publish
import os

root = "./test"
output_folder = os.path.join(root, "output_code")
template_folder = os.path.join(root, "template")

def setup_test_use_target():
    put_file("code.ce", put_folder("template", put_folder(root)), '''
{
    "subscribe_name": "test",
    "template_path": "./code.template",
    "output_path": "$target/code.js"
}
''')
    put_file("code.template", put_folder("template", put_folder(root)), """
def {{ name }}(){}
""")

def clear():
    remove(root)

@with_setup(setup_test_use_target, clear)
def test_use_target():
    subscribe_name = "test"
    data = { "name": "main" }
    output_path = os.path.join(output_folder, "code.js")
    publish(template_folder, subscribe_name, data, output_folder)

    content = contents_of(output_path)

    assert_that(content).contains("def main(){}")
    
