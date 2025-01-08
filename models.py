# app/models.py
from pydantic import BaseModel, Field
from typing import List, Dict

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float
    input_utxos: List[Dict]
    output_utxos: List[Dict]
    signature: str

class BlockData(BaseModel):
    index: int
    transactions: List[Transaction]
    previous_hash: str
    nonce: int
