
'''
simple blockchain with python
TODO: next step, implement json objects instead of python list´s
'''

# imports
import hashlib
from typing import Mapping

class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        '''
        function to create the first block 
        '''
        self.chain.append(DataBlock("0", ['1st Block']))
    
    def create_block_from_transaction(self, transaction_list):
        '''
        function to create one block from transaction
        to append blocks to the chain with just a list of transactions
        the first argument in this case is the previous hash block (previous_block_hash)
        '''
        previous_block_hash = self.last_block.block_hash
        self.chain.append(DataBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        '''
        function to display/print data chain
        with a for loop on the chain range
        '''
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        '''
        property to access the last element of the chain
        '''
        return self.chain[-1]
    
class DataBlock:
    def __init__(self, previous_block_hash, transaction_list):
        # reference to the previous block of data
        self.previous_block_hash = previous_block_hash
        # a list with all of the transactions made
        self.transaction_list = transaction_list
        
        # string with the previous hash and the transaction list
        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        # create the block_hash, which other blocks will use to continue the chain
        # pre-built sha256 from hashlib, to make immutable blocks
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
# test function 1
# test DataBlock        
def test1():
    d1 = 'data 1'
    d2 = 'data 2'
    d3 = 'data 3'
    d4 = 'data 4'
    
    block1 = DataBlock(previous_block_hash='first_block', transaction_list=[d1, d2])
    block2 = DataBlock(previous_block_hash=block1.block_hash, transaction_list=[d3, d4])

    print('data1:', str(block1.block_data))
    print('hash1:', str(block1.block_hash))
    
    print('data2:', str(block2.block_data))
    print('hash2:', str(block2.block_hash))
    
def test2():
    # examples of blocks of data
    d1 = 'data 1'
    d2 = 'data 2'
    d3 = 'data 3'
    d4 = 'data 4'
    
    # create blockchain
    bc = Blockchain()
    
    # append/create block from transactions
    bc.create_block_from_transaction([d1, d2])
    bc.create_block_from_transaction([d3, d4])
    
    # display all block on the chain
    bc.display_chain()
    
if __name__ == "__main__":
    # test1()
    test2()