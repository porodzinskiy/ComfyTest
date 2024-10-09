import time

import pytest

from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.spec_page import Spec_page
from pages.tv_audio_video_page import Tv_audio_video_page
from pages.tv_page import Tv_page


def test_buy_product_with_filters(set_up):
    driver = set_up

    mp = Main_page(driver)
    mp.goto_tv_audio_video()

    tavp = Tv_audio_video_page(driver)
    tavp.goto_tv()

    tvp = Tv_page(driver)
    tvp.filters()
    product_name, product_price = tvp.to_cart()

    sp = Spec_page(driver, product_name, product_price)
    sp.add_to_cart()

    cp = Cart_page(driver, product_name, product_price)
    cp.goto_checkout()

    chp = Checkout_page(driver, product_name, product_price)
    chp.goto_order()