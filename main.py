from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from threading import Thread

from jnius import autoclass

# Android permissions
from android.permissions import request_permissions, Permission

# ---- Bluetooth classes ----
BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
UUID = autoclass('java.util.UUID')

# ---- HC-05 DETAILS ----
HC05_MAC = "00:00:13:03:8A:42"
SPP_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")


class MainLayout(BoxLayout):
    socket = None
    stream = None

    def connect_bt(self):
        self.ids.connection_status.text = "Connecting..."
        Thread(target=self._connect_worker, daemon=True).start()

    def _connect_worker(self):
        try:
            adapter = BluetoothAdapter.getDefaultAdapter()

            if not adapter or not adapter.isEnabled():
                self.ids.connection_status.text = "Bluetooth OFF"
                return

            device = adapter.getRemoteDevice(HC05_MAC)
            socket = device.createRfcommSocketToServiceRecord(SPP_UUID)

            adapter.cancelDiscovery()   # VERY IMPORTANT
            socket.connect()            # MUST be background thread

            self.socket = socket
            self.stream = socket.getInputStream()

            self.ids.connection_status.text = "Connected"
            Clock.schedule_interval(self.read_data, 1)

        except Exception as e:
            self.ids.connection_status.text = "Connection Failed"
            print("BT ERROR:", e)

    def read_data(self, dt):
        try:
            if self.stream and self.stream.available() > 0:
                data = self.stream.read()
                msg = chr(data)

                if msg == 'L':
                    self.ids.data_label.text = "Pill Low"
                elif msg == 'S':
                    self.ids.data_label.text = "Stock In"
        except:
            pass

    def reorder_medicine(self):
        import webbrowser
        webbrowser.open("https://www.tata1mg.com")


class PillApp(App):
    def build(self):
        request_permissions([
            Permission.BLUETOOTH_CONNECT,
            Permission.BLUETOOTH_SCAN
        ])
        return Builder.load_file("pillapp.kv")


if __name__ == "__main__":
    PillApp().run()



