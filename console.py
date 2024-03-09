import cmd
import json
from models.base_model import BaseModel
from models.base_model import storage
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, model):
        """create new base model"""
        if model:
            if model == 'BaseModel':
                New_inst = BaseModel()
                New_inst.save()
                print(New_inst.id)
            else:
                print("** class doesn't exist **")   
        else:
            print("** class name missing **")

    def do_show(self, args,):
        """Prints the string representation of an instance based on the class name and id"""
        if args:
            try:
                bm, myid = args.split("BaseModel", 1)
                if myid:
                    inst = f"BaseModel.{myid[1:]}"
                    stk = storage.all()
                    if inst in stk:
                        for k, v in stk.items():
                            if inst == k:
                                print(v)
                        
                    else:
                        print('** no instance found **')

                else:
                    print("** instance id missing **")
            
            except ValueError:
                pass
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
    def do_destroy(self, args,):
        """Deletes an instance based on the class name and id"""
        if args:
            try:
                bm, myid = args.split("BaseModel", 1)
                if myid:
                    inst = f"BaseModel.{myid[1:]}"
                    stk = storage.all()
                    if inst in stk:
                        del models.storage._File_storage__objects[inst]
                        models.storage.save()
                    else:
                        print('** no instance found **')

                else:
                    print("** instance id missing **")
            
            except ValueError:
                pass
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, model):
        """Prints all string representation of all instances"""
        if model:
            if model == 'BaseModel':
                l =[]
                for key, value in models.storage.all().items():
                    l.append(str(value))
                print(l)    

            else:
                print("** class doesn't exist **")   


    def emptyline(self):
        """skips empty lines"""
        pass

    def do_EOF(self, line):
        """command to exit the program"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()    