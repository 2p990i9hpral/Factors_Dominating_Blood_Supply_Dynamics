import pandas as pd
import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.bloodinfo.net/knrcbs/pr/promtn/lastPromtnList.do"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    processed_row_list = []
    for page_id in tqdm(range(1, 48+1)):
        data = {
            "currPage": page_id,
            "result": "L",
            "xssChk": "N",
            "maxSn": 10,
            "sysId": "knrcbs",
            "mi": 1099,
            "minSn": 0
        }

        response = requests.post(url=url, headers=headers, data=data)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        article_list = soup.select("div.bbs_ListA table tbody tr")

        for article in article_list:
            row_data_list = article.select("td")
            period_start, period_end = row_data_list[3].text.split("~")
            row_dict = {
                "id": int(row_data_list[0].text),
                "location": row_data_list[1].text,
                "title": row_data_list[2].text, # url
                "url": f"https://www.bloodinfo.net/knrcbs/pr/promtn/promtnInfoView.do?mi=1099&promtnSn={row_data_list[2].find('a').attrs['data-id']}&result=L",
                "period_start": period_start.strip(),
                "period_end": period_end.strip(),
                "institution": row_data_list[4].text,
                "wrote_date": row_data_list[5].text,
                "hits": int(row_data_list[6].text)
            }
            print(row_dict)
            processed_row_list.append(row_dict)
        time.sleep(0.5)
    promotion_df = pd.DataFrame(data=processed_row_list)
    print(promotion_df)
    promotion_df.to_csv("data/special_promotions.csv", index=False, encoding="utf-8-sig")