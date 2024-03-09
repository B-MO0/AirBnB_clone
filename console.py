import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_create(self, model):
        if model:
            if model == 'Basemodel':
                model = BaseModel()
                model.save()
                print(model.id)
            else:
                print("** class doesn't exist **")   
        else:
            print("** class name missing **")
            

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True
    """Quit command to exit the program"""
    def do_quit(self, line):
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()    