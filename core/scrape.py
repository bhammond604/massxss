# Import required modules
import os
import sys
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
	def __init__(self, query, pages):
		# Function: __init__()
		# Purpose: Initialize the scraper
		
		# Make sure a query was specified
		if query == None:
			# Raise an exception
			raise Exception("[E] Query must be specified with -q or --query!")
			
		# Dump everything to self
		self.query = query
		self.pages = pages
		
	# Define the get_page function
	def get_page(self, query, page_id):
		# Function: get_page()
		# Purpose: Get the raw HTML of the specified result page
		
		# Set the url
		url = "https://www.google.com/search"
		
		# Set the user agents
		user_agents = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
		               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:26.0) Gecko/20100101 Firefox/45.0.2",
		               "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136")
		
		# Set the scrape paramaters and headers
		scrape_params = {"q": query, "start": str(page_id)}
		scrape_headers = {"User-Agent": random.choice(user_agents)}
		
		# Attempt to get the raw HTML
		try:
			raw_html = requests.get(url, params = scrape_params, headers = scrape_headers)
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
		
		# Build a for loop to obtain the H3 tags with CSS class r
		for h3_tag in soup.find_all("h3", class_ = "r"):
			# Extract the URL
			url = h3_tag.a.get("href")
		
			# Append to the URL list
			url_list.append(url)
			
		# Return the URL list
		return url_list
			
# Define the __init__() function
def __init__(query, pages):
	# Function: __init__()
	# Purpose: Provide logic to scrape Google
	
	# Create the scraper object
	scraper = scrape(query, pages)
	
	# Define all URLs
	all_urls = []

	# Build a for loop to grab pages
	for i in range(pages):
		# Set the page ID
		page_id = i * 10
		
		# Attempt to get raw HTML
		try:
			raw_html = scraper.get_page(query, page_id)
		except:
			# Raise an exception
			raise Exception("[E] Unable to get raw HTML!")
		
		# Handle 503
		if raw_html.status_code == 503:
			# Display warning message
			print("[U] Temporarily banned by Google!")
		
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
			
		# Wait a 5 to 30 seconds
		time.sleep(random.randint(10, 30))
		
	# Return the URLs
	return all_urls
