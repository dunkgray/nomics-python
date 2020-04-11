import requests

from .api import API

class Currencies(API):
    def get_currencies(self, ids = None, interval = None, convert = None, include_transparency = False):
        '''
        Returns price, volume, market cap, and rank for all currencies

        :param  [str]   ids:                    Comma separated list of Nomics Currency IDs 
                                                to filter result rows. Optional

        :param  [str]   interval:               Comma separated time interval of the ticker(s). 
                                                Default is 1d,7d,30d,365d,ytd

        :param  str     convert:                Currency to quote ticker price, market cap, and volume values. 
                                                May be a Fiat Currency or Cryptocurrency. 
                                                Default is USD.     
        :param  bool    include-transparency:   Whether to include Transparent Volume information for currencies. 
                                                Default is false. Only available to paid API plans
        '''

        url = self.client.get_url('currencies/ticker')
        params = {
            'ids': ids,
            'interval': interval,
            'convert': convert,
            'include-transparency': include_transparency
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_metadata(self, ids = None, attributes = None):
        '''
        Returns  all the currencies and their metadata that Nomics supports

        :param  [str]   ids:        Comma separated list of Nomics Currency IDs 
                                    to filter result rows. Optional

        :param  [str]   attributes: Comma separated list of currency attributes to filter result columns
                                    Optional
        '''

        url = self.client.get_url('currencies')
        params = {
            'ids': ids,
            'attributes': attributes
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text