import logging 
from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__) # 

def test_find_authors_quotes(page :Page):
    page.goto("https://quotes.toscrape.com/")  #navigate to the quotes website
    quotes = page.locator(".quote") # find the locator for all the quotes on the page
    expect(quotes).to_have_count(10) # assert that there are 10 quotes on the page

    for i in range (quotes.count()):
        quote = quotes.nth(i) # get the quote at index i 
        text = quote.locator(".text").inner_text() # get the text of the quote
        author = quote.locator(".author").inner_text() # get the author of the quote
        if not author or not text: # check if the author or text is empty
            logger.warning(f"Quote at index {i} is missing author or text") # log a warning if the author or text is empty
        logger.info ( {'Author' :author , 'Quote' : text}) # print the author and quote in a dictionary format

        assert text
        assert author # assert that the text and author are not empty
