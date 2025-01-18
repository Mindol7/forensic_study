from urllib import parse

original_file = open('linux_forensic/wargame/access_log/access.log', 'r')
flag_file = open('linux_forensic/wargame/access_log/flag_file.log', 'w')

while True:
    line = original_file.readline()

    if not line:
        break

    decoded = parse.unquote(line) # 디코딩 해줌.
    
    if 'flag' in decoded and 'value' in decoded and '!=' in decoded:
        lindex = decoded.find('!=')
        rindex = decoded.find('SLEEP')

        f = decoded[lindex+2 : rindex-2]
        str = chr(int(f))
        flag_file.write(str)