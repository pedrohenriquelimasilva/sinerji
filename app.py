import argparse
import sys
from llm_factory import LLMFactory
from commands import ChatGPTCommand, BertCommand
from invoker import Invoker
from evaluation_strategies import LengthEvaluationStrategy, KeywordEvaluationStrategy
from observer import ResponsePresenter


def main():
  # escolhas via prompt: modelo, pergunta, estrategia de avaliação e 
    parser = argparse.ArgumentParser(description="Ask questions to different models.")
    parser.add_argument("--model", type=str, required=True, choices=["chatgpt", "bert"], help="Escolha o modelo que será usado")
    parser.add_argument("--question", type=str, required=True, help="Pergunta para o modelo")
    parser.add_argument("--eval_strategy", type=str, required=True, choices=["length", "keyword"], help="Escolha a estratégia de avaliação")
    parser.add_argument("--keyword", type=str, help="Palavra-chave para estratégia de avaliação de palavras")

    # Simular argumentos no ambiente interativo
    if len(sys.argv) == 1:
        sys.argv.extend(["--model", "chatgpt", "--question", "Hello! Could you solve 2+2?", "--eval_strategy", "length"])
        # ou para testar com o BERT
        sys.argv.extend(["--model", "bert", "--question", "Hello! Could you solve 2+2?"])

    args = parser.parse_args()

    # instanciar modelos
    chatgpt_client = LLMFactory.create_client("chatgpt")
    bert_client = LLMFactory.create_client("bert-base-uncased")

    invoker = Invoker()

    # modelo escolhido
    if args.model == "chatgpt":
        command = ChatGPTCommand(chatgpt_client, args.question)
    elif args.model == "bert":
        command = BertCommand(bert_client, args.question)
    
    # registrar
    invoker.register_command(args.model, command)


    # verificação de estrategia
    if args.eval_strategy == "length":
        strategy = LengthEvaluationStrategy()
    elif args.eval_strategy == "keyword":
        if not args.keyword:
            print("Keyword evaluation strategy requires --keyword argument")
            sys.exit(1)
        strategy = KeywordEvaluationStrategy(args.keyword)
    
    invoker.set_evaluation_strategy(strategy)

    presenter = ResponsePresenter()
    invoker.add_observer(presenter)

    invoker.execute_command(args.model)

if __name__ == "__main__":
    main()
    