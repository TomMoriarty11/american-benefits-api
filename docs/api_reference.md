# Endpoint Description
## GET `/benefits/{state}`

# Purpose
Returns all benefit programs available for a U.S. state.

# Example Use
Example: `/benefits/CA`

# Sample Response
{
  "state": "CA",
  "programs": [
    {
      "name": "Student Loan Assistance",
      "eligible": "Employed, Degree Holders",
      "type": "Federal"
    },
    {
      "name": "CalHFA Housing Program",
      "eligible": "First-time buyers",
      "type": "State"
    }
  ]
}


