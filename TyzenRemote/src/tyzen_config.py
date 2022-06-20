import json
import os.path


class Config:
    config_location = os.path.dirname(__file__) + "/../assets/config.json"

    def __init__(self):
        self.__config = json.load(open(self.config_location))

    def get_token(self):
        return self.__config["token"]

    def set_token(self, token: str):
        self.__config["token"] = token
        self.save()

    def get_mac(self):
        return self.__config["mac"]

    def get_host(self):
        return self.__config["host"]

    def get_api_port(self):
        return self.__config["api_port"]

    def get_wol_port(self):
        return self.__config["wol_port"]

    def get_api_location(self):
        return self.__config["api_location"]

    def set_mac(self, mac: str):
        self.__config["mac"] = mac
        self.save()

    def set_host(self, host: str):
        self.__config["host"] = host
        self.save()

    def set_api_port(self, api_port: int):
        self.__config["api_port"] = api_port
        self.save()

    def set_wol_port(self, wol_port: int):
        self.__config["wol_port"] = wol_port
        self.save()

    def save(self):
        file = open(self.config_location, "w+")
        file.write(json.dumps(self.__config))
