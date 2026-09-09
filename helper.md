# Pytest and Playwright Commands

Run these commands from the project root:

## Install dependencies and browsers

```bash
pip install -r requirements.txt
playwright install
```

Install only Chromium:

```bash
playwright install chromium
```

On Linux, install Chromium and its system dependencies:

```bash
playwright install --with-deps chromium
```

## Run test suites

Run all smoke tests:

```bash
pytest -m smoke
```

Run all regression tests:

```bash
pytest -m regression
```

Run all tests:

```bash
pytest
```

The default browser is Chromium, as configured in `pytest.ini`.

Run tests in another browser:

```bash
pytest -m regression --browser firefox
pytest -m regression --browser webkit
```

Run the suite in every supported browser:

```bash
for browser in chromium firefox webkit; do pytest -m regression --browser $browser; done
```

## Run a specific test

This project uses standalone test functions, not test classes:

```bash
pytest tests/test_smoke.py::test_locked_out_user_is_blocked
```

Run the specific test in GUI mode:

```bash
pytest tests/test_smoke.py::test_locked_out_user_is_blocked --headed
```

Run it in GUI mode with 500 milliseconds between actions:

```bash
pytest tests/test_smoke.py::test_locked_out_user_is_blocked --headed --slowmo 500
```

`--slowmo` is measured in milliseconds. For example, `500` means `0.5` seconds.

The `::` separates the test file from the specific test function. The `-m smoke`
option is optional here because the test name already selects one test:

```bash
pytest -m smoke tests/test_smoke.py::test_locked_out_user_is_blocked --headed --slowmo 500
```

## Debug with Playwright Inspector

```bash
PWDEBUG=1 pytest tests/test_smoke.py::test_locked_out_user_is_blocked
```

## Generate reports

`pytest.ini` is configured to create or replace this report on every run:

```text
logs/report.html
```

Run tests and create the report:

```bash
pytest -m smoke
```

Open the report in a browser after the run:

```bash
xdg-open logs/report.html
```

Save terminal output separately as a log file:

```bash
pytest -m smoke | tee logs/pytest.log
```

The HTML report and terminal log are overwritten when the same commands are run
again.
