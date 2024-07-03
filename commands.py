from command import Command

class ChatGPTCommand(Command):
    def __init__(self, client, message):
        self.client = client
        self.message = message

    def execute(self):
        return self.client.get_completion(self.message)

class BertCommand(Command):
    def __init__(self, client, message):
        self.client = client
        self.message = message

    def execute(self):
        return self.client.get_completion(self.message)
