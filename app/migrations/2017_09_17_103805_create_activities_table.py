from orator.migrations import Migration


class CreateActivitiesTable(Migration):

    def up(self):
        with self.schema.create('activities') as table:
            table.increments('id')
            table.timestamps()
            table.boolean('unknown')
            table.boolean('stationary')
            table.boolean('walking')
            table.boolean('running')
            table.integer('sample_id').unsigned()
            table.foreign('sample_id').references('id').on('samples')

    def down(self):
        self.schema.drop('activities')

