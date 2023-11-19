from googletrans import Translator
import queue
import sys
mainpath = __file__.replace("/Translator/translator.py", "/")
analyzepath = __file__.replace("/Translator/translator.py", "/Analyze")
sys.path.append(mainpath)
sys.path.append(analyzepath)
import config as cfg
import audio_in as a_in


def languager(translator: Translator(), text: str) -> str:
    try:
        return translator.translate(text, cfg.translator_languages['dest_lang'],cfg.translator_languages['init_lang']).text
    except:
        return ""
    
    
def main(old_q:queue.Queue(), newqueue:queue.Queue()) -> None:
    translator = Translator()
    while True:
        phrase = old_q.get()
        if phrase:
            newqueue.put(languager(translator, phrase))
        else:
            newqueue.put("")
        
        

        
    