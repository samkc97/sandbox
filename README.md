# sandbox

This repository contains an example Python script (`softub_controller.py`) that demonstrates how to connect a Raspberry Pi 3 Model B to a Softub main board controller via a serial interface.

## Requirements
- Python 3
- `pyserial` library

Install dependencies with:
```bash
pip install pyserial
```

## Usage
Edit the `port` and `baudrate` parameters in `softub_controller.py` to match your hardware configuration, then run:
```bash
python softub_controller.py
```

This will open the serial connection, send a sample `HELLO` command, read any response, and close the connection. Modify the script to add your specific commands.
