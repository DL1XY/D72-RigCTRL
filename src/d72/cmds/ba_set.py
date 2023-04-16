from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import BatteryType
from d72.cmds.ba import BA

class BASet(SerialCommand):

    config = BA()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.batteryType not in BatteryType:
            raise ValueError (f"Battery type {self.config.batteryType} outside valid range, should be {BatteryType.LITHIUM.value} or {BatteryType.ALKALINE.value}")
        self._receiver.action(f"{self.config.cmd} {self.config.batteryType}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = BASet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
