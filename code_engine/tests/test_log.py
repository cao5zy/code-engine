from code_engine.util.debug import log
from nose import with_setup
from assertpy import assert_that
from codegenhelper import test_root, init_test_folder, remove_test_folder
import logging

logging.basicConfig(level=logging.DEBUG)

def test_std_log():
    log(__name__)("test").debug("hello")


