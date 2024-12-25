import biathlonresults as api


def test_seasons():
    res = api.seasons()
    assert res[-1] == {
        "SeasonId": "5758",
        "Description": "1957/1958",
        "SortOrder": 1,
        "IsCurrent": False,
        "IsCurrentResults": False,
        "IsCurrentScheduled": False,
    }


def test_organizers():
    res = api.organizers()
    assert isinstance(res, list)


def test_analytic_results():
    res = api.analytic_results("BT2425SWRLCP01MXSR", api.consts.AnalysisType.TOTAL_COURSE_TIME)
    assert isinstance(res, dict)
    assert res["Results"][0]["Name"] == "NORWAY"


def test_cups():
    res = api.cups(1819)
    assert isinstance(res, list)
    assert len(res) == 37


def test_cup_results():
    res = api.cup_results("BT1819SWRLCP__SMTS")
    assert isinstance(res, dict)
    assert isinstance(res["Rows"], list)
    assert res["Rows"][0]["Name"] == "BOE Johannes Thingnes"


def test_athletes():
    res = api.athletes("boe", "johannes")
    assert isinstance(res, dict)
    assert isinstance(res["Athletes"], list)
    assert "boe" in res["Athletes"][0]["FamilyName"].lower()
    assert "johannes" in res["Athletes"][0]["GivenName"].lower()


def test_cisbios():
    res = api.cisbios("BTNOR11605199301")
    assert isinstance(res, dict)
    assert res["FullName"] == "Johannes Thingnes BOE"


def test_all_results():
    # Raphael Poiree
    res = api.all_results("BTFRA10908197401")
    assert isinstance(res, dict)
    assert isinstance(res["Results"], list)
    assert res["Results"][0]["SO"] == 2
    assert len(res["Results"]) == 329


def test_events():
    res = api.events(1819, api.consts.LevelType.BMW_IBU_WC)
    assert isinstance(res, list)
    assert len(res) == 10
    assert res[0]["Level"] == 1
    assert res[-1]["ShortDescription"] == "Oslo Holmenkollen"


def test_competitions():
    # Pokljuka 1819
    res = api.competitions("BT1819SWRLCP01")
    assert isinstance(res, list)
    assert len(res) == 8
    assert res[-1]["ShortDescription"] == "Women 10km Pursuit"


def test_results():
    # Pokljuka 1819 W PU
    res = api.results("BT1819SWRLCP01SWPU")
    assert isinstance(res, dict)
    assert isinstance(res["Results"], list)
    assert len(res["Results"]) == 60
    assert res["Results"][0]["ResultOrder"] == 1
    assert res["Results"][0]["Name"] == "MAKARAINEN Kaisa"


def test_stats():
    # podiums men stat
    res = api.stats("WCPOD_M", "WCPOD", "ATH", "M")
    assert isinstance(res, dict)
    assert isinstance(res["Rows"], list)
    # in case someone breaks Bjoerndalen's record
    assert int(res["Rows"][0]["Value"]) >= 199
