from os import system as sys

def get_str():
    f=open("contact.unl","r")
    o=f.read()
    f.close()
    return o
def escape_str(s):
    nl="""
"""
    s=s.replace("`",r"\`").replace(nl,r"\n")
    s=s+r"\n"
    s=f"echo -e \"{s}\"" 
    return s
def out(s):
    f=open("contact","w+")
    f.write("#!/bin/bash\n")
    f.write(s)
    f.close()
def chmod():
    sys("chmod +x ./contact")
def main():
    s=escape_str(get_str())
    out(s)
    chmod()

main()