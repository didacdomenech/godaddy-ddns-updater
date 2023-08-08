import pif, sys, os

from dotenv import load_dotenv
from godaddypy import Client, Account

global API_KEY, API_SECRET, PUBLIC_IP, DOMAIN, A_RECORD

load_dotenv()

try:
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    DOMAIN = os.getenv("DOMAIN")
    A_RECORD = os.getenv("A_RECORD")
    userAccount = Account(api_key=API_KEY, api_secret=API_SECRET)
    userClient = Client(userAccount)
except EnvironmentError:
    print("could not read environmental variables. Check '.env' file.")
    sys.exit()

PUBLIC_IP = pif.get_public_ip("ident.me")

def main():
    try:
        current_ip = userClient.get_records(DOMAIN, record_type='A', name=A_RECORD)
        if (PUBLIC_IP != current_ip[0]['data']):
            updateResult = userClient.update_record_ip(PUBLIC_IP, DOMAIN, A_RECORD, 'A')
            if updateResult is True:
                print(f"{A_RECORD}.{DOMAIN} updated with [{PUBLIC_IP}]")
            else:
                print(f"Something went wrong updating {A_RECORD}.{DOMAIN}")
        else:
            print("DNS records are correctly configured, no update needed")
    except:
        print(sys.exc_info()[1])
        sys.exit()

if __name__ == "__main__":
    try:
        main()
    except:
        print(f"⚙️ -- MEMBLOCK -- ⚙️\nmain() panicked with:\n {sys.exc_info()}")
