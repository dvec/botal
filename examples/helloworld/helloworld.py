from botal.datatypes import Message
from botal.handler import Handler
from botal.messengesrs import Terminal, Telegram

# This is handler for the terminal
handler = Handler([Terminal()])


# Or you can use the handler for telegram
# handler = Handler([Telegram(token='Your telegram bot token')])

# Or for terminal and telegram both
# handler = Handler([Terminal(), Telegram(token='Your telegram bot token')])


# This annotation indicates that this function will be called when message is received from a new user
@handler.handler
def on_message(user):
    # user_info is an instance of the UserInfo object
    while True:
        # When user will write new message, it will be passed into this generator by using generator.send
        # message is an instance of the Message object
        message = yield
        # You can send message to the user by yielding it
        user.send(Message('You typed: "{}"'.format(message.text)))


if __name__ == '__main__':
    # Finally, we need to run handler
    handler.run_handler()

# Now run this code and type something in terminal. You will see something like this:
# Hello!
# You typed: "Hello!"
