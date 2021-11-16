import requests
from jsonrpcclient import request
from hm_pyhelper.miner_json_rpc.exceptions import MinerConnectionError,\
                                                  MinerMalformedURL,\
                                                  MinerRegionUnset


class Client(object):

    def __init__(self, url='http://helium-miner:4467'):
        self.url = url

    def __fetch_data(self, method, **kwargs):
        try:
            response = request(self.url, method, **kwargs)
            return response.data.result
        except requests.exceptions.ConnectionError as e:
            return str(e)
        except requests.exceptions.MissingSchema as e:
            return str(e)
        except ConnectionRefusedError as e:
            return str(e)
        except Exception as e:
            return str(e)

    def get_height(self):
        try:
            return self.__fetch_data('info_height')
        except MinerConnectionError:
            raise
        except MinerMalformedURL as e:
            raise MinerConnectionError(e)

    def get_region(self):
        region = self.__fetch_data('info_region')
        if not region.get('region'):
            raise MinerRegionUnset(
                "Miner at %s does not have an asserted region"
                % self.url
            )
        return region

    def get_summary(self):
        return self.__fetch_data('info_summary')

    def get_peer_addr(self):
        return self.__fetch_data('peer_addr')

    def get_peer_book(self):
        try:
            return self.__fetch_data('peer_book', addr='self')
        except MinerConnectionError:
            raise
        except MinerMalformedURL as e:
            raise MinerConnectionError(e)

    def get_firmware_version(self):
        summary = self.get_summary()
        return summary.get('firmware_version')
