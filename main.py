from scraper import scrape_articles
from translator import translate_text
from analyzer import analyze_translated_headers


def main():
    # Scrape articles
    articles = scrape_articles()

    # Print and translate titles
    translated_headers = []
    for article in articles:
        print("Title (Spanish):", article["title"])
        print("Content:", article["content"][:200], "...")

        translated_title = translate_text(article["title"])
        print("Title (English):", translated_title)
        translated_headers.append(translated_title)

    # Analyze repeated words
    repeated_words = analyze_translated_headers(translated_headers)
    print("Repeated Words:", repeated_words)


if __name__ == "__main__":
    main()
