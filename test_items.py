

def test_button_exists(browser):
    button=len(browser.find_element_by_css_selector(".btn-add-to-basket").text)
    assert button>1