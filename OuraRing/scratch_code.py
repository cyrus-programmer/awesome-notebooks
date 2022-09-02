import argparse

import requests


class OuraRing:
    '''This class encompasses a set of functions to connect to the Oura Ring api
    and pull one's respective data. Note that this class assumes you are
    accessing the api for personal use, and thus authorization is only via
    personal access tokens.
    '''
    def __init__(self, personal_access_token: str) -> None:
        self.PAT = personal_access_token
        pass

    def authenticate_api(self) -> None:
        '''Function takes a personal access token and connect to the oura ring
        api. PATs can be generated by navigating to the following website and
        creating an account: https://cloud.ouraring.com/personal-access-tokens 

        Docs: https://cloud.ouraring.com/docs/authentication
        '''
        url = f'https://api.ouraring.com/v1/userinfo?access_token={self.PAT}'
        response = requests.get(url)
        
        print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-pat', '--pat', default=None, type=str)
    options = parser.parse_args()

    oura = OuraRing(personal_access_token=options.pat)
    oura.authenticate_api()
