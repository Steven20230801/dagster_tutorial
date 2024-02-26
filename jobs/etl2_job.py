from reports.etl2 import etl, extract, transform, load
from dagster import (
    AssetKey,
    AssetSelection,
    Definitions,
    RunsFilter,
    SensorEvaluationContext,
    asset,
    asset_sensor,
    define_asset_job,
    sensor,
    RunRequest,
)
import pandas as pd

# convert extract function to dagster asset


@asset
def etl2_extract_data() -> pd.DataFrame:
    return extract()


@asset
def etl2_transformed_data(etl2_extract_data: pd.DataFrame) -> pd.DataFrame:
    return transform(etl2_extract_data)


@asset
def etl2_loaded_data(etl2_transformed_data: pd.DataFrame) -> None:
    load(etl2_transformed_data)


# Addition: define all assets
all_assets = [etl2_extract_data, etl2_transformed_data, etl2_loaded_data]
# Addition: define a job that will materialize the assets
etl2_job = define_asset_job("etl2_after_etl1", selection=AssetSelection.all())

defs = Definitions(
    assets=all_assets,
    jobs=[etl2_job],  # Addition: add the job to Definitions object (see below)
)
