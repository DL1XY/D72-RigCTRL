from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.ba import BA

class BAGet(SerialCommand):
    config = BA()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        return self._receiver.action(f"{self.config.cmd}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = BAGet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()

