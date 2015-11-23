# coding: utf-8

from tapioca import (TapiocaAdapter, generate_wrapper_from_adapter)

from requests_oauthlib import OAuth2

from .resource_mapping import RESOURCE_MAPPING

from tapioca.adapters import XMLAdapterMixin
from tapioca.oauth2_token_requester import Oauth2TokenRequester  # todo: cookiecutter


class GsheetsClientAdapter(XMLAdapterMixin, TapiocaAdapter):
    api_root = 'https://spreadsheets.google.com/feeds'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(GsheetsClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = OAuth2(
            api_params.get('client_id', ''), token={
                'access_token': api_params.get('access_token'),
                'token_type': 'Bearer'})

        return params


# todo: add to cookiecutter for oauth2
def initialize_oauth2_request_session():
    '''
    A helper for getting Oauth2 tokens.

    Usage:
    # 1. Modify the code below for your Oauth2 app and authorizer
    # 2. Open a python shell

    >>> from tapioca_myproject import initialize_oauth_request_session
    >>> my_token = initialize_oauth2_request_session()

    # 3. Follow the instructions in the terminal to instantiate my_token
    # 4. Start using your Tapioca API!

    >>> from tapioca_myproject import Myproject
    >>> api = Myproject(access_token=my_token['access_token'])
    '''

    # boilerplate instructions:
    # client_id = '<client/app id>'
    # client_secret = '<client/app secret>'
    # redirect_uri = '<a valid redirect uri for your client>'
    # authorization_base_url = '<url to send initial auth request>'
    # obtain_token_url = '<url to exchange code for token>'
    # scope_list = ['<requested scope 1>', '<requested scope 2>']
    # auth_base_url_kwargs = {'<extra args to send with initial auth request>': '<value>',
    #                         '<another key>': '<another value>'}

    client_id = raw_input('\nEnter your app\'s client id:\n')
    client_secret = raw_input('\nEnter your app\'s client secret:\n')
    redirect_uri = raw_input('\nEnter your app\'s redirect URI:\n')

    authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
    obtain_token_url = 'https://accounts.google.com/o/oauth2/token'
    scope_list = ['https://spreadsheets.google.com/feeds']
    auth_base_url_kwargs = {'access_type': 'offline',
                            'approval_prompt': 'force'}

    if client_id == '<client/app id>':
        raise ValueError('Configure each variable for your Oauth2 request process.')

    o = Oauth2TokenRequester(client_id,
                             client_secret=client_secret,
                             redirect_uri=redirect_uri,
                             authorization_base_url=authorization_base_url,
                             obtain_token_url=obtain_token_url,
                             scope_list=scope_list,
                             **auth_base_url_kwargs)

    authorization_url = o.authorize_app()

    print ('\n###### OauthRequester User Prompt ######\n'
           '1. Please go to the following URL to authorize access: \n\n%s' % authorization_url)

    redirect_response = raw_input('\n2. Enter the full callback URL that your request was '
                                  'redirected to:\n')

    token = o.get_token(redirect_response)

    return token

Gsheets = generate_wrapper_from_adapter(GsheetsClientAdapter)
