from orator.migrations import Migration


class CreateSamplesTable(Migration):

    def up(self):
        with self.schema.create('samples') as table:
            table.increments('id')
            table.timestamps()
            table.datetime('timestamp')

    def down(self):
        self.schema.drop('samples')
