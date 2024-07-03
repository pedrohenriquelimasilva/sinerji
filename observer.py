from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, response, evaluation_result):
        pass

class ResponsePresenter(Observer):
    def update(self, response, evaluation_result):
        print("Model response:", response)
        print("Evaluation result:", evaluation_result)
