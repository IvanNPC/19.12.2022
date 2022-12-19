from socket import *
import RPi.GPIO as GPIO
import pygame.mixer
import time
import sys
import select


gpio_n     = (2,3,4,17,27,  22,10,9,11,5,  6,13,19,26,18,  23,24,25,8,7,  12,16,20,21)
host = '192.168.100.100'
port = 11121
addr = (host,port)
UDP_IP = "127.0.0.1"
UDP_PORT = 11120


in_socket = socket(AF_INET,SOCK_DGRAM)
in_socket.bind(("", UDP_PORT)) 

out_socket = socket(AF_INET,SOCK_DGRAM)



GPIO.setmode(GPIO.BCM)


#for n in range(0, 23):
#    GPIO.setup(gpio_n[n], GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(gpio_n[0], GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(gpio_n[1], GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(gpio_n[2], GPIO.OUT)
GPIO.setup(gpio_n[3], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[4], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[5], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[6], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[7], GPIO.OUT)
GPIO.setup(gpio_n[8], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[9], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[10], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[11], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[12], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[13], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[14], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[15], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[16], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[17], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[18], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[19], GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(gpio_n[20], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(gpio_n[21], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_n[22], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#in_socket.setblocking(0);

#pygame.mixer.init(44000,-16,1,1024)
#audio1 = pygame.mixer.Sound("match1.wav")
#audio2 = pygame.mixer.Sound("match2.wav")
#channel1 = pygame.mixer.Channel(1)
#channel2 = pygame.mixer.Channel(2)

p = GPIO.PWM(12,2500)  #GPIO12
input_state = 0
ictn=0
time_piu=0
if 0==1:
    input_state |= GPIO.input(gpio_n[0])<<gpio_n[0];
    input_state |= GPIO.input(gpio_n[1])<<gpio_n[1];
    input_state |= GPIO.input(gpio_n[2])<<gpio_n[2];
#    input_state |= GPIO.input(gpio_n[3])<<gpio_n[3];  (17)
    input_state |= GPIO.input(gpio_n[4])<<gpio_n[4];
    input_state |= GPIO.input(gpio_n[5])<<gpio_n[5];
    input_state |= GPIO.input(gpio_n[6])<<gpio_n[6];
#    input_state |= GPIO.input(gpio_n[7])<<gpio_n[7];  (9)
    input_state |= GPIO.input(gpio_n[8])<<gpio_n[8];
    input_state |= GPIO.input(gpio_n[9])<<gpio_n[9];
    input_state |= GPIO.input(gpio_n[10])<<gpio_n[10];
#    input_state |= GPIO.input(gpio_n[11])<<gpio_n[11]; (13)
    input_state |= GPIO.input(gpio_n[12])<<gpio_n[12];
    input_state |= GPIO.input(gpio_n[13])<<gpio_n[13];
    input_state |= GPIO.input(gpio_n[14])<<gpio_n[14];
    input_state |= GPIO.input(gpio_n[15])<<gpio_n[15];
    input_state |= GPIO.input(gpio_n[16])<<gpio_n[16];
    input_state |= GPIO.input(gpio_n[17])<<gpio_n[17];
    input_state |= GPIO.input(gpio_n[18])<<gpio_n[18];
    input_state |= GPIO.input(gpio_n[19])<<gpio_n[19];
#    input_state |= GPIO.input(gpio_n[20])<<gpio_n[20]; (12)
#    input_state |= GPIO.input(gpio_n[21])<<gpio_n[21]; (16)
    input_state |= GPIO.input(gpio_n[22])<<gpio_n[22];

while True:
    input_state &= 0x00000000
    input_state |= 0x80000000
#    for i in range(0, 23):
#        input_state |= GPIO.input(gpio_n[i])<<gpio_n[i];


        



    if (ictn&2) == 0:
        input_state |= 0<<9;
    else:
        input_state |= 1<<9;


#    if (ictn&2) == 0:
#        input_state &= 0x00038000^0xFFFFFFFF
#        input_state |= GPIO.input(24)<<16;
#        input_state |= GPIO.input(25)<<17;
#    else:
#        input_state &= 0x00007000^0xFFFFFFFF
#        input_state |= 1<<9;
#        input_state |= GPIO.input(24)<<13;
#        input_state |= GPIO.input(25)<<14;
    
    in_socket.settimeout(0.03)
    try:
        data,sz = in_socket.recvfrom(1024)
        if data[0] == 0x30:
            p.stop()
#            out_socket.sendto(data,addr)
        if data[0] == 0x31:
            p.ChangeFrequency(2500.0)
            p.start(50.0)
            GPIO.output(4, GPIO.HIGH)
#            channel1.play(audio1)
        else:
            GPIO.output(4, GPIO.LOW)
        if data[0] == 0x32:
            p.ChangeFrequency(33.0)
            p.start(5.0)
#            channel1.play(audio2) 
        if data[0] == 0x33:
            p.ChangeFrequency(500.0)
            p.start(5.0)
            time_piu=0.01;


            
    except:
        time.sleep(0.02)

         

#    GPIO.output(12, GPIO.LOW)
  
#    GPIO.output(12, GPIO.HIGH)
    while (time_piu>=0.01 and time_piu<=1):
        time.sleep(0.001)
        time_piu+=0.001
        if (time_piu<=0.2):
            p.ChangeFrequency(500.0+400.0*time_piu/0.2)
        else:
            if (time_piu<=0.6):
                p.ChangeFrequency(500.0+400.0+100*(time_piu-0.2)/0.8)
#               p.ChangeFrequency(random.uniform(300,3000))
                              
    if (time_piu>=1):
        time_piu=0
        p.stop()
    

    bdata = input_state.to_bytes(4,byteorder='little')
    ictn=ictn+1
    if (ictn&1) == 0:
        try:
            out_socket.sendto(bdata,addr)
        except:
            time.sleep(0.02)
    if (ictn&2) == 0:
        GPIO.output(9, GPIO.LOW)
    else:
        GPIO.output(9, GPIO.HIGH)

