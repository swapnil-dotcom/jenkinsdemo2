import pandas as pd

data = [
{
    "id": 1,
    "name": "Swapnil Bankar",
    "age": 25
},
{
    "id": 2,
    "name": "Rahul Gandhile",
    "age": 24
},
{
    "id": 3,
    "name": "Rohan Bhople",
    "age": 23
}
]

df = pd.DataFrame(data)

print(df)