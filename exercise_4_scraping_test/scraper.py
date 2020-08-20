from urllib.parse import urlparse

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def get_followers_count(url) -> int:
    username = urlparse(url).path.replace("/", "")

    req = Request(url)
    req.add_header('User-Agent', 'GoogleBot')
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    a_followers_tag = soup.find_all('a', attrs={"href": f'/{username}/followers'})
    if len(a_followers_tag) == 0:
        raise ValueError("Could not find user followers")
    title = a_followers_tag[0]["title"]  # 12,000 Followers
    count_str = title.replace(",", "").split()[0]
    return int(count_str)


print(get_followers_count("https://twitter.com/meshawara/"))
