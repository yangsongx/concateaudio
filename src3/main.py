# just use itchat pacakge

import itchat

## entry point here

#itchat.auto_login()
#itchat.send('Hello, filehelper', toUserName='filehelper')


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login(enableCmdQR=2)
itchat.run()
