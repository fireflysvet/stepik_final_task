from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    book_name = page.book_name()
    book_price = page.book_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_successful_add_alert()
    page.should_be_book_name_in_alert(book_name)
    page.should_be_alert_with_cart_price()
    page.should_be_correct_price_in_alert(book_price)
