from app import app
from webdriver_manager.chrome import ChromeDriverManager
print(ChromeDriverManager().install())

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Sales before and after the January 2021 price change" in header.text

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None
