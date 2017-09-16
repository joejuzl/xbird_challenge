from sample.sample_pb2 import Samples as ProtoSamples, Activity as ProtoActivity
from sample.sample import Sample
from sample.activity import Activity


def save_samples(sample_data):
    samples = ProtoSamples()
    samples.ParseFromString(sample_data)
    for proto_sample in samples.samples:
        sample = Sample.from_proto(proto_sample)

        data = proto_sample.data
        if data.Is(ProtoActivity.DESCRIPTOR):
            proto_activity = ProtoActivity()
            data.Unpack(proto_activity)
            Activity.from_proto(proto_activity, sample)

