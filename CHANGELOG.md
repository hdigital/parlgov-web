# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and version numbers use
[CalVer](https://calver.org/#when-to-use-calver) YY.MM (e.g., v24.08)
— see [tags](https://github.com/hdigital/parlgov-web/tags).

## [Unreleased] — YYYY-MM-DD

Django 5.2 and Python 3.12

### Added

- Upgrade to Django 5.2
  ([#53](https://github.com/hdigital/parlgov-web/pull/53))
- Add CodeMeta software metadata
  ([#31](https://github.com/hdigital/parlgov-web/issues/31))
- Add paper, source code, and data references
  ([#36](https://github.com/hdigital/parlgov-web/pull/36))
- Add CC0 waiver for documentation
  ([#35](https://github.com/hdigital/parlgov-web/pull/35))

### Changed

- Use '/api/v1' as API url for better versioning support
  ([#29](https://github.com/hdigital/parlgov-web/pull/29))
- Specify license with PEP 639 metadata format in 'pyproject.toml'
  ([#28](https://github.com/hdigital/parlgov-web/pull/28))
- Add links to PR, issue, or commit for all entries in the 'changelog'
  ([#30](https://github.com/hdigital/parlgov-web/pull/30))
- Use 'CITATION.cff' for Zenodo metadata
  ([#32](https://github.com/hdigital/parlgov-web/pull/32))
- Harmonize project information and metadata
  ([#38](https://github.com/hdigital/parlgov-web/issues/38))
- Restructure 'factories' import
  ([#23](https://github.com/hdigital/parlgov-web/pull/23))
- Use platform specification in Docker Compose
  ([#40](https://github.com/hdigital/parlgov-web/pull/40))

### Removed

- Remove '.python-version'
  ([#52](https://github.com/hdigital/parlgov-web/pull/52))

### Fixed

- Minor revisions

## [v24.12] — 2024-12-10

Django 4.2 and Python 3.12

### Added

- Add MIT license file
  ([730e9f8](https://github.com/hdigital/parlgov-web/commit/730e9f8))
- Add static page docs and deploy docs with a GitHub Actions workflow
  ([#3](https://github.com/hdigital/parlgov-web/issues/3))
- Add Zenodo metadata
  ([99ce699](https://github.com/hdigital/parlgov-web/commit/99ce699))

### Changed

- Use redirection instead of 'cat' in shell scripts
  ([#12](https://github.com/hdigital/parlgov-web/issues/12))
- Exclude migrations and tests from coverage reports
  ([41075f2](https://github.com/hdigital/parlgov-web/commit/41075f2))
- Replace Debian 'Bullseye' with 'Bookworm' in Docker
  ([d7dbd42](https://github.com/hdigital/parlgov-web/commit/d7dbd42))
- Allow robots to crawl site
  ([b1c1477](https://github.com/hdigital/parlgov-web/commit/b1c1477))
- Make R migration database optional
  ([253a4bc](https://github.com/hdigital/parlgov-web/commit/253a4bc))
- Use 'yaml' file extension instead of 'yml'
  ([a62b63d](https://github.com/hdigital/parlgov-web/commit/a62b63d))
- Update docs
  - Specify 'venv' and path in docs
    ([aa3a8cf](https://github.com/hdigital/parlgov-web/commit/aa3a8cf))
  - Replace 'page' with 'site' for website
    ([f1c1827](https://github.com/hdigital/parlgov-web/commit/f1c1827))
  - Minor revisions 'readme'
    ([7cdce99](https://github.com/hdigital/parlgov-web/commit/7cdce99))

### Fixed

- Specify database url Docker
  ([ebeee42](https://github.com/hdigital/parlgov-web/commit/ebeee42))

## [v24.08] — 2024-08-24

- Django 4.2 and Python 3.12
- initial public version

## [Template] — YYYY-MM-DD

Django 5.x and Python 3.1x

### Added

- _for new features_

### Changed

- _for changes in functionality_

### Removed

- _for removed features_

### Fixed

- _for bug fixes_
- Minor revisions
