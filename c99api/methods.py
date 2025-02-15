def register_methods(self):
    method_names = [func.__name__ for func in globals().values() if callable(func) and func.__name__ != 'register_methods']
    for method_name in method_names:
        method_func = globals()[method_name]
        setattr(self, method_name, method_func)
    return self

"""
Communication Tools
"""
def phonelookup(self, number, json=True):
    return self.perform_request(endpoint_name='phonelookup', number=number, json=json)

def emailvalidator(self, email, json=True):
    return self.perform_request(endpoint_name='emailvalidator', email=email, json=json)

def disposablemailchecker(self, email, json=True):
    return self.perform_request(endpoint_name='disposablemailchecker', email=email, json=json)


"""
Network Tools
"""
def portscanner(self, host, json=True):
    return self.perform_request(endpoint_name='portscanner', host=host, json=json)

def portscanner_port(self, host, port, json=True):
    return self.perform_request(endpoint_name='portscanner_port', host=host, port=port, json=json)

def ping(self, host, json=True):
    return self.perform_request(endpoint_name='ping', host=host, json=json)

def gethostname(self, host, json=True):
    return self.perform_request(endpoint_name='gethostname', host=host, json=json)

def dnschecker(self, url, type, json=True):
    return self.perform_request(endpoint_name='dnschecker', url=url, type=type, json=json)

def dnsresolver(self, host, server, json=True):
    return self.perform_request(endpoint_name='dnsresolver', host=host, server=server, json=json)

def ipvalidator(self, ip, json=True):
    return self.perform_request(endpoint_name='ipvalidator', ip=ip, json=json)

def torchecker(self, ip, json=True):
    return self.perform_request(endpoint_name='torchecker', ip=ip, json=json)

def iplogger(self, action, json=True):
    return self.perform_request(endpoint_name='iplogger', action=action, json=json)

def proxydetector(self, ip, json=True):
    return self.perform_request(endpoint_name='proxydetector', ip=ip, json=json)


"""
Web Tools
"""
def subdomainfinder(self, domain, json=True):
    return self.perform_request(endpoint_name='subdomainfinder', domain=domain, json=json)

def firewalldetector(self, url, json=True):
    return self.perform_request(endpoint_name='firewalldetector', url=url, json=json)

def ip2domains(self, ip, json=True):
    return self.perform_request(endpoint_name='ip2domains', ip=ip, json=json)

def alexarank(self, url, json=True):
    return self.perform_request(endpoint_name='alexarank', url=url, json=json)

def whois(self, domain, json=True):
    return self.perform_request(endpoint_name='whois', domain=domain, json=json)

def createscreenshot(self, url, json=True):
    return self.perform_request(endpoint_name='createscreenshot', url=url, json=json)

def geoip(self, host, json=True):
    return self.perform_request(endpoint_name='geoip', host=host, json=json)

def upordown(self, host, json=True):
    return self.perform_request(endpoint_name='upordown', host=host, json=json)

def reputationchecker(self, url, json=True):
    return self.perform_request(endpoint_name='reputationchecker', url=url, json=json)

def getheaders(self, host, json=True):
    return self.perform_request(endpoint_name='getheaders', host=host, json=json)

def linkbackup(self, url, json=True):
    return self.perform_request(endpoint_name='linkbackup', url=url, json=json)

def urlshortener(self, url, json=True):
    return self.perform_request(endpoint_name='urlshortener', url=url, json=json)


"""
Finance Tools
"""
def bitcoinbalance(self, address, json=True):
    return self.perform_request(endpoint_name='bitcoinbalance', address=address, json=json)

def ethereumbalance(self, address, json=True):
    return self.perform_request(endpoint_name='ethereumbalance', address=address, json=json)

def currency(self, amount, from_currency, to_currency, json=True):
    return self.perform_request(endpoint_name='currency', amount=amount, from_currency=from_currency, to_currency=to_currency, json=json)

def currencyrates(self, source, json=True):
    return self.perform_request(endpoint_name='currencyrates', source=source, json=json)


"""
Miscellaneous 
"""
def randomstringpicker(self, textfile, json=True):
    return self.perform_request(endpoint_name='randomstringpicker', textfile=textfile, json=json)

def dictionary(self, word, json=True):
    return self.perform_request(endpoint_name='dictionary', word=word, json=json)

def definepicture(self, url, json=True):
    return self.perform_request(endpoint_name='definepicture', url=url, json=json)

def synonym(self, word, json=True):
    return self.perform_request(endpoint_name='synonym', word=word, json=json)

def translate(self, text, tolanguage, json=True):
    return self.perform_request(endpoint_name='translate', text=text, tolanguage=tolanguage, json=json)

def randomperson(self, gender, json=True):
    return self.perform_request(endpoint_name='randomperson', gender=gender, json=json)

def youtubedetails(self, videoid, json=True):
    return self.perform_request(endpoint_name='youtubedetails', videoid=videoid, json=json)

def youtubemp3(self, videoid, json=True):
    return self.perform_request(endpoint_name='youtubemp3', videoid=videoid, json=json)

def weather(self, location, json=True):
    return self.perform_request(endpoint_name='weather', location=location, json=json)

def qrgenerator(self, string, size, json=True):
    return self.perform_request(endpoint_name='qrgenerator', string=string, size=size, json=json)

def textparser(self, url, json=True):
    return self.perform_request(endpoint_name='textparser', url=url, json=json)

def passwordgenerator(self, length, include, customlist, json=True):
    return self.perform_request(endpoint_name='passwordgenerator', length=length, include=include, customlist=customlist, json=json)

def randomnumber(self, length, between, json=True):
    return self.perform_request(endpoint_name='randomnumber', length=length, between=between, json=json)

def licensekeygenerator(self, template, amount, json=True):
    return self.perform_request(endpoint_name='licensekeygenerator', template=template, amount=amount, json=json)


"""
Fun and Games
"""
def eitheror(self, json=True):
    return self.perform_request(endpoint_name='eitheror', json=json)

def gif(self, keyword, json=True):
    return self.perform_request(endpoint_name='gif', keyword=keyword, json=json)

