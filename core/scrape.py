# Import required modules
import os
import sys
import re
import time
import string
import random
import requests
import bs4

# Define the scrape() class
class scrape(object):
	# Class: scrape()
	# Purpose: Scrape Google
	# Functions: __init__(), get_page(), get_urls()
	
	# Define the __init__() function
	def __init__(self, query, pages, proxy):
		# Function: __init__()
		# Purpose: Initialize the scraper
		
		# Make sure a query was specified
		if query == None:
			# Raise an exception
			raise Exception("[E] Query must be specified with -q or --query!")
			
		# Dump everything to self
		self.query = query
		self.pages = pages
		self.proxy = proxy
		
	# Define the get_page function
	def get_page(self, query, page_id, proxy):
		# Function: get_page()
		# Purpose: Get the raw HTML of the specified result page
		
		# Set the url
		url = "https://www.google.com/search"
		
		# Set the user agents
		user_agents = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:26.0) Gecko/20100101 Firefox/45.0.2",
		               "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136",
		               "Mozilla/5.0 (X11; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/45.0.2",
		               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/9.0.3 ",)
		
		# Set the scrape paramaters and headers
		scrape_params = {"q": query, "start": str(page_id)}
		scrape_headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
		
		# Determine if proxy was used
		if proxy == None:
			# No proxy was used
			# Attempt to get the raw HTML
			try:
				raw_html = requests.get(url, params = scrape_params, headers = scrape_headers)
			except:
				# Raise an exception
				raise Exception("[E] Unable to retrieve raw HTML!")
				
		else:
			# Proxy was used
			# Split the string
			proxy_type, address = proxy.split("%")
			
			# Set the proxy dictionary
			proxy_dict = {proxy_type: address}
			
			# Attempt to get the raw HTML
			try:
				raw_html = requests.get(url, params = scrape_params, headers = scrape_headers, proxies = proxy_dict)
			except:
				# Raise an exception
				raise Exception("[E] Unable to retrieve raw HTML!")

		# Return the raw HTML
		return raw_html
		
	# Define the get_urls() function
	def get_urls(self, raw_html):
		# Function: get_urls
		# Purpose: Extract URLs from raw HTML
		
		# Defile the URL list
		url_list = []
		
		# Create the soup object
		soup = bs4.BeautifulSoup(raw_html.text, "html.parser")
		
		# Build a for loop to obtain the cite tags
		for cite_tag in soup.find_all("cite"):
			# Extract the full URL
			full_url = str(cite_tag)
			
			# Create regular expression to strip html
			html_stripper = re.compile(r'<.*?>')
			
			# Get the URL
			part_url = html_stripper.sub('', full_url)
			
			# Check if http:// in url
			if "http://" in part_url:
				# No need to append it
				url = part_url
			
			# Check if https:// in url
			elif "https://" in part_url:
				# No need to append it
				url = part_url	
			
			else:	
				# Append http:// to url
				url = "http://{}".format(part_url)
		
			# Append to the URL list
			url_list.append(url)
		
		# Return the URL list
		return url_list
			
# Define the __init__() function
def __init__(query, pages, proxy):
	# Function: __init__()
	# Purpose: Provide logic to scrape Google
	
	# Create the scraper object
	scraper = scrape(query, pages, proxy)
	
	# Define all URLs
	all_urls = []

	# Build a for loop to grab pages
	for i in range(pages):
		# Set the page ID
		page_id = i * 10
		
		# Attempt to get raw HTML
		try:
			raw_html = scraper.get_page(query, page_id, proxy)
		except:
			# Raise an exception
			raise Exception("[E] Unable to get raw HTML!")
		
		# Handle 503
		if raw_html.status_code == 503:
			# Display warning message
			print("[W] Temporarily banned by Google!")
			print("[+] CTRL-C to stop scan, ignore to continue")
			print("==============================")
		
		# Attempt to retrieve the URLS from the HTML
		try:
			urls = scraper.get_urls(raw_html)
		except:
			# Raise an exception
			raise Exception("[E] Unable to extract URLS!")
		
		# Build a for loop to dump urls into main list
		for url in urls:
			# Append to all URLS
			all_urls.append(url)
			
		# Wait a 5 to 20 seconds
		print("[I] Sleeping 5 to 20 seconds!")
		time.sleep(random.randint(5, 20))
		
	# Return the URLs
	return all_urls
