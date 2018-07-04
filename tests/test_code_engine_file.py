from nose import with_setup
from assertpy import assert_that
import os
from code_engine_file import collect_files
root = "./.test"

def setup_test_collect_file():
    pass

def clear():
    pass

@with_setup(setup_test_collect_file, clear)
def test_collect_file():
    complete_path = os.path.abspath(root)
    assert_that(collect_files(root, "ce")) \
        .contains(complete_path + "/file1.ce", complete_path + "/folder1/file2.ce") \
        .does_not_contain(complete_path + "/file2.xd", complete_path + "/folder2/file2.xs")
