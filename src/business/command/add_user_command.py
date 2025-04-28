from business.command.command import Command

class AddUserCommand(Command):
    def __init__(self, user_control, user):
        self.user_control = user_control
        self.user = user

    def execute(self):
        return self.user_control.add(self.user)
