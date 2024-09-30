import serial
import serial.tools.list_ports as port_list


port = "COM3"
baudrate = 9600
serialPort = serial.Serial(port=port, baudrate=baudrate,
                                bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
serialString = ""
# serialPort.write(bytes.fromhex("A551F6"))
serialPort.write(bytes.fromhex("A555FA"))

while True:
    try:
        # serialPort.reset_input_buffer()
        # serialPort.reset_output_buffer()
        # serialString = serialPort.read(10).hex()
        serialString = serialPort.read()
        print(serialString)
    except KeyboardInterrupt:
        break

serialPort.close()
