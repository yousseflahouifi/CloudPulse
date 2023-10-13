from django_elasticsearch_dsl import DocType, Index
from .models import Cloud

cloud = Index('cloud')
cloud.settings(number_of_shards=1, number_of_replicas=0)

@cloud.doc_type
class CloudDocument(DocType):
    class Meta:
        # The model associated with Elasticsearch document
        model = Cloud
        # The fields of the model you want to be indexed
        # in Elasticsearch
        fields = (
            'ip',
            'common_name',
            'organization',
            'country',
            'locality',
            'province',
            'sandns',
            'sanip',
            'selfsigned',
        )
