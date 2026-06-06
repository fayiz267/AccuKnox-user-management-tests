from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(2000)

    page.locator("xpath=/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").fill("Admin")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").fill("admin123")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/button[2]/i").click()
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]").click()

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]").select_option("Admin")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").fill("Orange  Test")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]").click()
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]").click()
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").fill("Orange_test")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").fill("Qwerty@123")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").fill("Qwerty@123")
    page.wait_for_timeout(1000)

    page.locator("xpath=/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
    page.wait_for_timeout(1000)

    page.close()
    browser.close()