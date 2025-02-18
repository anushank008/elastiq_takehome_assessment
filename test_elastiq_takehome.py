import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("launchBrowser")
class TestValidateSearch:
    def test_ValidateTable(self):
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='example']")
        global rows_count
        rows_count = 0
        if table.is_displayed():
            while True:
                rows = table.find_elements(By.XPATH, "//tbody/tr")
                rows_count += len(rows)
                try:
                    button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@class='paginate_button next']"))
                    )
                    button.click()
                except Exception as e:
                    print(f"Last page reached or error: {e}")
                    break
        assert rows_count == 24 ,"FAIL : Table is having less than 24 entries"
        print("Total number of rows = ", rows_count)

    def test_searchBox(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_box.send_keys("New York")
        table = self.driver.find_element(By.CSS_SELECTOR, "table[id='example']")
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        search_result_rows = len(rows)
        print("Table is showing " ,search_result_rows ," of ", rows_count )
        assert search_result_rows == 5, " FAIL : search results count is not equal to 5"
        assert search_result_rows == 0, " FAIL: No results found"

        
        
