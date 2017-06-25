import nose
from nose.tools import *

from pychain.chainio import BlockReader, BlockParser
from pychain.chain import Chain

class test_BlockReader ():
  def setUp (self):
    self.chain = Chain (Chain.genesis, Chain.default_hash_function)
    self.chain.append ("block 2")
    self.chain.append ("block 3")
    self.chain.append ("block 4")

  def tearDown (self):
    pass

  def test_chain_exists (self):
    assert_equals (len (self.chain), 4)

  def test_chain_read (self):
    reader = BlockReader (self.chain, 2)
    blk = reader.read ()
    assert_true (isinstance (blk, dict))
    assert_true ("data" in blk.keys ())
    assert_true ("hash" in blk.keys ())
    assert_true ("time" in blk.keys ())
    assert_true ("prev" in blk.keys ())

  def test_blockparser_with (self):
    with BlockParser (self.chain) as blkr:
      print (blkr)
      assert_true (isinstance (blkr, BlockParser))
      blk = blkr[1]
      assert_true (isinstance (blk, dict))
      assert_true ("data" in blk.keys ())
      assert_true ("hash" in blk.keys ())
      assert_true ("time" in blk.keys ())
      assert_true ("prev" in blk.keys ())
