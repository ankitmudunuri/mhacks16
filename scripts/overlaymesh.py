import queue as Queue

def SpeechForBox(global q, char_limit: double):
    cur_string = ""
    char_count = 0

    while not q.isempty():
        str_size = len(q[0])
        cur_string.append(q.pop(0) + " ")
        char_count += str_size
        yield cur_string

        if char_count + len(q[0]) > char_limit:
            cur_string = ""
            char_count = 0

    return
