def login(page, username, password, target_url_after_login):
    print("🔐 Bắt đầu đăng nhập...")

    page.context.clear_cookies()

    LOGIN_URL = (
        "https://kc.dev.x-or.cloud/auth/realms/xor/protocol/openid-connect/auth?client_id=portal&redirect_uri=https%3A%2F%2Fportal.stack-dev.x-or.cloud%2Fcallback&state=e249dd16-6a8e-4bbc-8956-7a5719735166&response_mode=fragment&response_type=code&scope=openid&nonce=4f40033f-3c81-423f-9ebb-38c495f563a9&code_challenge=51S2lDqn6j6pKWRNqoFG4_-0w91eOJ4QlLMN9DhHkw0&code_challenge_method=S256"
    )
    page.goto(LOGIN_URL)

    try:
        if page.url.startswith("https://kc.dev.x-or.cloud/"):
            print("🔑 Trang yêu cầu đăng nhập...")

            page.wait_for_selector('input[name="username"]', timeout=10000)
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click('button[type="submit"]')

        print("⏳ Chờ hoàn tất đăng nhập...")
        page.wait_for_load_state("networkidle", timeout=15000)

        # Điều hướng đến trang thao tác chính
        print("➡️ Chuyển đến:", target_url_after_login)
        page.goto(target_url_after_login)
        page.wait_for_load_state("networkidle", timeout=15000)
        page.wait_for_timeout(2000)

        page.screenshot(path="step_images/debug_after_login.png")
        print("✅ Đã chuyển đến:", page.url)

    except Exception as e:
        print("❌ Đăng nhập thất bại:", e)
        raise e
