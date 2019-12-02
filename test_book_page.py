from .Pages.book_page import BookPage


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BookPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
