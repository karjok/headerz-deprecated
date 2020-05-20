# headerz
A simple header string parser from HttpCanary (Android App)


<b>Instalation</b></br>
<pre>pip install headerz</pre></br>

<b>Usage</b></br>
<pre>
import headerz

hdz = headerz.headerz()
</pre>

Parsing header string
<pre>
header_string = hdz.header_input()
parser = hdz.parser(header_string)
</pre>

Make a header data
<pre>
header = parser["headers"]
</pre>

Make a cookie data
<pre>
cookie_map = parser["cookie"]
</pre>

Make a cookie string
<pre>
cookie_string = hdz.cookie_builder(cookie_map)
</pre>
