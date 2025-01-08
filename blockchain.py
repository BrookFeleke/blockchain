from hashlib import sha256
from typing import List, Dict

class Block:
    def __init__(self, index: int, transactions: List[Dict], previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.transactions}{self.previous_hash}{self.nonce}"
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict] = []
        self.difficulty = 2
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        genesis_block.nonce = 0
        genesis_block.previous_hash = "0"
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_new_transaction(self, transaction: Dict):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=last_block.compute_hash(),
        )
        new_block.nonce = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []

    def proof_of_work(self, block: Block) -> int:
        while True:
            hash_value = block.compute_hash()
            if hash_value.startswith("0" * self.difficulty):
                return block.nonce
            block.nonce += 1

    def is_valid_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.compute_hash():
                return False
            if not current.compute_hash().startswith("0" * self.difficulty):
                return False
        return True
