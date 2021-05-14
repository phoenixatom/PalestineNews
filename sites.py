import requests
import lxml
from bs4 import BeautifulSoup


def aljazeera(url: str):
    main_url = "https://www.aljazeera.com"

    content = requests.get(url).text
    soup = BeautifulSoup(content, 'lxml')

    articles = []

    main_article = soup.find("div", class_="section-top-grid__col-1")
    main_title_h3 = main_article.find("h3", class_="gc__title")
    main_title = main_title_h3.text
    main_href = main_url + main_title_h3.find("a").get("href")
    main_image = main_url + \
        main_article.find("img", class_="gc__image").get("src")

    main_excerpt = main_article.find("div", class_="gc__excerpt").text
    articles.append({
        "title": main_title,
        "image": main_image,
        "excerpt": main_excerpt,
        "link": main_href
    })
    other_articles = soup.find("div", class_="section-top-grid__col-2")
    for article in other_articles.find_all("article", class_="gc gc--type-post gc--with-image"):
        title_h3 = article.find("h3", class_="gc__title")
        title = title_h3.text
        href = main_url + title_h3.find("a").get("href")
        image = main_url + \
            article.find("img", class_="gc__image").get("src")

        excerpt = article.find("div", class_="gc__excerpt").text

        articles.append({
            "title": title,
            "image": image,
            "excerpt": excerpt,
            "link": href
        })
    return articles
