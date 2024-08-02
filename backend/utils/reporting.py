import os
import datetime
import shutil
from PIL import Image
from screenshots import take_screenshot


class Reporting:
    def __init__(self, report_dir="reports"):
        self.report_dir = report_dir
        self.screenshot_dir = os.path.join(report_dir, "screenshots")
        self.log_file = os.path.join(report_dir, "report.log")
        self.create_report_directory()

    def create_report_directory(self):
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.datetime.now()}: {message}\n")

    def capture_screenshot(self, driver, step_name):
        screenshot_path = os.path.join(self.screenshot_dir, f"{step_name}.png")
        take_screenshot(driver, step_name)
        # Optional: Resize screenshot for better visibility in the report
        img = Image.open(screenshot_path)
        img = img.resize((800, 600))
        img.save(screenshot_path)

    def generate_report(self, results):
        self.log("Test Report")
        self.log("=" * 40)
        for result in results:
            self.log(f"Test Case: {result['test_case']}")
            self.log(f"Status: {result['status']}")
            if 'screenshot' in result:
                self.log(f"Screenshot: {result['screenshot']}")
            self.log("-" * 40)

        # Additional section for price comparison
        self.log("Price Comparison Results")
        self.log("=" * 40)
        self.log(f"Product: {results[-1].get('product_name', 'N/A')}")
        self.log(f"Lowest Price Platform: {results[-1].get('lowest_price_platform', 'N/A')}")
        self.log(f"Price: {results[-1].get('lowest_price', 'N/A')}")
        self.log("=" * 40)

    def move_screenshots(self):
        # Move screenshots to the report directory
        if not os.path.exists("screenshots"):
            return
        for file_name in os.listdir("screenshots"):
            shutil.move(os.path.join("screenshots", file_name), os.path.join(self.screenshot_dir, file_name))
        # Optional: Remove the original screenshots directory if empty
        if not os.listdir("screenshots"):
            os.rmdir("screenshots")
