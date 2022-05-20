import json
import os
from dataclasses import asdict, dataclass

import validators

tests_folder = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("/", os.sep)
    + "\\tests"
)
tests_settings = tests_folder + "\\tests.settings.json"
tests_log = tests_folder + "\\tests.pytia_ui_tools.log"


@dataclass
class TestSettings:
    mail: str = ""


if not os.path.exists(tests_settings):
    with open(tests_settings, "w") as f:
        ts = TestSettings()
        f.write(json.dumps(asdict(ts)))
else:
    with open(tests_settings, "r") as f:
        ts = TestSettings(**json.load(f))
    assert validators.email(ts.mail)  # type: ignore

if not os.path.exists(tests_log):
    with open(tests_log, "w") as f:
        f.write(
            "2022-05-13 11:12:27,705	pytia-ui-tools	INFO	HOSTNAME	USERNAME	Running PYTIA-UI-TOOLS"
        )
