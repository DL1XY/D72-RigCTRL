from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import InternalGPS,Status
from d72.cmds.gp import GP

class LKSet(SerialCommand):

    config = GP()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.igps not in InternalGPS:
            raise ValueError (f"Internal GPS {self.config.igps} outside valid range, should be {InternalGPS.IGPS.value} or {InternalGPS.IGPS_DATA_OUT.value}")
        if self.config.status not in Status:
            raise ValueError (f"Status {self.config.status} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.status},{self.config.igps}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = LKSet(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
 