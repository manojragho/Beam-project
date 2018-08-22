from google.cloud import bigquery
from google.cloud.bigquery import Dataset
import csv

from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField

big_query_client = bigquery.Client.from_service_account_json('my-beam-project-b2834963a4ae.json')

dataset_ref = big_query_client.dataset('D')
dataset = Dataset(dataset_ref)
dataset.description = 'my dataset'
dataset = big_query_client.create_dataset(dataset)

SCHEMA = [
    SchemaField('Tweetscount', 'STRING', mode='Nullable'),


]
table_ref = big_query_client.dataset('D').table('tabl')

load_config = LoadJobConfig()
load_config.skip_leading_rows = 1
load_config.schema = SCHEMA
load_config.allow_quoted_newlines = True
load_config.ignore_unknown_values= False
load_config.max_bad_records = 200

# Contents of csv_file.csv:
#     Name,Age
#     Tim,99
with open('tweetsfile.csv', 'rb') as readable:
    big_query_client.load_table_from_file(
        readable, table_ref, job_config=load_config)
