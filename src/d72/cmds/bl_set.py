from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band
from d72.cmds.bl import BL

# TODO Seems to be useless, just get ? as response
class BLSet(SerialCommand):

    config = BL()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if int(self.config.backlightStatus) not in range(0,9):
            raise ValueError (f"Backlight status {self.config.backlightStatus} outside valid range, should be between 0 and 8")
        return self._receiver.action(f"{self.config.cmd} {self.config.backlightStatus}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = BLSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
