#!/usr/bin/python
import mechanize
import cookielib
from bs4 import BeautifulSoup
import re

#Browser
br = mechanize.Browser()

#Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
r = br.open('http://www.ldoceonline.com/browse/english/a/')
html = r.read()
#print html
#print br.response().read()
soup = BeautifulSoup(html, "html5lib")
innerDiv = soup.find(attrs={'class': "page_content"})
links = innerDiv.find_all("a", href=re.compile("^http"))
firstlink = None
for link in links:
    if link.find("span"):
        #print link
        sublink = link['href']
        r = br.open(sublink)
        html = r.read()
        soup = BeautifulSoup(html, "html5lib")
        inner_ul = soup.find(attrs={'class': "browse_results"})
        word_links = inner_ul.find_all("a", href=re.compile("^http"))
        for link in word_links:
            #text=link.find("span")
            #print text.string.encode('utf-8').strip()
            print link['href']
