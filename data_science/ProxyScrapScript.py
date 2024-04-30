import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib as matplotlib
url = "https://sofifa.com/players?showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=vl&showCol%5B11%5D=wg&showCol%5B12%5D=rc&showCol%5B13%5D=ta&showCol%5B14%5D=cr&showCol%5B15%5D=fi&showCol%5B16%5D=he&showCol%5B17%5D=sh&showCol%5B18%5D=vo&showCol%5B19%5D=ts&showCol%5B20%5D=dr&showCol%5B21%5D=cu&showCol%5B22%5D=fr&showCol%5B23%5D=lo&showCol%5B24%5D=bl&showCol%5B25%5D=to&showCol%5B26%5D=ac&showCol%5B27%5D=sp&showCol%5B28%5D=ag&showCol%5B29%5D=re&showCol%5B30%5D=ba&showCol%5B31%5D=tp&showCol%5B32%5D=so&showCol%5B33%5D=ju&showCol%5B34%5D=st&showCol%5B35%5D=sr&showCol%5B36%5D=ln&showCol%5B37%5D=te&showCol%5B38%5D=ar&showCol%5B39%5D=in&showCol%5B40%5D=po&showCol%5B41%5D=vi&showCol%5B42%5D=pe&showCol%5B43%5D=cm&showCol%5B44%5D=td&showCol%5B45%5D=ma&showCol%5B46%5D=sa&showCol%5B47%5D=sl&showCol%5B48%5D=tg&showCol%5B49%5D=gd&showCol%5B50%5D=gh&showCol%5B51%5D=gc&showCol%5B52%5D=gp&showCol%5B53%5D=gr&showCol%5B54%5D=tt&showCol%5B55%5D=bs&showCol%5B56%5D=ir&showCol%5B57%5D=pac&showCol%5B58%5D=sho&showCol%5B59%5D=pas&showCol%5B60%5D=dri&showCol%5B61%5D=def&showCol%5B62%5D=phy%3D&offset=0"


def proxy_scrap_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "United States"
    }

    max_retries = 5  # Maximum number of retry attempts
    retries = 0
    while retries < max_retries:
        try:
            response = requests.post(
                "https://realtime.oxylabs.io/v1/queries",
                auth=("YOUR ACCOUNT", "YOUR PASSWORD"),
                json=payload
            )
            response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
            data = response.json()
            if response.status_code == 200:
                response_html = data['results'][0]['content']
                return BeautifulSoup(response_html, 'html.parser')
            else:
                print(f"Request failed or status not 'done'. Retrying... Attempt {retries + 1}")
                retries += 1
                time.sleep(1)  # Add a delay between retries
        except (requests.RequestException, ValueError) as e:
            print(f"An error occurred: {e}. Retrying... Attempt {retries + 1}")



pages = [
    "https://sofifa.com/players?showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=vl&showCol%5B11%5D=wg&showCol%5B12%5D=rc&showCol%5B13%5D=ta&showCol%5B14%5D=cr&showCol%5B15%5D=fi&showCol%5B16%5D=he&showCol%5B17%5D=sh&showCol%5B18%5D=vo&showCol%5B19%5D=ts&showCol%5B20%5D=dr&showCol%5B21%5D=cu&showCol%5B22%5D=fr&showCol%5B23%5D=lo&showCol%5B24%5D=bl&showCol%5B25%5D=to&showCol%5B26%5D=ac&showCol%5B27%5D=sp&showCol%5B28%5D=ag&showCol%5B29%5D=re&showCol%5B30%5D=ba&showCol%5B31%5D=tp&showCol%5B32%5D=so&showCol%5B33%5D=ju&showCol%5B34%5D=st&showCol%5B35%5D=sr&showCol%5B36%5D=ln&showCol%5B37%5D=te&showCol%5B38%5D=ar&showCol%5B39%5D=in&showCol%5B40%5D=po&showCol%5B41%5D=vi&showCol%5B42%5D=pe&showCol%5B43%5D=cm&showCol%5B44%5D=td&showCol%5B45%5D=ma&showCol%5B46%5D=sa&showCol%5B47%5D=sl&showCol%5B48%5D=tg&showCol%5B49%5D=gd&showCol%5B50%5D=gh&showCol%5B51%5D=gc&showCol%5B52%5D=gp&showCol%5B53%5D=gr&showCol%5B54%5D=tt&showCol%5B55%5D=bs&showCol%5B56%5D=ir&showCol%5B57%5D=pac&showCol%5B58%5D=sho&showCol%5B59%5D=pas&showCol%5B60%5D=dri&showCol%5B61%5D=def&showCol%5B62%5D=phy%3D&offset=0"]

