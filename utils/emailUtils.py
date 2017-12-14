import base64

from email.mime.text import MIMEText

def CreateMessage(to, sender, subject, message_text):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode("utf-8"))}

def send_message(service, user_id, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    message = (service.users().messages().send(userId=user_id, body=message.decode("utf-8")).execute())
    # print 'Message Id: %s' % message['id'] "uncomment this line to get
                                            #message id of the sent message"
    return message
