import cookielib 
import urllib2 
import mechanize 
def is_sblock_form(form):
    return "id" in form.attrs and form.attrs['id'] == "etc-login-form"
# Browser 
br = mechanize.Browser() 

# Enable cookie support for urllib2 
cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

# Broser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 

# ?? 
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

# authenticate 
#br.open("http://securecn1.englishtown.com/login/handler.ashx") 
br.open("http://e1.englishtown.com/partner/englishcenters/cn") 
#br.select_form( predicate=is_sblock_form ) 
br.select_form(predicate=lambda f: f.attrs.get('id', None) == 'etc-login-form' ) 
# these two come from the code you posted
# where you would normally put in your username and password
br[ "username" ] = "zyuruc"
br[ "password" ] = "120215"
res = br.submit()
url = br.open("http://e1.englishtown.com/school/myaccount2.aspx") 
returnpg = url.read() 
print returnpg
