import tweepy
Bearer_Token="AAAAAAAAAAAAAAAAAAAAAGf25gEAAAAAlpp1ne4c8CpnzquNFHbclzrhExQ%3DRdoCjHiuTFpsDbKTBbblgn7eHTvqcHqn2H2uVbFn7OcL7U4Dlk"
API_Key="bIJ9KVfja6DGwx8nsrAUVyt1g"
API_Secret_Key="gJpdL7WwKf7MFZVf9hB7ejubGjyPDKyvohqaKOajx09EOxiY8z"
Access_Token="1995350816266592256-RdPfT8P0BW6pncj1aOReG7VNLWcWK3"
Access_Token_Secret="rnG2zrDDfnGonCcC3m2091M481vRxbhc25IiZiGZ5VxDn"
client=tweepy.Client(bearer_token=Bearer_Token,consumer_key=API_Key,consumer_secret=API_Secret_Key,access_token=Access_Token,access_token_secret=Access_Token_Secret)
response=client.create_tweet(text="Hello,How are u")
print(f"tweet posted successfully with ID:{response.data['id']}")
me=client.get_me()
print(me)