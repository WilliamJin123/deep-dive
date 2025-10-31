import os
from getpass import getpass
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv

def langSmithInit():
    load_dotenv()
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or getpass(
        "Enter LANGCHAIN API Key: "
    )

    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "langchain-course-langsmith"

    os.environ["CEREBRAS_API_KEY"] = os.getenv("CEREBRAS_API_KEY") or getpass(
        "Enter OpenAI API Key: "
    )
if __name__=="__main__":
    langSmithInit()

    llm = ChatCerebras(temperature=0.0, model="llama-3.3-70b")
    llm.invoke("hello")

    from langsmith import traceable
    import random
    import time


    @traceable
    def generate_random_number():
        return random.randint(0, 100)

    @traceable
    def generate_string_delay(input_str: str):
        number = random.randint(1, 5)
        time.sleep(number)
        return f"{input_str} ({number})"

    @traceable
    def random_error():
        number = random.randint(0, 1)
        if number == 0:
            raise ValueError("Random error")
        else:
            return "No error"

    from tqdm.auto import tqdm

    for _ in tqdm(range(10)):
        generate_random_number()
        generate_string_delay("Hello")
        try:
            random_error()
        except ValueError:
            pass


    from langsmith import traceable

    @traceable(name="Chitchat Maker")
    def error_generation_function(question: str):
        delay = random.randint(0, 3)
        time.sleep(delay)
        number = random.randint(0, 1)
        if number == 0:
            raise ValueError("Random error")
        else:
            return "I'm great how are you?"


    for _ in tqdm(range(10)):
        try:
            error_generation_function("How are you today?")
        except ValueError:
            pass