import requests


def indeed_request():
    

    url = "https://www.indeed.com/jobs ?q=software engineer&l=charlotte"

    payload = {}
    headers = {
    'Cookie': '__cf_bm=KzZwCkOaKl0uOg8xvxK8E33wKV_mLZV8mTt.pSWaZNQ-1687965772-0-ASn1VUCXldnn7SSBVG2oIEQjW8KqmjyNjJBhq4E1YYRT4XZWAAlg4iLV483FdJvk6sCv/6lu7FUGTDcXKnUy56c='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # TODO 2: 

    


if __name__ == '__main__':
    indeed_request()
