import cmd
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import classes


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, model):
        """create new base model"""
        if model:
            for k, v in classes.items():
                if model == k:
                    New_inst = v()
                    New_inst.save()
                    print(New_inst.id)
                    break
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args,):
        """Prints the string form of instance"""
        if args:
            my_args = args.split()
            for a, b in classes.items():
                if my_args[0] == a:
                    break
            else:
                print("** class doesn't exist **")
                return
            if len(my_args) < 2:
                print("** instance id missing **")
                return
            inst = f"{a}.{my_args[1]}"
            stk = models.storage.all()
            if inst in stk:
                for k, v in stk.items():
                    if inst == k:
                        print(v)
            else:
                print('** no instance found **')
        else:
            print("** class name missing **")

    def do_destroy(self, args,):
        """Deletes an instance based on the class name and id"""
        if args:
            my_args = args.split()
            for a, b in classes.items():
                if my_args[0] == a:
                    break
            else:
                print("** class doesn't exist **")
                return
            if len(my_args) < 2:
                print("** instance id missing **")
                return
            inst = f"{a}.{my_args[1]}"
            stk = models.storage.all()
            if inst in stk:
                del models.storage._FileStorage__objects[inst]
                models.storage.save()
            else:
                print('** no instance found **')
        else:
            print("** class name missing **")

    def do_all(self, model):
        """Prints all string representation of all instances"""
        if model:
            for k, v in classes.items():
                if model == k:
                    break
            else:
                print("** class doesn't exist **")
                return
        lst = []
        for a, b in models.storage.all().items():
            if model:
                if model == a.split('.')[0]:
                    lst.append(str(b))
            else:
                lst.append(str(b))
        print(lst)

    def do_update(self, args):
        """updates an instance"""
        if not args:
            print("** class name missing **")
            return
        my_args = args.split()
        if my_args[0] == "BaseModel":
            pass
        else:
            print("** class doesn't exist **")
            return
        if len(my_args) < 2:
            print("** instance id missing **")
            return
        if my_args[0] + '.' + my_args[1] in models.storage.all():
            pass
        else:
            print('** no instance found **')
            return
        if len(my_args) < 3:
            print('** attribute name missing **')
            return
        if len(my_args) < 4:
            print('** value missing **')
            return
        for key, val in models.storage.all().items():
            if my_args[0] + '.' + my_args[1] == key:
                break
        try:
            atype = type(getattr(val, my_args[2]))
            setattr(val, my_args[2], atype(my_args[3][1:-1]))
        except:
            setattr(val, my_args[2], my_args[3][1:-1])
        val.save()

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
