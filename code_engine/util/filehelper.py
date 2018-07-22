import os
from codegenhelper import debug

def collect_files(path, ext):
    return debug([filepath for filepath in debug([y for x in debug([list(map(lambda file: "%s/%s" % (root, file), files))\
           for root, _, files in os.walk(os.path.abspath(path))]\
    ) for y in x]) if os.path.splitext(filepath)[1] == ext or os.path.splitext(filepath)[1] == "." + ext])
