# from sensor_invoke_after_etl import etl2_job
# from dagster import AssetSelection, Definitions, RunsFilter, SensorEvaluationContext, asset, define_asset_job, sensor, RunRequest

# @sensor(job=etl2_job)
# def etl2_sensor(context: SensorEvaluationContext):
#     run_records = context.instance.get_run_records(
#         filters= RunsFilter(
#             job_name="etl1_job",
#             statuses=["SUCCESS"],
#         )
#     )
#     if run_records:
#         yield RunRequest(run_key="etl2_sensor", run_config={})