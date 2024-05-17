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
    graph,
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


@op(ins={"search_date": In(date), "report_config": In(dict)})
def extract_data(search_date: date, report_config: dict) -> pd.DataFrame:
    return extract(search_date, report_config)


@op
def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    return transform(data)


@op
def load_data(data: pd.DataFrame) -> None:
    load(data)


@asset
def main():
    search_date = date.today()
    report_config = {}
    data = extract_data(search_date, report_config)
    data = transform_data(data)
    load_data(data)


job = define_asset_job("main_etl3_with_op")
schedule = ScheduleDefinition(
    job=job, cron_schedule="00 14 * * 1-5", execution_timezone="Asia/Singapore"
)
definition = Definitions(assets=[main], schedules=[schedule])
