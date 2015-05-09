from cloudmesh_base.Shell import Shell
import cloudmesh
from pprint import pprint


class command_spark(object):

    @classmethod
    def status(cls, host):
        msg = "Unknown host"
        try:
            msg = Shell.ping("-c", "1", host)
        except:
            pass
        if "1 packets transmitted, 1 packets received" in msg:
            return True
        elif "Unknown host" in msg:
            return False
        else:
            return False
  
    @classmethod
    def deploy(cls, name, count = 3, ln = "ubuntu", cloud = "india", flavor = "m1.small", image = "futuresystems/ubuntu-14.04"):
        mesh = cloudmesh.mesh("mongo")
        username = cloudmesh.load().usernam()
        print username
