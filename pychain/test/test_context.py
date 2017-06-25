import nose
from nose.tools import *

import sys
from StringIO import StringIO
from pychain import RedirectStdout

class test_context ():
  def setUp (self):
    pass

  def tearDown (self):
    pass

  def test_context_stdout_write (self):
    test_string = "test_context"
    out = StringIO ()
    with RedirectStdout (out):
      sys.stdout.write (test_string)
    assert_equals (out.getvalue (), test_string)

  def test_context_stdout_print (self):
    test_string = "test_context"
    out = StringIO ()
    with RedirectStdout (out):
      print (test_string)
    assert_equals (out.getvalue(), test_string + "\n")
