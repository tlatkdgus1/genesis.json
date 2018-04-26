import subprocess
import sys
import pexpect
def openGeth(enode):
    process = pexpect.spawn('geth --rpc --datadir "/home/pi-lab/data" --rpcaddr 0.0.0.0 --rpcport 8545 --rpccorsdomain "*" --nodiscover console')
    process.expect(">")
    process.sendline("personal.unlockAccount(eth.accounts[0], '1234qwer', 0)");
    process.expect(">")
    process.sendline("admin.addPeer(\""+enode+"\")")
    process.interact()

enode = raw_input('Input enode : ')
openGeth(enode)

