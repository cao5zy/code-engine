from nose import with_setup
from code_engine.util.env import put_folder, remove, put_file, compose_dir
from assertpy import assert_that
import os

root = "./.test_files"

def setup_collect_files_with_ext():
    put_file("cf.ce", put_folder("folder1", put_folder(root)), "")


def clear_env():
    remove(root)

@with_setup(setup_collect_files_with_ext, clear_env)
def test_collect_files_with_ext():
    assert_that(os.path.exists(compose_dir(compose_dir(root, "folder1"), "cf.ce"))).is_true()
