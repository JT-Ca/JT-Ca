import mechanize
import http.cookiejar
import random
import urllib.request

class hideB(mechanize.Browser):

	def __init__(self, proxies = [], user_agents = []):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		self.set_handle_equiv(False)
		self.proxies = proxies
		self.user_agents = user_agents + ['Mozilla/4.0 ', 'Firefox/6.01', 'ExactSearch', 'Nokia7110/1.0']
		self.cookie_jar = http.cookiejar.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()
	
	def clear_cookies(self):
		self.cookie_jar = http.cookiejar.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
	
	def change_user_agent(self):
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', (self.user_agents[index]))]
		
	def change_proxy(self):
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies({'http', self.proxies[index]})
			
	def anonymize(self, sleep = False):
		self.clear_cookies()
		self.change_user_agent()
		self.change_proxy()
		
		if sleep:
			time.sleep(60)

