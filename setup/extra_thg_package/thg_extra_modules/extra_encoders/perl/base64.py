from base64 import b64encode
from thgconsole.core.ModulesBuild.Encoders.encoders import BaseEncoder
from thgconsole.core.ModulesBuild.Payloads.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "name": "Perl Base64 Encoder",
        "description": "Module encodes PERL payload to Base64 format.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    architecture = Architectures.PERL

    def encode(self, payload):
        encoded_payload = str(b64encode(bytes(payload, "utf-8")), "utf-8")
        return "use MIME::Base64;eval(decode_base64('{}'));".format(encoded_payload)
