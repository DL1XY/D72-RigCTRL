#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.ae_get import AEGet
from d72.cmds.id_get import IDGet
from d72.cmds.fv_get import FVGet
from d72.cmds.cs_get import CSGet

interface = Builder.load_string('''

<RigInterface>:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                id: enable_button
                text: 'Connect TH-D72'
                disabled: False
                on_release:
                    root.enable()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
            Button:
                id: disable_button
                text: 'Disconnect TH-D72'
                disabled: True
                on_release:
                    root.disable()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Label:
                text: "Model"
            Label:
                text: str(root.model)
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Label:
                text: 'Serial'
            Label:
                text: str(root.serial)
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Label:
                text: 'Firmware MAIN'
            Label:
                text: str(root.firmware)
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Label:
                text: 'Callsign'
            Label:
                text: str(root.callsign)            
''')
                                
class RigInterface(BoxLayout):

    model = StringProperty("TH-D72")
    serial = StringProperty("ABC")
    firmware= StringProperty("firmware")
    callsign = StringProperty("DL1XY")

    def enable(self):
        self.rcv = SerialReceiver()
        self.inv = SerialInvoker()
        # Model
        self.cmd_id_get = IDGet(self.rcv)
        self.inv.store_command(self.cmd_id_get)   

        # Radio Serial
        self.cmd_ae_get = AEGet(self.rcv)
        self.inv.store_command(self.cmd_ae_get)   
        
        # Firmware MAIN
        self.cmd_fv_get = FVGet(self.rcv)
        self.inv.store_command(self.cmd_fv_get)   
        
        # Callsign
        self.cmd_cs_get = CSGet(self.rcv)
        self.inv.store_command(self.cmd_cs_get) 
        self.sendCmds()


    def disable(self):
        self.rcv.close()
        
    def sendCmds(self):        
        self.rcvd = self.inv.execute_commands()
        self.model = self.rcvd.get('ID')
        self.serial = self.rcvd.get('AE')
        self.firmware = self.rcvd.get('FV')  
        self.callsign = self.rcvd.get('CS')    
    
class RigApp(App):
   
    def build(self):
        return RigInterface()


if __name__ == '__main__':
    RigApp().run()