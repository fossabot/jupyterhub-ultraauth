from oauthenticator.github import LocalGitHubOAuthenticator
import os

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
c.Authenticator.admin_users = {'brendancol'}
c.Authenticator.whitelist = {'brendancol', 'chbrandt'}

c.LocalGitHubOAuthenticator.create_system_users = True
c.LocalGitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
c.LocalGitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']
c.LocalGitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
