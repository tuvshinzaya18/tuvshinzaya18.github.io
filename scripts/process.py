from insertTo import insertToText
from typing import List 
# Names of pages
pages:List[str] = ["index","more","projects","resume","books"]

html:str = insertToText("../template/master.html","../template/index.html")

with open("result.html","w") as file:
    file.write(html)