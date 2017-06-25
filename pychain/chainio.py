from chain import Chain
import sys

"""override the __builtin__.open to access a chain
   from the globals context"""
def open (blockname):
  chain = globals["chain"]
  return BlockReader (chain, blockname)

class BlockReader:
  def __init__ (self, chain, blockname):
    self.chain = chain
    self.block = blockname

  def read (self, count=-1):
    return self.chain[self.block] 


class BlockParser:
  def __init__ (self, chain):
    self.chain = chain

  def __enter__ (self):
    print ("enter")

  def __exit__ (self, type, value, traceback):
    return False

  def __getitem__ (self, i):
    return self.chain[i]
