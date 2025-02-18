# Selenium Python Automation

This repository contains tests for **Selenium WebDriver** written in Python using the **pytest** framework. The tests validate functionality on a sample page with a table and search box.

## Requirements

- Python 3.x
- Selenium
- pytest

## Setup

1. Install Python and pip.
2. Install required dependencies:
   ```bash
   pip install selenium pytest

## Tests
1. Test to Validate Table Entries
This test verifies that the table on the page has exactly 24 rows. It handles pagination to navigate through the table pages.
 ```bash
 def test_ValidateTable(self):
    table = self.driver.find_element(By.CSS_SELECTOR, "table[id='example']")
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
    assert rows_count == 24, "FAIL: Table is having less than 24 entries"
    print("Total number of rows = ", rows_count)
 ```

2. Test to Validate Search Box
This test enters the text "New York" into the search box and validates that exactly 5 rows are shown as search results.
```bash
def test_searchBox(self):
    search_box = self.driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("New York")
    table = self.driver.find_element(By.CSS_SELECTOR, "table[id='example']")
    rows = table.find_elements(By.XPATH, "//tbody/tr")
    search_result_rows = len(rows)
    assert search_result_rows == 5, "FAIL: Search results count is not equal to 5"
```

## Running Tests
To run the tests, use the following command:
```bash
pytest test_validate_search.py
``` 
