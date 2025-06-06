from scraper_helper import ScraperHelper

# Edward Yeboah
# CSE 337 HW 5
# SBU ID: 114385084

def scrape_headlines():
    # URL of the BBC website
    url = "https://www.bbc.com"
    
    # Fetch and parse the webpage
    soup = ScraperHelper.fetch_webpage(url)
    
    if soup:
        # Extract headlines and links
        # TODO: Call the extract_headlines method and pass the correct arguments
        headlines = ScraperHelper.extract_headlines(soup, url, "a", "media__link")
        
        # TODO: Use the print_headlines method to display the results
        ScraperHelper.print_headlines(headlines)
    else:
        print("Failed to retrieve headlines.")

# Run the function
scrape_headlines()
