import hashlib
import time
import json
from datetime import datetime

class BTCMiner:
    def __init__(self):
        self.difficulty = 4
        self.max_nonce = 2 ** 32
        self.target = 2 ** (256 - self.difficulty)

    def mine_block(self, block_data):
        start_time = time.time()
        prefix = '0' * self.difficulty
        
        for nonce in range(self.max_nonce):
            data = str(block_data) + str(nonce)
            hash_result = hashlib.sha256(data.encode('utf-8')).hexdigest()
            
            if hash_result.startswith(prefix):
                print(f"Block mined! Nonce: {nonce}")
                print(f"Hash: {hash_result}")
                print(f"Mining time: {time.time() - start_time} seconds")
                return nonce, hash_result
        
        return None, None

if __name__ == "__main__":
    miner = BTCMiner()
    block_data = {
        'timestamp': str(datetime.now()),
        'transactions': [],
        'previous_hash': '0' * 64
    }
    
    nonce, hash_result = miner.mine_block(json.dumps(block_data))
