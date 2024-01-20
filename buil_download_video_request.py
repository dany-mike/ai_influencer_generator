import os

def build_download_video_request(link):
    cookies = {
        '_ga': 'GA1.1.445204468.1705697560',
        'FCCDCF': '%5Bnull%2Cnull%2Cnull%2C%5B%22CP4oVMAP4oVMAEsACBENAkEgAAAAAEPgACgAAAAQaQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAgAA%22%2C%222~~dv.2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.317.323.2373.338.358.2415.415.449.2506.2526.482.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958.1960%22%2C%22A3F9BB76-32D9-44C6-8300-DA819CA91FCC%22%5D%5D',
        '_ga_ZSF3D6YSLC': 'GS1.1.1705697560.1.0.1705697585.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # set token below if needed
        'cookie': os.environ.get('tiktok_cookie'),
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'NnZBMVVk',
    }

    return {
        'data': data,
        'params': params,
        'headers': headers,
        'cookies': cookies
    }