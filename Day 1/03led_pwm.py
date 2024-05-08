import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_pin=5

GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(0)

while True:
    duty=int(input("Enter Brightness (0to 100): "))
    pwm_led.ChangeDutyCycle(duty)