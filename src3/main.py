# just use itchat pacakge

import os
import itchat
from itchat.content import *

## entry point here

#itchat.auto_login()
#itchat.send('Hello, filehelper', toUserName='filehelper')

concation_begin = False
concation_end = False
file_list = []

def try_concate_files(mylist):
    idx = 0
    fd = open('list.txt', 'w')
    for it in mylist:
        cmds = 'ffmpeg -i "%s" -acodec pcm_s16le -ac 2 -ar 44100 y%d.wav' %(it, idx)
        print("the execute commands:\n%s\n" %(cmds))
        os.system(cmds)
        cmds = 'lame -b128 y%d.wav y%d.mp3' %(idx, idx)
        os.system(cmds)
        fd.write("file 'y%d.mp3'\n" %(idx))
        idx = idx + 1

    fd.close()
    cmds = 'ffmpeg -f concat -i list.txt -c copy yyx.mp3'
    os.system(cmds)

    return 'yyx.mp3'

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print('%s: %s' % (msg.type, msg.text))
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    if msg.text == 'a':
        msg.user.send("Please send your files, end with 'b'")
        concation_begin = True

    if msg.text == 'b':
        msg.user.send("please wait...")
        result = try_concate_files(file_list)
        print("will send back with %s" %(result))
        msg.user.send_file(result)
        cmds = 'rm *.m4a'
        os.system(cmds)
        cmds = 'rm *.wav'
        os.system(cmds)
        cmds = 'rm *.mp3'
        os.system(cmds)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print("will download %s" %(msg.fileName))
    msg.download(msg.fileName)
    file_list.append(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

itchat.auto_login(enableCmdQR=2)
itchat.run()
