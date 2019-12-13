import json;
from random import randint;
from time import sleep;
from selenium import webdriver;
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary;
from selenium.webdriver.firefox.options import Options;

class Generate():
	
	def __init__(self, sleep = 0.2):
		self.hash = 'Qq1Ww2Ee3Rr4Tt5Yy6Uu7Ii8Oo9Pp0AaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm';
		self.sleep = sleep;

	def isValidGift(self, url):
		# binary = FirefoxBinary('/usr/lib/firefox/firefox')
		with open('agents.json') as json_data:
		    agents = json.load(json_data)
		    json_data.close();

		n = randint(0, len(agents) - 1);
		options = Options();
		options.add_argument('--headless');
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", agents[n]);
		print('\033[1;30mSet useragent - %s\033[1;30m' % agents[n]);
		driver = webdriver.Firefox(options=options)
		print('\033[1;32mFirefox launched\033[1;32m')
		driver.implicitly_wait(4)
		driver.get(url)
		el = driver.find_elements_by_xpath("//*[contains(text(), 'Gift Code Invalid')]")
		if (len(el) == 0):
			print("\033[1;32m%s - valid gift\033[1;32m" % url);
			log = open('codes.log', 'w');
			log.write(url);
			log.close();
		else:
			print("\033[1;35m%s\033[1;35m - \033[1;31minvalid gift\033[1;31m" % url);
		driver.quit();
		print('\033[1;31mFirefox killed\033[1;31m')
	def gen(self):
		length = 16;
		str = '';
		print("\033[1;33mGenerate gift code...\033[1;33m")
		while (len(str) != length):
			n = randint(0, len(self.hash) - 1);
			str += self.hash[n];
			sleep(self.sleep);
		url = 'https://discord.gift/' + str;
		print('\033[1;33mSend request...\033[1;33m');
		self.isValidGift(url);
		self.gen();

Generate().gen();