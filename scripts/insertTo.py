def insertToTextFile(entryPoint: str,source: str,insert: str) -> str:
    start:str = ""
    end:str = ""
    mid:str = ""
    with open(source) as file:
        lines: list[str] = file.readlines()
        i:int = 0
        while "{{" + entryPoint + "}}" not in lines[i]:
            i = i + 1
            if i >= len(lines):
                break
        if i == len(lines):
            return "no place to insert"
        start = ''.join(lines[:i])
        if i >= len(lines) - 1:
            end = ""
        else:
            end = ''.join(lines[i+1:])
    with open(insert) as file:
        mid = file.read()
    return start + mid + '\n' + end

def insertToTextString(entryPoint: str,source: str,insert: str) -> str:
    start:str = ""
    end:str = ""
    mid:str = ""
    lines: list[str] = source.split("\n")
    i:int = 0
    while "{{" + entryPoint + "}}" not in lines[i]:
        i = i + 1
        if i >= len(lines):
            break
    if i == len(lines):
        return "no place to insert"
    start = '\n'.join(lines[:i])
    if i >= len(lines) - 1:
        end = ""
    else:
        end = '\n'.join(lines[i+1:])
    mid = insert
    return start + '\n' + mid + '\n' + end