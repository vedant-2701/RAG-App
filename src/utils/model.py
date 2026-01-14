import ollama
from src.helper.prompt import Prompt 
from src.config.settings import Settings

# Function to generate answer using ollama with formatted prompt
def generate_answer(context: str, question: str) -> str:
    answer = ollama.generate(
        model=Settings.MODEL_NAME,
        prompt=Prompt.CONTEXT_QUESTION_ANSWER.format(context=context, question=question)
    )
    return answer["response"]