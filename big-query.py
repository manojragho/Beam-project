from google.cloud import bigquery
from google.cloud.bigquery import Dataset
import csv

from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField

big_query_client = bigquery.Client.from_service_account_json('my-beam-project-b2834963a4ae.json')




dataset_ref = big_query_client.dataset('c')
table_ref = dataset_ref.table('l')
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True

with open('celebs.csv', 'rb') as source_file:
    job = big_query_client.load_table_from_file(
        source_file,
        table_ref,
        location='US',  # Must match the destination dataset location.
        job_config=job_config)  # API request

#job.result()  # Waits for table load to complete.

print('Loaded {} rows into {}:{}.'.format(
    job.output_rows, 'c','l'))



