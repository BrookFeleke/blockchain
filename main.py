from fastapi import FastAPI, HTTPException
from blockchain import Blockchain  
from models import Transaction, BlockData  

app = FastAPI()
blockchain = Blockchain()

@app.post("/mine_block")
def mine_block():
    blockchain.mine_block()
    return {"message": "Block mined successfully", "block": blockchain.chain[-1].__dict__}

@app.post("/new_transaction")
def new_transaction(transaction: Transaction):
    blockchain.add_new_transaction(transaction.dict())
    return {"message": "Transaction added successfully"}

@app.post("/add_block")
def add_block(block_data: BlockData):
    new_block = Block(
        index=block_data.index,
        transactions=[tx.dict() for tx in block_data.transactions],
        previous_hash=block_data.previous_hash,
        nonce=block_data.nonce
    )
    if blockchain.is_valid_chain():
        blockchain.chain.append(new_block)
        return {"message": "Block added successfully"}
    raise HTTPException(status_code=400, detail="Invalid block")

@app.get("/chain")
def get_chain():
    return {"chain": [block.__dict__ for block in blockchain.chain]}
