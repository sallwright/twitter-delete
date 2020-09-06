with open("code/twitter-config.json") as f:
    config = json.load(f)

os.environ["API_KEY"] = config['api-key']
os.environ["API_SECRET_TOKEN"] = config['api-secret-token']
os.environ["ACCESS_TOKEN"] = config['access-token']
os.environ["ACCESS_TOKEN_SECRET"] = config['access-token-secret']