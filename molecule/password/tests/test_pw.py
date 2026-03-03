from default.common.test_common import *  # noqa: F401,F403


def test_new_user_default(host):
    new_user = host.user("new_user")
    password_hash = {
        "noble": "$6$rounds=656000$808553$TJTSMegyZQiehjaAn3UuVhMdKgAhWm2E6MV."
        "EqjRh4wSNHW7Fn0ZfKL.iJ2rYs6VzV/NyYMi0oqKUEVdyAaee0",
        "trixie": "$6$rounds=656000$164790$TI8NxQicQ4fcU.qGsFJUZqr1Futpd6FNDnt"
        "za0aiGkyvJijKciS3pJuk4cf9UR9yt3IUtc1Oh/SVY9pAM9Isi.",
    }

    assert new_user.password == password_hash[host.system_info.codename]
