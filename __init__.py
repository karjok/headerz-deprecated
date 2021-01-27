import re,json

class HeaderTypeError(TypeError):
        pass
class CookieMapError(TypeError):
        pass
class Headerz:
        ''' A module for help you to parsing raw HTTP header string to customizable object.
I know this is a little shit but i like this module :D

Read full documentation at https://github.com/karjok/headerz'''
        def __init__(self):
                pass
        @classmethod
        def parser(self,headstring):
                ''' Parsing your raw header string from http sniffer tool like BurpSuite (PC), HttpCanary (Android) and return dictionary data
>>> raw_header_string = """
GET /?gws_rd=ssl h2
Host: www.google.com
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 9; Redmi Note 5A Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
dnt: 1
x-requested-with: mark.via.gp
sec-fetch-site: none
accept-encoding: gzip, deflate
accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7
cookie: SID=4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxzNqfMEY33_jQqKyizAUOfQ.
cookie: __Secure-3PSID=4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxNnECUtxpWINSJGrvM3jDaw.
cookie: HSID=APtpdvr7lnqKGjqrW
cookie: SSID=AXuQc_luyVDNx4vrE
cookie: APISID=1wmcYq9Ja0wEAknV/AGhZYVmR8vW4AC4az
cookie: SAPISID=H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ
cookie: __Secure-3PAPISID=H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ
cookie: CONSENT=YES+ID.en-AU+
cookie: 1P_JAR=2020-12-23-11
cookie: SEARCH_SAMESITE=CgQIu5EB
cookie: NID=205=C2H5rMrZtqbu8rob5hnT7tykdGdFkqGU84pk3YFwc5zteBb2A2YNUaFDBMlZmzFKQ3q8IUbTrdq56tgltw9nAYkXpyXLUXdr_PvKKR09nfO0k3AKvEdxGFZQhabvB3ME5lEc2uGC7TvBxb31JzejUXN0bKSx3wqJj8Ib-yJlUBRJXy3iryyhRX-17JNcb8A56btFjS8Vmv1PNim_pRhbU9LiRB4pZk7Zrqle3jbXGA6VT2eA1HtHRwKmfz3weDfWNXOcqpx9m442ndpzZPaHtg5dz-wsbUEmS8AI7Cl8ts-Hysva5cqepIrTksbHyVdA-xcNoTzOW-W5G44HvHA
cookie: SIDCC=AJi4QfGwtNFO9Dhfh96knkwKH3siz_G7w6RJrhUKTtxxaww5fB2RGkEFxKGVHlZyBLJmYl4Imw
cookie: __Secure-3PSIDCC=AJi4QfGCeDpLIylEar-u0t_bePUTuguVw-0HU05bjTZQB_wdfQmNUqLLadifLV0KwfP3PYzi9A"""
>>> parser(raw_header_string)
>>> {'ua': {'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5A Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36'}, 'headers': {'Host': 'www.google.com', 'upgrade-insecure-requests': '1', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}, 'cookie': {' SID': '4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxzNqfMEY33_jQqKyizAUOfQ.', ' __Secure-3PSID': '4wcfGdfcOyeM5iKg0cBOF7lKVfefpwccumQtjTLBvs3J-XTxNnECUtxpWINSJGrvM3jDaw.', ' HSID': 'APtpdvr7lnqKGjqrW', ' SSID': 'AXuQc_luyVDNx4vrE', ' APISID': '1wmcYq9Ja0wEAknV/AGhZYVmR8vW4AC4az', ' SAPISID': 'H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ', ' __Secure-3PAPISID': 'H2pagKd1LkCU6QVN/Aa4_qVEWBiLPyEAUJ', ' CONSENT': 'YES+ID.en-AU+', ' 1P_JAR': '2020-12-23-11', ' SEARCH_SAMESITE': 'CgQIu5EB', ' NID': '205=C2H5rMrZtqbu8rob5hnT7tykdGdFkqGU84pk3YFwc5zteBb2A2YNUaFDBMlZmzFKQ3q8IUbTrdq56tgltw9nAYkXpyXLUXdr_PvKKR09nfO0k3AKvEdxGFZQhabvB3ME5lEc2uGC7TvBxb31JzejUXN0bKSx3wqJj8Ib-yJlUBRJXy3iryyhRX-17JNcb8A56btFjS8Vmv1PNim_pRhbU9LiRB4pZk7Zrqle3jbXGA6VT2eA1HtHRwKmfz3weDfWNXOcqpx9m442ndpzZPaHtg5dz-wsbUEmS8AI7Cl8ts-Hysva5cqepIrTksbHyVdA-xcNoTzOW-W5G44HvHA', ' SIDCC': 'AJi4QfGwtNFO9Dhfh96knkwKH3siz_G7w6RJrhUKTtxxaww5fB2RGkEFxKGVHlZyBLJmYl4Imw', ' __Secure-3PSIDCC': 'AJi4QfGCeDpLIylEar-u0t_bePUTuguVw-0HU05bjTZQB_wdfQmNUqLLadifLV0KwfP3PYzi9A'}, 'data': {}, 'url': {'url': '/?gws_rd=ssl'}, 'type': {'type': 'GET'}, 'other': {}}
'''
                ua = {}
                header = {}
                cookie = {}
                data = {}
                url = {}
                tiipe = {}
                other = {}
                if type(headstring) != str:
                        raise HeaderTypeError("your entering data is an invalid header data. the data must be 'str'")
                for i in headstring.split("\n"):
                        if len(i) != 0:
                                y = i.split(":")
                                if i.split()[0] in ["POST","GET","PUT","DELETE","HEAD"]:
                                        uu = i.split()
                                        tiipe["type"] = uu[0]
                                        url["url"] = uu[1].strip()
                                elif "cookie" in y or "Cookie" in y or "cookie " in y or "Cookie " in y:
                                        if y[1].strip() !=  "":
                                                if len(y) > 2:
                                                        w = ":".join(y[1:])
                                                else:
                                                        w = y[1]
                                                a = w.split("=")
                                                if len(a) > 2:
                                                        cookie[a[0]] = "=".join(a[1:]).strip()
                                                else:
                                                        cookie[a[0]] = a[1].strip()
                                        else:
                                                cookie["Cookie"] = None
                                elif y[0] == "User-Agent" or y[0] == "user-agent" or y[0] == "User-agent":
                                        ua[y[0]] = y[1].strip()
                                elif "{" in i[0] or "}" in i[-1]:
                                        data.update(json.loads(i))
                                else:
                                        if len(y) > 2 :
                                                header[y[0]] = ":".join(y[1:]).strip()
                                        else:
                                                if len(y) < 2:
                                                        other["other"] = y[0].strip()
                                                else:
                                                        header[y[0]] = y[1].strip()
                return {"ua":ua,"headers":header,"cookie":cookie,"data":data,"url":url,"type":tiipe,"other":other}
        @classmethod
        def cookie_builder(self,kukimap):
                ''' If you have cookie in dictionary and you want to change it to cookie string.
>>> header_cookie = {"PHPSESSID":"rAnD0mStrInG","additional-cookie":"session1234567890"}
>>> cookie_builder(header_cookie)
>>> "PHPSESSID=rAnD0mStrInG;additional-cookie=session1234567890;"
'''
                if type(kukimap) != dict:
                        raise CookieMapError("cookie type must be dictionary")
                ck = []
                for a,b in kukimap.items():
                        ck.append(a.strip()+"="+b.strip())
                return ";".join(ck)
        @classmethod
        def header_input(self,args=None):
                ''' This function have optional argument like print() function. So if you put a value to header_input(), it will printing the argument.
Press ctrl + c if you has done.
>>> header_input()
>>>
>>> header_input("enter your headerstring: ")
>>> enter your headerstring

'''
                txt = ""
                if args:
	                print(args)
                while True:
                   try:
                            i = input()
                            if len(i) != 0:
                                  txt += i+"\n"
                            else:
                                  txt += "\n"
                   except:
                            break
                return txt
        @classmethod
        def other_parser(self,other_string):
                ''' This function is for parsing paramenter data from header string
>>> other_parser("id=1&name=karjok&github=karjok")
>>> {"id":"1","name":"karjok","github":"karjok"}
'''
                data = {}
                for i in other_string.split("&"):
                      x = i.split("=")
                      data[x[0]] = x[1]
                return data
        @classmethod
        def header_builder(self,header_string):
                ''' This function like parser() function but this is for if you want to direct use raw header string to ready use for requests headers paramenter'''
                raw_parser = self.parser(header_string)
                headers = raw_parser["headers"]
                headers.update(raw_parser["ua"])
                headers.update({"cookie":self.cookie_builder(raw_parser["cookie"])})
                return headers
