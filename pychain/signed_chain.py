from chain import Chain

class SignedChain(Chain):
  @staticmethod
  def default_signed_hash_function (block_def, sign):
    hash = sign[::-1] + ("0" * (64 - len (sign)))

    if block_def.has_key ("nonce") == False:
      block_def.update ({"nonce" : 0})

    while hash.startswith (sign.lower ()) == False:
      block_def["nonce"] += 1
      hash = Chain.default_hash_function (block_def)

    return hash

  def __init__ (self, sign, signed_hash_function):
    self.sign = sign.lower ()
    l_genesis_fn = lambda h_fn: Chain.genesis (h_fn)
    l_hash_fn = lambda block_def : signed_hash_function (block_def, self.sign)

    self.nonce = []
    Chain.__init__ (self, l_genesis_fn, l_hash_fn)

  def __getitem__ (self, i):
    """get the block at index i"""
    b = Chain.__getitem__ (self, i)
    b.update ({"nonce" : self.nonce[i]})
    return b

  def __setitem__ (self, i, value):
    """set the block values at index i, iff i >= len (self)"""
    Chain.__setitem__ (self, i, value)
    self.nonce.append (value["nonce"])

  def make (self, data, previous_hash):
    """create a block dictionary using the super class
    add a nonce field
    produce a new hash"""
    b = Chain.make (self, data, previous_hash)
    #b.update ({"hash" : SignedChain.hash (b, Chain.hash, self.sign)})
    return b

  def is_valid (self):
    """checks the super class validity holds and
    all hashes start with the sign for this chain"""
    return Chain.is_valid (self) and all ([h.startswith (self.sign) for h in self.chsh])