#!/usr/bin/env python

# -*- coding:utf8 -*-


import socket

import os

import sys


HOST = 'localhost'

PORT = 7777

ADDR = (HOST,PORT)

BUFSIZE = 4096

videofile = "../Pictures/desert.png"

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

filename = "i.png"


#Bind Socket

serv.bind(ADDR)

serv.listen(5)

conn, addr = serv.accept()

print ('client connected ... ', addr)


#Open the file

#Read and then Send to Client

f=open(filename,'rb')# open file as binary

data=f.read()

print (data,',,,')

exx=conn.sendall(data)

print (exx,'...')

f.flush()

f.close()


#Close the Socket

print ('finished writing file')

conn.close()

serv.close()
