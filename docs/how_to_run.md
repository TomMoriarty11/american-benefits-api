# How to Run the API

# Step 1: Clone the Repo
git clone https://github.com/yourusername/american-benefits-api.git
cd american-benefits-api

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Run the API
uvicorn api.main:app --reload
The visit: http://localhost:8000/benefits/CA (This launches a live deployment server. FastAPI prepares your app's endpoints and makes them accessible on localhost. 

#Step 4: Add Data Files
---

Step 8: Add `docs/api_reference.md`

```markdown
# 📚 API Reference

# GET `/benefits/{state}`
Returns all benefit programs available for a U.S. state.

**Example**: `/benefits/CA`
# Response:
'json
{
  "state": "CA",
  "programs": [
    {"name": "Student Loan Assistance", "eligible": "Employed, Degree Holders", "type": "Federal"},
    ...
  ]
}
