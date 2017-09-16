from orator import Model
from orator.orm import belongs_to

from db.connection import get_connection
from sample.sample import Sample

Model.set_connection_resolver(get_connection())


class Activity(Model):

    @belongs_to
    def sample(self):
        return Sample

    @classmethod
    def from_proto(cls, proto, sample):
        activity = cls()

        activity.sample().associate(sample)

        activity.unknown = proto.unknown
        activity.stationary = proto.stationary
        activity.walking = proto.walking
        activity.running = proto.running

        activity.save()

        return activity


