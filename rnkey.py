import js2py
import re
import requests
import json


def rnkey(siteurl):
	resp = requests.get(url=siteurl)
	jscode = re.search(r'<!--([\s\S]+)//--></script', resp.text).group(1)

	code = jscode.replace("{ document.cookie=", "return ")
	code = re.sub(r'document.location.reload\(true\);\s*}\s*}', '} var res=go();', code)

	evaluated = js2py.eval_js(code)
	rncookie = re.sub(r'^([^=]+)=([^;]+).*', '{"\\1":"\\2"}', evaluated)

	return json.loads(rncookie)
