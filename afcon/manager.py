from flask.ext.migrate import MigrateCommand
from flask.ext.script import Manager, Server as ServerCommand

from afcon import app


class Server(ServerCommand):
    def handle(self, *args, **kwargs):
        app.running = True

        super(Server, self).handle(*args, **kwargs)

        print("Shutting down")
        app.running = False


manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server)