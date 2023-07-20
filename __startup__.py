import jedi
import readline
import rlcompleter
import os
import atexit

historyPath = os.path.expanduser("~/.pyhistory")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)

readline.parse_and_bind("tab: complete")

# Use jedi for auto-completion
def complete(text, state):
    buffer = readline.get_line_buffer()
    if not buffer:
        return None
    column = readline.get_begidx()
    script = jedi.Script(buffer)
    completions = script.complete()
    return [c.name_with_symbols for c in completions][state]

readline.set_completer(complete)

