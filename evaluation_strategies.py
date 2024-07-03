from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response):
        pass

class LengthEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response):
        return len(response)

class KeywordEvaluationStrategy(EvaluationStrategy):
    def __init__(self, keyword):
        self.keyword = keyword

    def evaluate(self, response):
        return self.keyword in response