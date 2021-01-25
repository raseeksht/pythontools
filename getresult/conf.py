
# tweaking the code might be required for some websites
# this is good enought for majority of website

#if website send the post data to different page multipart = True else False
multipleUrl = True
url = "https://example.org/contact-us"
url2 = "https://example.org/feedback"

#False if the token is not required
tokenRequired = True

# for laravel --> _token
# for django --> csrfmiddlewaretoken
tokenName = "_token"



#this is just a headers modify if neded
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}


