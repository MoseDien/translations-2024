# env
import getpass
import os

from dotenv import load_dotenv
load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key")

# proxy
os.environ['http_proxy'] = 'http://127.0.0.1:7890' 
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
os.environ['all_proxy'] = 'socks5://127.0.0.1:7890'