from subject import Subject

class Invoker(Subject):
    def __init__(self):
        self.commands = {}
        self.evaluation_strategy = None
        self.observers = []

    def register_command(self, name, command):
        self.commands[name] = command

    def set_evaluation_strategy(self, strategy):
        self.evaluation_strategy = strategy

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, response, evaluation_result):
        for observer in self.observers:
            observer.update(response, evaluation_result)

    def execute_command(self, name):
        if name in self.commands:
            response = self.commands[name].execute()
            if self.evaluation_strategy:
                evaluation_result = self.evaluation_strategy.evaluate(response)
                self.notify_observers(response, evaluation_result)
                return response, evaluation_result
            self.notify_observers(response, None)
            return response, None
        else:
            print(f"Command {name} not recognized.")
            return None, None
