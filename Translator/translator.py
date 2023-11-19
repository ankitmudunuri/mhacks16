from googletrans import Translator
import queue
import sys
mainpath = __file__.replace("/Translator/translator.py", "/")
analyzepath = __file__.replace("/Translator/translator.py", "/Analyze")
sys.path.append(mainpath)
sys.path.append(analyzepath)
import config as cfg
import audio_in as a_in


def languager(text: str) -> str:
    translator = Translator()
    return translator.translate(text, cfg.translator_languages['dest_lang'],cfg.translator_languages['init_lang']).text

    
    
def main(old_q:queue.Queue(), newqueue:queue.Queue()) -> None:
    while True:
        phrase = old_q.get()
        if phrase:
            newqueue.put(languager(phrase))
        else:
            newqueue.put("")
        
        

        
    