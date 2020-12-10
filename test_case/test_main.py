import pytest
import yaml

from page.app import App



class TestMain:
    @pytest.mark.parametrize("v1", "v2", yaml.safe_load(open("../test_main.yaml")))
    def test_main(self):
        app = App()
        app.start().main().search()



