from googletrans import Translator
import queue
import audio_in.py as a_in
import config as cfg


def languager(text: str) -> str:
    translator = Translator()
    return translator.translate(text, cfg.translator_languages['dest_lang'],cfg.translator_languages['init_lang']).text

def enqueue(q: queue.Queue, text: str) -> None:
    q.put(text)
    
    
def main(q:queue.Queue()) -> None:
    phrase = a_in.main()
    enqueue(q, languager(phrase))
    return q

        
    