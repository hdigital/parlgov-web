DROP VIEW IF EXISTS view_party;

CREATE VIEW view_party AS
SELECT
  data_country.name_short AS country,
  data_code.short AS party_family,
  data_party.*
FROM
  data_party
  LEFT JOIN data_country ON data_party.country_id = data_country.id
  LEFT JOIN data_code ON data_party.family_id = data_code.id
ORDER BY
  country,
  name_short;

DROP VIEW IF EXISTS view_election;

CREATE VIEW view_election AS
SELECT
  data_country.name_short AS country,
  data_election.`date` AS `date`,
  data_code.short AS type,
  data_party.name_short AS party,
  data_election_result.*
FROM
  data_election_result
  LEFT JOIN data_election ON data_election_result.election_id = data_election.id
  LEFT JOIN data_country ON data_election.country_id = data_country.id
  LEFT JOIN data_party ON data_election_result.party_id = data_party.id
  LEFT JOIN data_code ON data_election.type_id = data_code.id
ORDER BY
  country,
  `date`,
  seats DESC,
  vote_share DESC;

DROP VIEW IF EXISTS view_cabinet;

CREATE VIEW view_cabinet AS
SELECT
  data_country.name_short AS country,
  data_cabinet.start_date AS start_date,
  data_party.name_short AS party,
  data_cabinet_party.*
FROM
  data_cabinet_party
  LEFT JOIN data_cabinet ON data_cabinet_party.cabinet_id = data_cabinet.id
  LEFT JOIN data_country ON data_cabinet.country_id = data_country.id
  LEFT JOIN data_party ON data_cabinet_party.party_id = data_party.id
ORDER BY
  country,
  start_date,
  pm DESC,
  party;
