from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import RadioGPSMode
from d72.cmds.gm import GM

class GMSet(SerialCommand):

    config = GM()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):        
        if self.config.radioGpsMode not in RadioGPSMode:
            raise ValueError (f"Radio/GPS mode {self.config.radioGpsMode} outside valid range, should be {RadioGPSMode.RADIO_ON_GPS_OFF.value} or {RadioGPSMode.RADIO_OFF_GPS_ON.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.radioGpsMode}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = GMSet(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
