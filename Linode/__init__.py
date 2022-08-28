import cfscrape
from bs4 import BeautifulSoup

def linode(username,password):
    scraper = cfscrape.create_scraper()

    req = scraper.get("https://login.linode.com/login")
    soup = BeautifulSoup(req.content, 'html.parser')
    TK = soup.input["value"]

    datas = f"csrf_token={TK}&return_to=https%3A%2F%2Flogin.linode.com%2F&created=2021-03-21T07%3A43%3A43.668635&username={username}&password={password}&submit=Oturum+a%C3%A7"

    headerss = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    req = scraper.post("https://login.linode.com/login", data=datas, headers=headerss, allow_redirects=False).text
    print(req)
    if "<li>Username or password incorrect.</li>" in req:
        print(f"Wrong Credentials >> {username}:{password}")
    elif "You should be redirected automatically to target URL: <a href=\"https://login.linode.com/\">https://login.linode.com/</a>." in req:
        print(f"Login Successfully! >> {username}:{password}")
    elif "You should be redirected automatically to target URL: <a href=\"/login/verify\">/login/verify</a>." in req:
        print(f"2FACTOR >> {username}:{password}")
