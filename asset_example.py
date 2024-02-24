from etl_example import etl, extract, transform, load
from dagster import AssetSelection, Definitions, asset, define_asset_job 
import pandas as pd 
# convert extract function to dagster asset 

@asset
def extract_data() -> pd.DataFrame:
    return extract()

@asset
def transformed_data(extract_data: pd.DataFrame) -> pd.DataFrame:
    return transform(extract_data)

@asset
def loaded_data(transformed_data: pd.DataFrame) -> None:
    load(transformed_data)


# Addition: define all assets
all_assets = [extract_data, transformed_data, loaded_data]  
# Addition: define a job that will materialize the assets
hackernews_job = define_asset_job("etl_example_job", selection=AssetSelection.all())

defs = Definitions(
    assets=all_assets,
    jobs=[hackernews_job],  # Addition: add the job to Definitions object (see below)
)