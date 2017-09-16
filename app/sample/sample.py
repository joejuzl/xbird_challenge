from orator import Model

from db.connection import get_connection

Model.set_connection_resolver(get_connection())


class Sample(Model):
    @classmethod
    def from_proto(cls, proto):
        sample = cls()
        sample.timestamp = proto.timestamp.ToDatetime()
        sample.save()

        return sample
