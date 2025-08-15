# How to Run the API

# Step 1: Clone the Repo
git clone https://github.com/yourusername/american-benefits-api.git
cd american-benefits-api

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Run the API
uvicorn api.main:app --reload
The visit: http://localhost:8000/benefits/CA (This launches a live deployment server. FastAPI prepares your app's endpoints and makes them accessible on localhost. 

