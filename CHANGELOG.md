# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and version numbers use
[CalVer](https://calver.org/#when-to-use-calver) YY.MM (e.g., v24.08).

## [Unreleased]

Django 4.2 and Python 3.12

### Added

- [ _for new features_ ]

### Changed

- Use '/api/v1' as API url for better versioning support
  ([#29](https://github.com/hdigital/parlgov-web/pull/29))
- Specify license with PEP 639 metadata format in 'pyproject.toml'
  ([#28](https://github.com/hdigital/parlgov-web/pull/28))

### Removed

- [ _for removed features_ ]

### Fixed

- [ _for bug fixes_ ]

## [v24.12] — 2024-12-10

Django 4.2 and Python 3.12

### Added

- Add MIT license file
- Add static page docs and deploy docs with a GitHub Actions workflow

### Changed

- Use redirection instead of 'cat' in shell scripts
- Exclude migrations and tests from coverage reports
- Replace Debian 'Bullseye' with 'Bookworm' in Docker
- Allow robots to crawl site
- Make R migration database optional
- Update docs
  - Specify 'venv' and path in docs
  - Replace 'page' with 'site' for website
  - Minor revisions 'readme'

### Fixed

- Specify database url Docker

## [v24.08] — 2024-08-24

- Django 4.2 and Python 3.12
- initial public version
