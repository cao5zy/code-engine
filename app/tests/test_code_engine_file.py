from nose import with_setup
from assertpy import assert_that
import os
from code_engine_file import get_value
from util.env import put_folder, put_file, remove
from util.debug import on


root = "./.test"

def setup_test_get_value():
    put_file("file2.ce", put_folder(root), '''
{
  "subscribe_name": "abc"
}
''')


def clear():
    remove(root)

@with_setup(setup_test_get_value, clear)
def test_get_value():
    assert_that(get_value(os.path.join(root, "file2.ce"), "subscribe_name")) \
        .is_equal_to("abc")


def setup_test_push_values():
    put_file("test_push.ce", put_folder(root), '''
{
    "subscribe_name": "xyc"
}
''')

@with_setup(setup_test_push_values, clear)
def test_push_values():
    from code_engine_file import push_values
    import demjson
    
    data = {
        "name": "test",
        "value": 123
    }
    
    assert_that(demjson.decode_file(push_values(os.path.join(root, "test_push.ce"), data))["variables"]).is_equal_to(data)
    

