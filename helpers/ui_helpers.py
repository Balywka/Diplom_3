import allure

@allure.step("Создать заказ через UI")
def add_order(main_page, email, password, drag_and_drop_script):
    if not main_page.is_user_logged_in():
        main_page.login(email, password)
        main_page.wait_for_login_completion()

    order_id = main_page.create_order_ui(drag_and_drop_script)
    return order_id