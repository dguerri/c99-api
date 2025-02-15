# Client for handling responses from API and outputting in desired format

import requests
from .methods import register_methods

@register_methods

class EndpointClient:

    base_url = None
    key = None
    session = None
    json = None
    
    def __init__(self, user_agent='python-c99api', base_url='https://api.c99.nl', json=False, key=None):
        self.base_url = base_url
        self.json = json
        self.key = key
        self.session = requests.Session()

        self.session.headers.update({'User-Agent': user_agent})

    def fetch_endpoint(self, endpoint_name, json=True, **kwargs):
        if not self.key:
            raise ValueError("API key not set. Use c99_api.key = 'your_api_key'")
        
        json_query = '&json' if json else ''
        
        endpoint_list = {
        'phonelookup': self.base_url + f'/phonelookup?key={self.key}&number={kwargs.get("number")}{json_query}',
        'emailvalidator': self.base_url + f'/emailvalidator?key={self.key}&email={kwargs.get("email")}{json_query}',
        'disposablemailchecker': self.base_url + f'/disposablemailchecker?key={self.key}&email={kwargs.get("email")}{json_query}',
        'portscanner': self.base_url + f'/portscanner?key={self.key}&host={kwargs.get("host")}{json_query}',
        'portscanner_port': self.base_url + f'/portscanner?key={self.key}&host={kwargs.get("host")}&port={kwargs.get("port")}{json_query}',
        'ping': self.base_url + f'/ping?key={self.key}&host={kwargs.get("host")}{json_query}',
        'gethostname': self.base_url + f'/gethostname?key={self.key}&host={kwargs.get("host")}{json_query}',
        'dnschecker': self.base_url + f'/dnschecker?key={self.key}&url={kwargs.get("url")}&type={kwargs.get("type")}{json_query}',
        'dnsresolver': self.base_url + f'/dnsresolver?key={self.key}&host={kwargs.get("host")}&server={kwargs.get("server")}{json_query}',
        'ipvalidator': self.base_url + f'/ipvalidator?key={self.key}&ip={kwargs.get("ip")}{json_query}',
        'torchecker': self.base_url + f'/torchecker?key={self.key}&ip={kwargs.get("ip")}{json_query}',
        'iplogger': self.base_url + f'/iplogger?key={self.key}&action={kwargs.get("action")}{json_query}',
        'proxydetector': self.base_url + f'/proxydetector?key={self.key}&ip={kwargs.get("ip")}{json_query}',
        'subdomainfinder': self.base_url + f'/subdomainfinder?key={self.key}&domain={kwargs.get("domain")}{json_query}',
        'firewalldetector': self.base_url + f'/firewalldetector?key={self.key}&url={kwargs.get("url")}{json_query}',
        'ip2domains': self.base_url + f'/ip2domains?key={self.key}&ip={kwargs.get("ip")}{json_query}',
        'alexarank': self.base_url + f'/alexarank?key={self.key}&url={kwargs.get("url")}{json_query}',
        'whois': self.base_url + f'/whois?key={self.key}&domain={kwargs.get("domain")}{json_query}',
        'createscreenshot': self.base_url + f'/createscreenshot?key={self.key}&url={kwargs.get("url")}{json_query}',
        'geoip': self.base_url + f'/geoip?key={self.key}&host={kwargs.get("host")}{json_query}',
        'upordown': self.base_url + f'/upordown?key={self.key}&host={kwargs.get("host")}{json_query}',
        'reputationchecker': self.base_url + f'/reputationchecker?key={self.key}&url={kwargs.get("url")}{json_query}',
        'getheaders': self.base_url + f'/getheaders?key={self.key}&host={kwargs.get("host")}{json_query}',
        'linkbackup': self.base_url + f'/linkbackup?key={self.key}&url={kwargs.get("url")}{json_query}',
        'urlshortener': self.base_url + f'/urlshortener?key={self.key}&url={kwargs.get("url")}{json_query}',
        'bitcoinbalance': self.base_url + f'/bitcoinbalance?key={self.key}&address={kwargs.get("address")}{json_query}',
        'ethereumbalance': self.base_url + f'/ethereumbalance?key={self.key}&address={kwargs.get("address")}{json_query}',
        'currency': self.base_url + f'/currency?key={self.key}&amount={kwargs.get("amount")}&from={kwargs.get("from")}&to={kwargs.get("to")}{json_query}',
        'currencyrates': self.base_url + f'/currencyrates?key={self.key}&source={kwargs.get("source")}{json_query}',
        'randomstringpicker': self.base_url + f'/randomstringpicker?key={self.key}&textfile={kwargs.get("textfile")}{json_query}',
        'dictionary': self.base_url + f'/dictionary?key={self.key}&word={kwargs.get("word")}{json_query}',
        'definepicture': self.base_url + f'/definepicture?key={self.key}&url={kwargs.get("url")}{json_query}',
        'synonym': self.base_url + f'/synonym?key={self.key}&word={kwargs.get("word")}{json_query}',
        'translate': self.base_url + f'/translate?key={self.key}&text={kwargs.get("text")}&tolanguage={kwargs.get("tolanguage")}{json_query}',
        'randomperson': self.base_url + f'/randomperson?key={self.key}&gender={kwargs.get("gender")}{json_query}',
        'youtubedetails': self.base_url + f'/youtubedetails?key={self.key}&videoid={kwargs.get("videoid")}{json_query}',
        'youtubemp3': self.base_url + f'/youtubemp3?key={self.key}&videoid={kwargs.get("videoid")}{json_query}',
        'weather': self.base_url + f'/weather?key={self.key}&location={kwargs.get("location")}{json_query}',
        'qrgenerator': self.base_url + f'/qrgenerator?key={self.key}&string={kwargs.get("string")}&size={kwargs.get("size")}{json_query}',
        'textparser': self.base_url + f'/textparser?key={self.key}&url={kwargs.get("url")}{json_query}',
        'passwordgenerator': self.base_url + f'/passwordgenerator?key={self.key}&length={kwargs.get("length")}&include={kwargs.get("include")}&customlist={kwargs.get("customlist")}{json_query}',
        'randomnumber': self.base_url + f'/randomnumber?key={self.key}&length={kwargs.get("length")}&between={kwargs.get("between")}{json_query}',
        'licensekeygenerator': self.base_url + f'/licensekeygenerator?key={self.key}&template={kwargs.get("template")}&amount={kwargs.get("amount")}{json_query}',
        'eitheror': self.base_url + f'/eitheror?key={self.key}{json_query}',
        'gif': self.base_url + f'/gif?key={self.key}&keyword={kwargs.get("keyword")}{json_query}'
        }

        url_template = endpoint_list[endpoint_name]
        result_endpoint = url_template.format(**kwargs)
        return result_endpoint

    def perform_request(self, endpoint_name, json=True, **kwargs):
        url = self.fetch_endpoint(endpoint_name=endpoint_name, json=json, **kwargs)
        response = self.session.get(url)
        return response.json() if json else response.text
    
    @classmethod
    def list_methods(cls):

        methods_list = [
            'phonelookup',
            'emailvalidator',
            'disposablemailchecker',
            'portscanner',
            'portscanner_port',
            'ping',
            'gethostname',
            'dnschecker',
            'dnsresolver',
            'ipvalidator',
            'torchecker',
            'iplogger',
            'proxydetector',
            'subdomainfinder',
            'firewalldetector',
            'ip2domains',
            'alexarank',
            'whois',
            'createscreenshot',
            'geoip',
            'upordown',
            'reputationchecker',
            'getheaders',
            'linkbackup',
            'urlshortener',
            'bitcoinbalance',
            'ethereumbalance',
            'currency',
            'currencyrates',
            'randomstringpicker',
            'dictionary',
            'definepicture',
            'synonym',
            'translate',
            'randomperson',
            'youtubedetails',
            'youtubemp3',
            'weather',
            'qrgenerator',
            'textparser',
            'passwordgenerator',
            'randomnumber',
            'licensekeygenerator',
            'eitheror',
            'gif'
        ]

        return methods_list
        
