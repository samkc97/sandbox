import serial
import time

class SoftubController:
    """Interface to communicate with a Softub main board controller via serial."""

    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        """Open serial connection to the Softub board."""
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )
        if self.ser.is_open:
            print(f"Connected to {self.port} at {self.baudrate} baud")

    def disconnect(self):
        """Close the serial connection."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Disconnected")

    def send_command(self, cmd: bytes):
        """Send a raw command to the board."""
        if not self.ser or not self.ser.is_open:
            raise RuntimeError("Serial connection is not open")
        self.ser.write(cmd)
        print(f"Sent: {cmd}")
        time.sleep(0.1)  # small delay

    def read_response(self):
        """Read any available data from the board."""
        if not self.ser or not self.ser.is_open:
            raise RuntimeError("Serial connection is not open")
        response = self.ser.readline()
        print(f"Received: {response}")
        return response

def main():
    controller = SoftubController()
    try:
        controller.connect()
        # Example handshake. Replace with actual command for your board.
        controller.send_command(b'HELLO\r\n')
        controller.read_response()

        # TODO: Add more interactions with the board here.
    finally:
        controller.disconnect()

if __name__ == "__main__":
    main()
