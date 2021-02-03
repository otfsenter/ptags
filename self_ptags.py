import sys, re, os

tags = []    # Modified global variable!

path_root = r'D:\Python\Lib'

expr = r'^[ \t]*(def|class)[ \t]+([a-zA-Z0-9_]+)[ \t]*[:\(]'
matcher = re.compile(expr)

def run():
    matches = []
    for dirpath, dirnames, filenames in os.walk(path_root):
        for filename in filenames:
            if filename.endswith('.py'):
                a = os.path.join(dirpath, filename)
                matches.append(a)
    return matches

def main():
    args = run()
    for filename in args:
        treat_file(filename)

    if tags:
        print('in tags')
        fp = open('tags', 'w', encoding='utf-8', errors='ignore')
        tags.sort()
        for s in tags: fp.write(s)



def treat_file(filename):
    fp = open(filename, 'r', encoding='utf-8', errors='ignore')
    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break
        m = matcher.match(line)
        if m:
            content = m.group(0)
            name = m.group(2)
            s = name + '\t' + filename + '\t/^' + content + '/\n'
            tags.append(s)

if __name__ == '__main__':
    main()
