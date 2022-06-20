import sys

from TyzenRemote.src.tyzen_config import Config
from TyzenRemote.src.tyzen_remote import Remote

if len(sys.argv) < 2:
    print("Error:\tNo parameters given!")
else:
    if sys.argv[1] == "remote":
        try:
            config = Config()
            tv_remote = Remote(config)
            tv_remote.connect()
            if len(sys.argv) == 3:
                try:
                    tv_remote.send_key(sys.argv[2], 1)
                except:
                    print("Error: Not a valid key!")
            elif len(sys.argv) == 4:
                try:
                    tv_remote.send_key(sys.argv[2], int(sys.argv[3]))
                except:
                    print("Error: Not a valid key or number of times!")
            else:
                print("Error: Not a valid input!")
        except:
            print("Error: Could not establish connection!")
    elif sys.argv[1] == "issue_token":
        try:
            config = Config()
            tv_remote = Remote(config)
            tv_remote.issue_token()
        except:
            print("Error: Could issue token!")
    elif sys.argv[1] == "config":
        config = Config()
        if len(sys.argv) == 4:
            try:
                if sys.argv[2] == "mac":
                    config.set_host(sys.argv[3])
                elif sys.argv[2] == "host":
                    config.set_host(sys.argv[3])
                elif sys.argv[2] == "api_port":
                    config.set_host(int(sys.argv[3]))
                elif sys.argv[2] == "wol_port":
                    config.set_host(int(sys.argv[3]))
            except:
                print("Error: Not a valid input!")
        else:
            print("Error: Not a valid input!")
    elif sys.argv[1] == "turn_on":
        try:
            config = Config()
            tv_remote = Remote(config)
            tv_remote.turn_on()
        except:
            print("Error: Could not turn on TV!")
quit()
