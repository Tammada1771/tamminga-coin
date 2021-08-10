import requests
import time

from backend.wallet.wallet import Wallet

BASE_URL = 'http://localhost:5000'


def get_blockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()


def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()


def post_wallet_transact(recipient, amount):
    return requests.post(f'{BASE_URL}/wallet/transact',
                         json={'recipient': recipient,
                               'amount': amount}
                         ).json()


def main():
    start_blockchain = get_blockchain()
    print(f'Start Blockchain: {start_blockchain}')

    recipient = Wallet().address

    post_wallet_transact_1 = post_wallet_transact(recipient, 21)
    print(f'\nPost wallet transact: {post_wallet_transact_1}')

    post_wallet_transact_2 = post_wallet_transact(recipient, 12)
    print(f'\nPost wallet transact 2: {post_wallet_transact_2}')

    time.sleep(1)
    mined_block = get_blockchain_mine()
    print(f'\nMined block: {mined_block}')


if __name__ == '__main__':
    main()
