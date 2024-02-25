from sensor_invoke_after_etl import etl2_sensor
from dagster import repository

@repository
def my_repository():
    return [etl2_sensor]

