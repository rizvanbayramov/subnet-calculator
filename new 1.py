# -*- coding: utf-8 -*-
import paramiko
import time


ip_address = raw_input('IP address: ')
username = raw_input ('Username: ')
password = raw_input ('Password: ')
filename = raw_input ('Path to commands file: ')


"""
def commands_func (file):
    file_open = open(file, 'r')
    lines = file_open.readlines()	
    for i in lines:
        return i
"""
	
def output_file(file):
    file_open = open("outputs.txt" , 'w')
    file_open.truncate() # Truncating the commands outputs file
    file_open.write(file)
    file_open.close()


def ssh (Ip, User, Password):
    print 'You are going to connect to network device via SSH.'
    print 'Please enter necessary information to connect:'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Ip,username=User,password=Password)
    print "Successful connection to ", Ip
    
    remote_connection = ssh.invoke_shell()
    file_open = open(filename, 'r')
    lines = file_open.readlines()	
    for commands in lines:
        remote_connection.send(commands)
    time.sleep(1)
    output = remote_connection.recv(65535)
    output_file (output)
    print "Commands executed, script completed..."
    ssh.close

ssh (ip_address, username, password)