import json
import os
from dagster import AssetExecutionContext, MetadataValue, asset, MaterializeResult


import requests
import pandas as pd

@asset
def extract() -> MaterializeResult:
    # download fake data    
    # create dataframe with 100 rows and columns id and score
    data = pd.DataFrame({
        "id": range(100),
        "score": range(100)
    })

    # check data directory exists
    os.makedirs("data", exist_ok=True)

    data.to_csv("data/fake_data.csv", index=False)
    # markdown preview head
    return MaterializeResult(
        metadata={
            "num_records": 20,
            "preview": MetadataValue.md(data.head().to_markdown())
        }
    )

# def topstory_ids() -> None: # turn it into a function
#     newstories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
#     top_new_story_ids = requests.get(newstories_url).json()[:100]

#     os.makedirs("data", exist_ok=True)
#     with open("data/topstory_ids.json", "w") as f:
#         json.dump(top_new_story_ids, f)