# -*- coding: utf-8 -*-

import sys
import dbus
import Skype4Py

# ----------------------------------------------------------------------------------------------------
# Fired on attachment status change. Here used to re-attach this script to Skype in case attachment is lost. Just in case.
def OnAttach(status):
    print 'API attachment status: ' + skype.Convert.AttachmentStatusToText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach();

    if status == Skype4Py.apiAttachSuccess:
       print('******************************************************************************');


# ----------------------------------------------------------------------------------------------------
# Fired on chat message status change. 
# Statuses can be: 'UNKNOWN' 'SENDING' 'SENT' 'RECEIVED' 'READ'        

def OnMessageStatus(Message, Status):
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)
        body = "<html><b>" + Message.FromDisplayName + ":</b> " + Message.Body.replace("\n", "<br/>") + "</html>"
        notifications.Notify('skype-visual-notifications', 0, 'someid', 'skype', Message.Chat.FriendlyName, body, [], [], 10000, dbus_interface='org.kde.VisualNotifications')
    if Status == 'SENT':
        print('Myself: ' + Message.Body);


sessionBus = dbus.SessionBus()
notifications = sessionBus.get_object('org.kde.VisualNotifications', '/VisualNotifications')

# ----------------------------------------------------------------------------------------------------
# Creating instance of Skype object, assigning handler functions and attaching to Skype.
skype = Skype4Py.Skype();
skype.OnAttachmentStatus = OnAttach;
skype.OnMessageStatus = OnMessageStatus;

print('******************************************************************************');
print 'Connecting to Skype..'
skype.Attach();

# ----------------------------------------------------------------------------------------------------
# Looping until user types 'exit'
Cmd = '';
while not Cmd == 'exit':
    Cmd = raw_input('');
