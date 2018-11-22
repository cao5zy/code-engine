from code_engine.util.debug import log
from nose import with_setup
from assertpy import assert_that
from codegenhelper import test_root, init_test_folder, remove_test_folder

@with_setup(init_test_folder, remove_test_folder)
def test_log():
    pass

