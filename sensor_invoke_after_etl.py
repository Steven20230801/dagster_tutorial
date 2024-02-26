import time
from etl2 import etl, extract, transform, load
from dagster import (
    AssetKey,
    AssetSelection,
    Definitions,
    RunsFilter,
    SensorEvaluationContext,
    asset,
    asset_sensor,
    define_asset_job,
    job,
    repository,
    sensor,
    RunRequest,
    DagsterRunStatus,
)
from asset_example2 import (
    etl2_job,
    extract,
    transform,
    load,
    etl,
    etl2_extract_data,
    etl2_transformed_data,
    etl2_loaded_data,
)


@job
def sensor_job():
    time.sleep(10)
    etl()


@sensor(job=sensor_job, minimum_interval_seconds=300)
def etl2_sensor(context: SensorEvaluationContext):
    monitored_jobs = "etl_example_job"
    run_records = context.instance.get_run_records(
        filters=RunsFilter(
            job_name=monitored_jobs,
            statuses=[DagsterRunStatus.SUCCESS],
        )
    )
    if run_records:
        yield RunRequest(run_key=None, run_config={})


@repository
def my_repository():
    return [etl2_sensor]
