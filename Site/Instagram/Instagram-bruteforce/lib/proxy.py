#Code:BY BLACK
#KodlayapCS
#İnstagram : @eeneskara61


class Proxy(object):

    def __init__(self, proxy):
        self.proxy = proxy 

    @property
    def ip(self):
        return self.proxy['ip']
    
    @property
    def port(self):
        return self.proxy['port']
    
    @property
    def country(self):
        return self.proxy['country']
    
    @property
    def addr(self):
        addr = 'http://{}:{}'.format(self.proxy['ip'], self.proxy['port'])
        return { 'http': addr, 'https': addr } 