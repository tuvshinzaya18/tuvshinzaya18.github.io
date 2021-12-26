from insertTo import insertToTextFile,insertToTextString
from typing import List 
# Names of pages
pages:List[str] = ["index","more","projects","resume","books"]

html:str = insertToTextFile("insert","../template/master.html","../template/index.html")
html:str = insertToTextString("style",html,"<link rel=\"stylesheet\" type=\"text/css\" href=\"../styles/index.css\">")
with open("result.html","w") as file:
    file.write(html)

for name in pages:
    html:str = insertToTextFile("insert","../template/master.html","../template/"+name+".html")
    html:str = insertToTextString("style",html,"<link rel=\"stylesheet\" type=\"text/css\" href=\"../styles/"+name+".css\">")
    with open("../docs/"+name+".html","w") as file:
        file.write(html)