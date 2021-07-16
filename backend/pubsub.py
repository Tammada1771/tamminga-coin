import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-02d71e0a-e5d0-11eb-bc98-fa4b4b21bdc4'
pnconfig.publish_key = 'pub-c-1a894079-7eb0-4686-9634-c22a2a4a9a5f'

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f'\n-- Channel: {message_object.channel} || Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain netowork
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish a message object to the channel

        """

        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
