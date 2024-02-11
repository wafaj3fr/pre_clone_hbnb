import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True
    
    def emptyline(self):
        pass
    
    def do_EOF(self, line):
        return True
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()