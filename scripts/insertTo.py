def insertToText(source: str,insert: str) -> str:
    start:str = ""
    end:str = ""
    mid:str = ""
    with open(source) as file:
        lines: list[str] = file.readlines()
        i:int = 0
        while "{{insert}}" not in lines[i]:
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