# Changelog

All notable changes to OsuStatQt will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.4] Alpha - 2022-01-02

### Added / Changes
- Overhauled recent activity and scores pane.
- Stylized Scrollbars
- Panes now show rankscore images
- Other statistics such as beatmap title, diff, relative time is also shown
- The panes now have a "Show more" for pagination.

### Bug Fixes
- Fixed AttributeError: attribute UserSupportEvent
## [0.0.3] Alpha - 2021-12-30

### Added / Changes
- Added a cooldown to refresh button to prevent spamming
- Switched to pickling of config instead of dumping plain text.
- `Get Credentials` Button now opens the account settings.
- Achievement Names show up in Recent Activities

### Bug Fixes
- App crashing when the config file is blank or with missing values

## [0.0.2] Alpha - 2021-12-28

### Added / Changes
- Refresh Button can now be enabled from the settings automatically
- Recent activity and scores work now!

### Bug Fixes
- Could not set default user from settings UI
- Application crash when credentials were correct
- Default User Exception
- 2 Recent Scores Panel Showing up on refresh
- User Data Actually Shows Up now!


## [0.0.1] Alpha - 2021-12-27


### Added
- First release
- Created .osustat config wrapper
- API Credentials Authorization
- Shows Recent Activity and Recent Scores Beatmap Titles for User set as default.



[0.0.4]: https://github.com/sortedcord/osu-statqt/releases/tag/v0.0.4-alpha
[0.0.3]: https://github.com/sortedcord/osu-statqt/releases/tag/v0.0.3-alpha
[0.0.2]: https://github.com/sortedcord/osu-statqt/releases/tag/v0.0.2-alpha
[0.0.1]: https://github.com/sortedcord/osu-statqt/releases/tag/v0.0.1-alpha
