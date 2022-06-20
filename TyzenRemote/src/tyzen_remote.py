import json
import ssl
import time

import wakeonlan
import websocket

from TyzenRemote.src.tyzen_config import Config


class Remote:

    def __init__(self, config: Config):
        self.__config = config
        self.__url = f"wss://{config.get_host()}:{config.get_api_port()}/{config.get_api_location()}channels/samsung.remote.control"
        self.__connection = None

    def connect(self):
        self.__connection = websocket.create_connection(f"{self.__url}?token={self.__config.get_token()}",
                                                        sslopt={"cert_reqs": ssl.CERT_NONE})

    def issue_token(self):
        connection = websocket.create_connection(self.__url, sslopt={"cert_reqs": ssl.CERT_NONE})
        response = json.loads(connection.recv())
        self.__config.set_token(response["data"]["token"])
        connection.close()

    def turn_on(self):
        wakeonlan.send_magic_packet(self.__config.get_mac(), ip_address=self.__config.get_host(),
                                    port=self.__config.get_wol_port())

    def send_key(self, key, times):
        if not hasattr(Key, key):
            raise Exception("Error: Key is not valid!")
        if self.__connection is None:
            raise Exception("Error: There is no connection established!")

        data = json.dumps({
            'method': "ms.remote.control",
            'params': {
                'Cmd': 'Click',
                'DataOfCmd': key,
                'Option': 'false',
                'TypeOfRemote': 'SendRemoteKey'
            }
        })
        for i in range(times):
            self.__connection.send(data)
            time.sleep(0.5)


class Key:
    KEY_POWER = "KEY_POWER"
    KEY_UP = "KEY_UP"
    KEY_DOWN = "KEY_DOWN"
    KEY_LEFT = "KEY_LEFT"
    KEY_RIGHT = "KEY_RIGHT"
    KEY_CHUP = "KEY_CHUP"
    KEY_CHDOWN = "KEY_CHDOWN"
    KEY_ENTER = "KEY_ENTER"
    KEY_RETURN = "KEY_RETURN"
    KEY_CH_LIST = "KEY_CH_LIST"
    KEY_MENU = "KEY_MENU"
    KEY_SOURCE = "KEY_SOURCE"
    KEY_TOOLS = "KEY_TOOLS"
    KEY_INFO = "KEY_INFO"
    KEY_RED = "KEY_RED"
    KEY_GREEN = "KEY_GREEN"
    KEY_YELLOW = "KEY_YELLOW"
    KEY_BLUE = "KEY_BLUE"
    KEY_VOLUP = "KEY_VOLUP"
    KEY_VOLDOWN = "KEY_VOLDOWN"
    KEY_PLAY = "KEY_PLAY"
    KEY_PAUSE = "KEY_PAUSE"
    KEY_MUTE = "KEY_MUTE"
