

# **Blockchain API with FastAPI**

This project demonstrates the implementation of a basic blockchain system using FastAPI. It includes endpoints for mining blocks, adding transactions, validating blocks, and fetching the blockchain.

## **Features**
- Mine a new block (`/mine_block`)
- Accept new transactions (`/new_transaction`)
- Add received blocks (`/add_block`)
- Fetch the current blockchain (`/chain`)
- Basic blockchain validation with proof-of-work and block validation.

## **Tech Stack**
- **Python 3.9+**
- **FastAPI**: Web framework for building APIs.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server for running the FastAPI app.

---

## **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/your_username/blockchain_api.git
   cd blockchain_api
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate       # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## **API Endpoints**

### 1. **Mine a Block**
   - **Endpoint**: `/mine_block`
   - **Method**: `POST`
   - **Description**: Mines a new block using pending transactions and adds it to the blockchain.
   - **Response**:
     ```json
     {
       "message": "Block mined successfully",
       "block": { ...block_data }
     }
     ```

### 2. **Add a New Transaction**
   - **Endpoint**: `/new_transaction`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "sender": "Alice",
       "receiver": "Bob",
       "amount": 50.0,
       "input_utxos": [...],
       "output_utxos": [...],
       "signature": "signature_string"
     }
     ```
   - **Description**: Adds a new transaction to the list of pending transactions.
   - **Response**:
     ```json
     {
       "message": "Transaction added successfully"
     }
     ```

### 3. **Add a Block**
   - **Endpoint**: `/add_block`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "index": 1,
       "transactions": [...],
       "previous_hash": "hash_string",
       "nonce": 12345
     }
     ```
   - **Description**: Accepts a block from another node and validates it before appending it to the chain.
   - **Response**:
     ```json
     {
       "message": "Block added successfully"
     }
     ```

### 4. **Get Blockchain**
   - **Endpoint**: `/chain`
   - **Method**: `GET`
   - **Description**: Returns the current blockchain.
   - **Response**:
     ```json
     {
       "chain": [...list_of_blocks]
     }
     ```

---

