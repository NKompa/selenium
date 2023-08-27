import yaml
import time
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])


def test_login_negative(x_selector1, x_selector2, x_selector3, btn_selector, expected_res_neg):
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector3)
    assert err_label.text == expected_res_neg, 'Test login negative failed.'


def test_login_positive(x_selector1, x_selector2, x_selector4, btn_selector, expected_res_pos):
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', btn_selector)
    btn.click()
    greeting = site.find_element('xpath', x_selector4)
    assert greeting.text == expected_res_pos, 'Test login positive failed.'


def test_create_post(
        create_post_btn_selector,
        title_input_selector, expected_title,
        description_input_selector, expected_description,
        content_input_selector, expected_content,
        post_button_selector, x_selector5
):
    # Нажать кнопку "Create new post"
    create_post_button = site.find_element('xpath', create_post_btn_selector)
    create_post_button.click()

    # Заполнить поля
    title_input = site.find_element('xpath', title_input_selector)
    title_input.send_keys(expected_title)
    description_input = site.find_element('xpath', description_input_selector)
    description_input.send_keys(expected_description)
    content_input = site.find_element('xpath', content_input_selector)
    content_input.send_keys(expected_content)

    post_button = site.find_element('xpath', post_button_selector)
    post_button.click()
    time.sleep(testdata['sleep_time'])

    # Проверить наличие поста на странице
    post_title = site.find_element('xpath', x_selector5)
    assert post_title.text == expected_title, 'Test create post failed.'
    site.close()
