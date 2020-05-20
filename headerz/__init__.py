import re,json

class HeaderTypeError(TypeError):
        pass
class CookieMapError(TypeError):
        pass
class headerz:
        def __init__(self):
                pass

        def parser(self,headstring):
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
        def cookie_builder(self,kukimap):
                if type(kukimap) != dict:
                        raise CookieMapError("cookie type must be dictionary")
                ck = []
                for a,b in kukimap.items():
                        ck.append(a.strip()+"="+b.strip())
                return ";".join(ck)

        def header_input(self):
                txt = ""
                print(f"Type !done if you're done")
                while True:
                            i = input()
                            if i == "!done":
                                  break
                            elif len(i) != 0:
                                  txt += i+"\n"
                            else:
                                  txt += "\n"
                return txt
        def other_parser(self,other_string):
                data = {}
                for i in other_string.split("&"):
                      x = i.split("=")
                      data[x[0]] = x[1]
                return data
