from genesis import create_genesis_block
from genesis import next_block

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)

    blockchain.append(block_to_add)

    previous_block = block_to_add

    print "Block #{} has been added to the blockchain!".format(block_to_add.index)

    print "Hash: {}".format(block_to_add.hash)

    print "Data: {}\n".format(block_to_add.data)