from os import environ
c.JupyterHub.authenticator_class = 'oauthenticator.generic.GenericOAuthenticator'

# c.OAuthenticator.client_id = environ.get('ULTRAAUTH_CLIENT_ID')
# c.OAuthenticator.client_secret = environ.get('ULTRAAUTH_CLIENT_SECRET')
#
# # oauth2 provider's token url
# c.GenericOAuthenticator.token_url = environ.get('ULTRAAUTH_TOKEN_URL')
#
# # oauth2 provider's endpoint with user data
# c.GenericOAuthenticator.userdata_url = environ.get('ULTRAAUTH_USERDATA_URL')
#
# c.GenericOAuthenticator.userdata_method = 'POST'
#
# # params to send for userdata endpoint
# # c.GenericOAuthenticator.userdata_params = {} #environ.get('ULTRAAUTH_USERDATA_PARAMS')
#
# # username key from json returned from user data endpoint
# # c.GenericOAuthenticator.username_key = environ.get('ULTRAAUTH_USERNAME_KEY')
#
# c.Application.log_level = 'DEBUG'
#
#
# c.GenericOAuthenticator.extra_params = {
#     'scope': ['openid', 'email', 'profile', 'address'],
#     'client_id': '1ee853bc-0009-4b27-b0c2-d26412f23689',
#     'client_secret': 'rKXpYrQNwI/ga2iDS/rhHEBl072j641ZZQR8VSPYsON0SPpW8hFMK5mDvxAnQ+4/'
#     }
