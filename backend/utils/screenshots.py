import os
from backend.utils.params import screenshot_dir

def take_screenshot(page, name):
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    page.get_screenshot_as_file(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")