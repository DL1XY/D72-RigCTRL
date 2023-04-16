from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Status, KeyLock
from d72.cmds.lk import LK

class LKSet(SerialCommand):

    config = LK()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.status not in Status:
            raise ValueError (f"Status {self.config.status} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.lock not in KeyLock:
            raise ValueError (f"Key lock {self.config.lock} outside valid range, should be between {KeyLock.KEY_LOCK.value} and {KeyLock.KEY_F_LOCK.value}")

        return self._receiver.action(f"{self.config.cmd} {self.config.status},{self.config.lock}")  

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = LKSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd) 
    inv.execute_commands()

