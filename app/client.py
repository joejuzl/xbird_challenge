import requests
from google.protobuf import json_format

from sample.sample_pb2 import Samples


def load_file_into_samples(file, collection):
    with open(file) as data_file:
        content = data_file.readlines()

    for line in content:
        sample = collection.samples.add()
        json_format.Parse(line.strip(), sample)


samples = Samples()

print('Loading activity.json')
load_file_into_samples('activity.json', samples)

print('Loading location.json')
load_file_into_samples('location.json', samples)

print('Posting sample data')
HEADERS = {'Content-Type': 'application/octet-stream'}
response = requests.post('http://localhost:8081/samples', data=samples.SerializeToString(), headers=HEADERS)
print(response.content)
