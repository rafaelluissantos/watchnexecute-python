import os

class Executor:

    def __init__(self, cmd_str):
        self.cmd = cmd_str

    def execute(self, parameter_list):
        complete_cmd = self.cmd.replace("%s", parameter_list) 
        print ("executing \"%s\"" % complete_cmd)
        os.system(complete_cmd)