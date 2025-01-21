
import io
import json
import os
import requests


class Webhook:
    """
    任意の Webhook でメッセージを送信するクラス
    """

    def __init__(self, webhook_url:str):
        """
        Args:
            webhook_url (str): Webhook の URL
        """

        self.webhook_url = webhook_url


    def sendMessage(self, message:dict, image_path:str=None) -> dict:
        """
        Webhook でメッセージを送信する

        Args:
            message (str): 送信するメッセージの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: ステータスコードとエラーメッセージが入った辞書
        """

        # Webhook を送信
        response = requests.post(self.webhook_url, json=message)

        # 失敗した場合はエラーメッセージを取得
        if response.status_code != 200 and response.status_code != 204:
            message = response.json()['message'] + f' (Code: {response.json()["code"]})'
        else:
            message = 'Success'

        # ステータスコードとエラーメッセージを返す
        return {
            'status': response.status_code,
            'message': message,
        }
