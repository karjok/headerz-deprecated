# headerz
A simple header string parser from HttpCanary (Android App)


## Instalation
```
pip install headerz
```

## Usage
```
from headerz import Headerz
```

### Parsing header string from user input
```
header_string = Headerz.header_input()
parser = Headerz.parser(header_string)
```

### Make a header data and use it for requests module header
```
header_string = Headerz.header_input('input your header here: ')
ready_use_header = Headerz.header_builder(header_string)
```

## All function defined in headerz module
* `parser(header_string)`
* `header_input(optional_argument)`
* `header_builder(header_string)`
* `cookie_builder(cookie_map)`
* `other_parser(other_data)`

## This is help text from help('headerz.Headerz')
```
headerz.Headerz = class Headerz(builtins.object)                                                                                               |  A module for help you to parsing raw HTTP header string to customizable object.
 |  I know this is a little shit but i like this module :D                                                                                     |
 |  Read full documentation at https://github.com/karjok/headerz
 |
 |  Methods defined here:
 |                                                                                                                                             |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  cookie_builder(kukimap) from builtins.type
 |      If you have cookie in dictionary and you want to change it to cookie string.
 |      >>> header_cookie = {"PHPSESSID":"rAnD0mStrInG","additional-cookie":"session1234567890"}
 |      >>> cookie_builder(header_cookie)
 |      >>> "PHPSESSID=rAnD0mStrInG;additional-cookie=session1234567890;"
 |
 |  header_builder(header_string) from builtins.type
 |      This function like parser() function but this is for if you want to direct use raw header string to ready use for requests headers paramenter
 |
 |  header_input(args=None) from builtins.type
 |      This function have optional argument like print() function. So if you put a value to header_input(), it will printing the argument.    |      Press ctrl + c if you has done.                                                                                                        |      >>> header_input()
 |      >>>
 |      >>> header_input("enter your headerstring: ")
 |      >>> enter your headerstring
 |                                                                                                                                             |  other_parser(other_string) from builtins.type                                                                                              |      This function is for parsing paramenter data from header string                                                                        |      >>> other_parser("id=1&name=karjok&github=karjok")                                                                                     |      >>> {"id":"1","name":"karjok","github":"karjok"}                                                                                       |                                                                                                                                             |  parser(headstring) from builtins.type                                                                                                      |      Parsing your raw header string from http sniffer tool like BurpSuite (PC), HttpCanary (Android) and return dictionary data             |      >>> raw_header_string = """                                                                                                            |      GET /?gws_rd=ssl h2                                                                                                                    |      Host: www.google.com                                                                                                                   |      upgrade-insecure-requests: 1
 |      user-agent: Mozilla/5.0 (Linux; Android 9; Redmi Note 5A Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36
 |      accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
 |      dnt: 1
 |      x-requested-with: mark.via.gp
 |      sec-fetch-site: none
 |      accept-encoding: gzip, deflate
 |      accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7
 |      cookie: SID=4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxzNqfMEY33_jQqKyizAUOfQ.
 |      cookie: __Secure-3PSID=4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxNnECUtxpWINSJGrvM3jDaw.
 |      cookie: HSID=APtpdvr7lnqKGjqrW
 |      cookie: SSID=AXuQc_luyVDNx4vrE
 |      cookie: APISID=1wmcYq9Ja0wEAknV/AGhZYVmR8vW4AC4az
 |      cookie: SAPISID=H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ
 |      cookie: __Secure-3PAPISID=H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ
 |      cookie: CONSENT=YES+ID.en-AU+
 |      cookie: 1P_JAR=2020-12-23-11
 |      cookie: SEARCH_SAMESITE=CgQIu5EB
 |      cookie: NID=205=C2H5rMrZtqbu8rob5hnT7tykdGdFkqGU84pk3YFwc5zteBb2A2YNUaFDBMlZmzFKQ3q8IUbTrdq56tgltw9nAYkXpyXLUXdr_PvKKR09nfO0k3AKvEdxGFZQhabvB3ME5lEc2uGC7TvBxb31JzejUXN0bKSx3wqJj8Ib-yJlUBRJXy3iryyhRX-17JNcb8A56btFjS8Vmv1PNim_pRhbU9LiRB4pZk7Zrqle3jbXGA6VT2eA1HtHRwKmfz3weDfWNXOcqpx9m442ndpzZPaHtg5dz-wsbUEmS8AI7Cl8ts-Hysva5cqepIrTksbHyVdA-xcNoTzOW-W5G44HvHA
 |      cookie: SIDCC=AJi4QfGwtNFO9Dhfh96knkwKH3siz_G7w6RJrhUKTtxxaww5fB2RGkEFxKGVHlZyBLJmYl4Imw
 |      cookie: __Secure-3PSIDCC=AJi4QfGCeDpLIylEar-u0t_bePUTuguVw-0HU05bjTZQB_wdfQmNUqLLadifLV0KwfP3PYzi9A"""
 |      >>> parser(raw_header_string)
 |      >>> {'ua': {'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5A Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36'}, 'headers': {'Host': 'www.google.com', 'upgrade-insecure-requests': '1', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}, 'cookie': {' SID': '4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxzNqfMEY33_jQqKyizAUOfQ.', ' __Secure-3PSID': '4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxNnECUtxpWINSJGrvM3jDaw.', ' HSID': 'APtpdvr7lnqKGjqrW', ' SSID': 'AXuQc_luyVDNx4vrE', ' APISID': '1wmcYq9Ja0wEAknV/AGhZYVmR8vW4AC4az', ' SAPISID': 'H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ', ' __Secure-3PAPISID': 'H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ', ' CONSENT':'YES+ID.en-AU+', ' 1P_JAR': '2020-12-23-11', ' SEARCH_SAMESITE': 'CgQIu5EB', ' NID': '205=C2H5rMrZtqbu8rob5hnT7tykdGdFkqGU84pk3YFwc5zteBb2A2YNUaFDBMlZmzFKQ3q8IUbTrdq56tgltw9nAYkXpyXLUXdr_PvKKR09nfO0k3AKvEdxGFZQhabvB3ME5lEc2uGC7TvBxb31JzejUXN0bKSx3wqJj8Ib-yJlUBRJXy3iryyhRX-17JNcb8A56btFjS8Vmv1PNim_pRhbU9LiRB4pZk7Zrqle3jbXGA6VT2eA1HtHRwKmfz3weDfWNXOcqpx9m442ndpzZPaHtg5dz-wsbUEmS8AI7Cl8ts-Hysva5cqepIrTksbHyVdA-xcNoTzOW-W5G44HvHA', ' SIDCC': 'AJi4QfGwtNFO9Dhfh96knkwKH3siz_G7w6RJrhUKTtxxaww5fB2RGkEFxKGVHlZyBLJmYl4Imw', ' __Secure-3PSIDCC': 'AJi4QfGCeDpLIylEar-u0t_bePUTuguVw-0HU05bjTZQB_wdfQmNUqLLadifLV0KwfP3PYzi9A'}, 'data': {}, 'url': {'url': '/?gws_rd=ssl'}, 'type': {'type': 'GET'}, 'other': {}}
```

## Contact
* https://t.me/om_karjok

