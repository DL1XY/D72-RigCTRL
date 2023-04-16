class SerialInvoker:

    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        rcvd = {}
        for command in self._commands:
            resp = command.execute()
            print (f'invoker resp:{resp}')
            if resp != 'N' and resp != None:
                tokens = resp.split()
                if len(tokens) != 2:
                    print(f'Error cmd:{command.cmd} resp:{resp}, wrong token length')    
                    continue
                else:
                    rcvd[tokens[0]]=tokens[1]
            else:
                print(f'Error cmd:{command.config.cmd} resp:{resp}')
                continue

        return rcvd
