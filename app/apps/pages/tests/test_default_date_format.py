def test_default_date_format_setting():
    from config.settings import DATE_FORMAT

    assert DATE_FORMAT == "Y-m-d"
