# -*- coding: utf-8 -*-
#@cserko

# Create a Blockchain!

# importing the libraries. . .
import datetime
import hashlib
import json
from flask import Flask, jsonify


# Building Blockchain
class BlockChain:
    
    def __init__(self):
        self.difficulty = '0000'
        self.chain = []
        self.createblock(proof = 1, previous_hash = '0')
        
    def createblock(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash
                }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def hash_operation(self, proof, previous_proof, difficulty):
        hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:4] is difficulty:
            return True
        else:
            return False
        

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] =='0000':
                check_proof = True                
            else:
                new_proof += 1
                
        return new_proof
    def hash_(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_valid_chain(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash[previous_block]:
                return False
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] !='0000':
                return False
            previous_block = block
            block_index += 1
        return True
            
 #Build Mining Tools. . . Flask
 # WEB server initialized
#from flask import Flask

app = Flask(__name__)

# Create a blockchain object. . .
blockchain = BlockChain()
@app.route('/mine_block', methods = {'GET'})
def mine_block():
    previous_block = blockchain.get_previous_block()
    
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    
    previous_hash = blockchain.hash_(previous_block)
    
    block = blockchain.createblock(proof, previous_hash)
    response = {"message": "Congratulations, you just mined the block!",
                "index": block["index"],
                "timestamp": block["timestamp"],
                "proof": block["proof"],
                "previous_hash": block["previous_hash"]
                }
    return jsonify(response), 200
    

@app.route('/get_chain', methods = {'GET'})  
def get_Chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)
                }
    return jsonify(response), 200
    
    
# Run
    
app.run(host = '0.0.0.0', port = 5000)
    
    
    
    
    
    
    
    
    
