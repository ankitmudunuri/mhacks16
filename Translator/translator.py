from googletrans import Translator
import queue
import sys
path = __file__.replace("/Translator/translator.py", "/Analyze")
sys.path.append(path)
import config as cfg
import audio_in as a_in

def languager(text: str) -> str:
    translator = Translator()
    return translator.translate(text, cfg.translator_languages['dest_lang'],cfg.translator_languages['init_lang']).text

def enqueue(q: queue.Queue, text: str) -> None:
    q.put(text)
    
    
def main(q:queue.Queue(), on:bool) -> None:
    newqueue = queue.Queue()
    while True:
        if not on:
            break
        else:
            newqueue = languager(q.get())
            phrase = q.get()
            newqueue = languager(phrase)
            return newqueue

        
    
