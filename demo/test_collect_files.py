from nose import with_setup
from util.env import put_folder, remove, put_file

root = "./.test_files"

def setup_collect_files_with_ext():
    put_file("cf.ce", put_folder("folder1", put_folder(root)), "")


def clear_env():
    remove(root)

@with_setup(setup_collect_files_with_ext, clear_env)
def test_collect_files_with_ext():
    pass
