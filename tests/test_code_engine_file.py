from nose import with_setup
from assertpy import assert_that
import os
from code_engine_file import get_subscribe_name
from util.env import put_folder, put_file, remove
from util.debug import on


root = "./.test"

def setup_test_collect_file():
    put_file("file2.ce", put_folder(root), '''
{
  "subscribe_name": "abc"
}
''')


def clear():
    remove(root)

@with_setup(setup_test_collect_file, clear)
def test_get_subscribe_name():
    assert_that(get_subscribe_name(os.path.join(root, "file2.ce"))) \
        .contains_entry({"subscribe_name": "abc"})
    

