import subprocess
import sys
import pexpect

def makeAccount():
    process = pexpect.spawn('geth --datadir "/home/pi-lab/data" account new')
    process.expect("assphrase:")
    process.sendline("1234qwer")
    process.expect("assphrase:")
    process.sendline("1234qwer")
    account = process.read().split("{")[1].split("}")[0]
    return account

account = makeAccount()
