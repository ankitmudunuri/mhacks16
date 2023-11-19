from googletrans import Translator
import queue


def languager(text: str, lang: str, dest: str) -> str:
    translator = Translator()
    return translator.translate(text, dest='en').text

def enqueue(q: queue.Queue, text: str) -> None:
    q.put(text)
    
    
def main() -> None:
    with open('config.py', 'r') as f:
        text = f.read()
    