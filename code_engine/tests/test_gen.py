
from nose import with_setup
from assertpy import assert_that, contents_of
import os
from code_engine.code_engine_core import gen
from code_engine.util.env import put_folder, put_file, remove
from code_engine.util.debug import on


root = "./.test"

def setup_test_gen():
    put_file("test.template", put_folder(root), '''I am {{ name }}
''')

def clear():
    remove(root)

@with_setup(setup_test_gen, clear)
def test_gen():
    templatepath = os.path.join(root, "test.template")
    outputpath = os.path.join(root, "test.file1")
    data = {"name": "alan"}
    content = contents_of(gen(templatepath, data, outputpath))

    assert_that(content).contains("I am alan")
