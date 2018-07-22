from nose import with_setup
from assertpy import assert_that
import os
from code_engine.util.filehelper import collect_files
from codegenhelper import put_folder, put_file


root = "./.test"

def setup_test_collect_file():
    put_file("file2.ce", put_folder("folder1", put_folder(root)), "")
    put_file("file2.xs", put_folder("folder2", put_folder(root)), "")
    put_file("file1.ce", put_folder(root), "")
    put_file("file2.xd", put_folder(root), "")

def clear():
    pass

@with_setup(setup_test_collect_file, clear)
def test_collect_file():
    complete_path = os.path.abspath(root)
    assert_that(collect_files(root, "ce")) \
        .contains(complete_path + "/file1.ce", complete_path + "/folder1/file2.ce") \
        .does_not_contain(complete_path + "/file2.xd", complete_path + "/folder2/file2.xs")
