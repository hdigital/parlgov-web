#!/usr/bin/env Rscript

# Migrate legacy ParlGov SQLite database to CSV files for Django import

library(conflicted)
conflicts_prefer(dplyr::filter, .quiet = TRUE)

library(tidyverse)

library(DBI)
library(dbplyr)


## Database ----

con_pg <- dbConnect(RSQLite::SQLite(), "parlgov-experimental.db")

dbListTables(con_pg)

path_data <- "import-data-legacy/"
unlink(paste0(path_data, "*.*"))


## Functions ----

get_parlgov_table <- function(table_name) {
  tbl(con_pg, table_name) |>
    as_tibble() |>
    rename_with(~ gsub("_id", "", .x, fixed = TRUE))
}


## Core ----

### Info ----

tables_to_exclude <- c("faq_section", "minister_salience", "person_family_relation")

info_id <-
  get_parlgov_table("info_id") |>
  filter(!table_variable %in% tables_to_exclude, ) |>
  mutate(
    description = if_else(is.na(description), "", description),
    comment = ""
  )

write_csv(info_id, paste0(path_data, "01__datacore__Code.csv"))


### Country ----

country_flags <- read_csv("country-flags.csv", show_col_types = FALSE)

country_iso <-
  get_parlgov_table("external_country_iso") |>
  select(iso_numeric = id, code_iso2 = iso2)

country <-
  get_parlgov_table("country") |>
  left_join(country_iso) |>
  left_join(country_flags) |>
  select(id:eu_accession_date, code_iso2, flag, comment, data_json) |>
  mutate(
    eu_accession_date = if_else(is.na(eu_accession_date), NA_character_, eu_accession_date),
    oecd_accession_date = if_else(
      is.na(oecd_accession_date),
      NA_character_,
      oecd_accession_date
    ),
    comment = if_else(is.na(comment), "", comment)
  )

write_csv(country, paste0(path_data, "02__datacore__Country.csv"), na = "")


## Documentation ----

### News ----

news <- get_parlgov_table("info_news")

unique(news$author) |> sort()

write_csv(news, paste0(path_data, "12__docs__News.csv"), na = "")

### Page ----

data_source <- get_parlgov_table("info_page_content")

write_csv(data_source,
  paste0(path_data, "13__docs__Page.csv"),
  na = ""
)

## Parties ----

### Party ----

party <-
  get_parlgov_table("party") |>
  select(id:data_json)

write_csv(party, paste0(path_data, "21__parties__Party.csv"), na = "")


### Party family ----

party_family <-
  get_parlgov_table("party_family") |>
  rename(family = type)

write_csv(party_family,
  paste0(path_data, "22__parties__PartyFamily.csv"),
  na = ""
)

all(party_family$party %in% party$id)
all(party_family$family %in% info_id$id)


### Party name change ----

party_name_change <- get_parlgov_table("party_name_change")

write_csv(party_name_change,
  paste0(path_data, "23__parties__PartyNameChange.csv"),
  na = ""
)


### Party change ----

party_change <- get_parlgov_table("party_change")

write_csv(party_change,
  paste0(path_data, "24__parties__PartyChange.csv"),
  na = ""
)


## Elections ----

### Election ----

election <-
  get_parlgov_table("election") |>
  select(-first_round_election, -old_countryID, -old_parlID)

write_csv(election,
  paste0(path_data, "31__elections__Election.csv"),
  na = ""
)


### Election result ----

election_results <-
  get_parlgov_table("election_result") |>
  rename(party_id_source = party_source) |>
  arrange(!is.na(alliance), alliance) # avoid import foreign key issue

all(election_results$election %in% election$id)

alliance_id <-
  election_results |>
  filter(!is.na(alliance)) |>
  pull(alliance)
all(alliance_id %in% election_results$id)

all(election_results$alliance != election_results$id, na.rm = TRUE)

all(election_results$party %in% party$id)


write_csv(election_results,
  paste0(path_data, "32__elections__ElectionResult.csv"),
  na = ""
)


## Cabinet ----

### Cabinet ----

cabinet <-
  get_parlgov_table("cabinet")

write_csv(cabinet, paste0(path_data, "41__cabinets__Cabinet.csv"), na = "")

### Cabinet party ----

cabinet_party <-
  get_parlgov_table("cabinet_party") |>
  rename(party_id_source = party_source)

write_csv(cabinet_party,
  paste0(path_data, "42__cabinets__CabinetParty.csv"),
  na = ""
)


## Clean-up ----

dbDisconnect(con_pg)
