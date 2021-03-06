import time
import fcntl
from struct import *

PWM_FILE = '/dev/pwmtimer'

pwm_pin = 6
pwm_value = 128
pwm_freq = 150

# Set frequency
with open(PWM_FILE, 'wb') as f:
	pwm_struct = pack('iiiI', pwm_pin, 0, 0, pwm_freq)
	fcntl.ioctl(f, 0x107, pwm_struct)


# Set duty cycle
with open(PWM_FILE, 'wb') as f:
	pwm_struct = pack('ii', pwm_pin, pwm_value)
	fcntl.ioctl(f, 0x106, pwm_struct)

#time.sleep(2)

# Stop PWM
#with open(PWM_FILE, 'wb') as f:
#	pwm_struct = pack('ii', pwm_pin, 0)
#	fcntl.ioctl(f, 0x106, pwm_struct)
