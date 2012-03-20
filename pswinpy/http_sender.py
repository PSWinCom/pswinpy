
import httplib
from pswinpy.mode import Mode

class HttpSender(object):
  apiHost = 'sms3.pswin.com'
  apiUrl = '/sms'

  def __init__(self, host=apiHost, url=apiUrl):
    self.host = host
    self.url = url

  def send(self, request):
    if Mode.test:
      return
    xml = request.xml()
    webservice = httplib.HTTP(self.host)
    if Mode.debug:
      webservice.set_debuglevel(3)
    webservice.putrequest("POST", self.url)
    webservice.putheader("Content-type", "text/xml; charset=\"latin1\"")
    webservice.putheader("Content-length", "%d" % len(xml))
    webservice.endheaders()
    webservice.send(xml)
    statuscode, statusmessage, header = webservice.getreply()
    if Mode.debug:
        print "Response: ", statuscode, statusmessage
        print "headers: ", header
        res = webservice.getfile().read()
        print res
    return statuscode
