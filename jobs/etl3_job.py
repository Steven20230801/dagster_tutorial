from reports.etl_with_argument import extract, transform, load

import pandas as pd

import os
import sys
from datetime import datetime, timedelta, date, time
from typing import List


from dagster import (
    Any,
    AssetIn,
    In,
    asset,
    job,
    op,
    multi_asset,
    graph_asset,
    RetryPolicy,
    define_asset_job,
    Definitions,
    ScheduleDefinition,
    FilesystemIOManager,
    op,
)


@op(out=AssetIn("extracted_data", asset_key="extracted_data"))
def extract_data(search_date: date, report_config: dict) -> pd.DataFrame:
    return extract(search_date, report_config)


@op
def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    return transform(data)


@op
def load_data(data: pd.DataFrame) -> None:
    load(data)


@job
def main():
    search_date = date.today()
    report_config = {}
    data = extract_data(search_date, report_config)
    data = transform_data(data)
    load_data(data)


# job = define_asset_job("test")
# schedule = ScheduleDefinition(job=job, cron_schedule="00 14 * * 1-5", execution_timezone="Asia/Singapore")
# io_manager = FilesystemIOManager(base_dir=r"reports\steven_workspace\ftt\ftt_temp")
# definition = Definitions(assets=[extract_data, transform_data], schedules=[schedule], resources={"io_manager": io_manager})
