from elasticsearch import Elasticsearch
import csv

# Elasticsearch connection settings
es = Elasticsearch([{'host': 'es', 'port': 9200}])

# CSV file path
csv_file = 'data.csv'  # Changed the CSV file path

# Elasticsearch index name
index_name = 'cloud'  # Changed the index name to "cloud"

# Open and read the CSV file
with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Index the CSV data into Elasticsearch without specifying doc_type
        es.index(index=index_name,doc_type="doc", body=row)
        print(f'Indexed: {row}')

print('CSV data has been imported to Elasticsearch')