for page in range(0, 3060, 60): #Offset is 60 per page
    pages.append(
        "https://sofifa.com/players?showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=vl&showCol%5B11%5D=wg&showCol%5B12%5D=rc&showCol%5B13%5D=ta&showCol%5B14%5D=cr&showCol%5B15%5D=fi&showCol%5B16%5D=he&showCol%5B17%5D=sh&showCol%5B18%5D=vo&showCol%5B19%5D=ts&showCol%5B20%5D=dr&showCol%5B21%5D=cu&showCol%5B22%5D=fr&showCol%5B23%5D=lo&showCol%5B24%5D=bl&showCol%5B25%5D=to&showCol%5B26%5D=ac&showCol%5B27%5D=sp&showCol%5B28%5D=ag&showCol%5B29%5D=re&showCol%5B30%5D=ba&showCol%5B31%5D=tp&showCol%5B32%5D=so&showCol%5B33%5D=ju&showCol%5B34%5D=st&showCol%5B35%5D=sr&showCol%5B36%5D=ln&showCol%5B37%5D=te&showCol%5B38%5D=ar&showCol%5B39%5D=in&showCol%5B40%5D=po&showCol%5B41%5D=vi&showCol%5B42%5D=pe&showCol%5B43%5D=cm&showCol%5B44%5D=td&showCol%5B45%5D=ma&showCol%5B46%5D=sa&showCol%5B47%5D=sl&showCol%5B48%5D=tg&showCol%5B49%5D=gd&showCol%5B50%5D=gh&showCol%5B51%5D=gc&showCol%5B52%5D=gp&showCol%5B53%5D=gr&showCol%5B54%5D=tt&showCol%5B55%5D=bs&showCol%5B56%5D=ir&showCol%5B57%5D=pac&showCol%5B58%5D=sho&showCol%5B59%5D=pas&showCol%5B60%5D=dri&showCol%5B61%5D=def&showCol%5B62%5D=phy%3D&offset=" + str(
            page))

players = []
for i, page in enumerate(pages):
    try:
        scrap = proxy_scrap_request(page)
        print(len(scrap))
        webPage = scrap.find(("table", {"class": "table table-hover persist-area"}))
        for row in webPage.find_all("tr")[1:]:
            cols = row.find_all("td")
            player = {"name": cols[1].get_text().strip()}
            for col in cols[2:]:
                header = webPage.find_all("th")[cols.index(col)].get_text().strip()
                player[header] = col.get_text().strip()

            players.append(player)
        print(i)

    except (ValueError, AttributeError) as e:
        print(f"An error occurred: {e}. Retrying scraping...")
        scrap = proxy_scrap_request(page)
        if scrap:
            webPage = scrap.find(("table", {"class": "table table-hover persist-area"}))
            for row in webPage.find_all("tr")[1:]:
                cols = row.find_all("td")
                player = {"name": cols[1].get_text().strip()}
                for col in cols[2:]:
                    header = webPage.find_all("th")[cols.index(col)].get_text().strip()
                    player[header] = col.get_text().strip()

                players.append(player)
        else:
            print("Failed to scrape page after retrying.")

df = pd.DataFrame(players)
df.to_csv('playerDB.csv', index=False)
print(df.head())
# print(players)

#%%
