import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        print("")