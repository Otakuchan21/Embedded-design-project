import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# MPU6050 address, 0x68(104)
# Select PWR_MGMT_1 register, 0x6B(107)
#		0x01(1)	Reset device
bus.write_byte_data(0x68, 0x6B, 0x01)

# MPU6050 address, 0x68(104)
# Select Configuration register, 0x1A(26)
#		0x00(00)	FS_SEL = 0, Accelerometer Full Scale Range = +/- 2g
bus.write_byte_data(0x68, 0x1A, 0x00)

# MPU6050 address, 0x68(104)
# Select Gyroscopes Configuration register, 0x1B(27)
#		0x00(00)	FS_SEL = 0, Gyroscope Full Scale Range = +/- 250 degrees/sec
bus.write_byte_data(0x68, 0x1B, 0x00)

while True:
    # MPU6050 address, 0x68(104)
    # Read data back from 0x3B(59), 14 bytes
    data = bus.read_i2c_block_data(0x68, 0x3B, 14)

    # Convert the data
    # Accelerometer
    xAcc = data[0] * 256 + data[1]
    if xAcc > 32767 :
        xAcc -= 65536

    yAcc = data[2] * 256 + data[3]
    if yAcc > 32767 :
        yAcc -= 65536

    zAcc = data[4] * 256 + data[5]
    if zAcc > 32767 :
        zAcc -= 65536

    # Gyroscope
    xGyro = data[8] * 256 + data[9]
    if xGyro > 32767 :
        xGyro -= 65536

    yGyro = data[10] * 256 + data[11]
    if yGyro > 32767 :
        yGyro -= 65536

    zGyro = data[12] * 256 + data[13]
    if zGyro > 32767 :
        zGyro -= 65536

    # Output data to screen
    print("Accelerometer: {0} {1} {2}".format(xAcc, yAcc, zAcc))
    print("Gyroscope: {0} {1} {2}".format(xGyro, yGyro, zGyro))
    # Sleep for some time
    time.sleep(0.1)
