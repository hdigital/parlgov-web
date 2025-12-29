#!/usr/bin/env Rscript

# Compare legacy and new ParlGov databases to verify migration

library(conflicted)
conflicts_prefer(dplyr::filter, .quiet = TRUE)

library(tidyverse)

library(DBI)
library(dbplyr)


## Database ----

con_old <- dbConnect(RSQLite::SQLite(), "parlgov-experimental.db")
con_new <- dbConnect(RSQLite::SQLite(), "../../app/parlgov.sqlite")

tbl_old <- dbListTables(con_old)
tbl_new <- dbListTables(con_new)


## Migration check----

tbl_check <- read_csv("migration-check.csv")

tbl_check_new <-
  tbl_check |>
  filter(migrate == 1, !is.na(table_new)) |>
  arrange(table_new) |>
  pull(table_new)

tbl_new_select <- tbl_new[!grepl("auth_|django_|sqlite_", tbl_new)]

check_old <- all(tbl_check$table_legacy == tbl_old)
check_new <- all(tbl_check_new == tbl_new_select)

if (!check_old || !check_new) {
  stop("Migration check table documentation failed.")
}


## Clean-up ----

dbDisconnect(con_old)
dbDisconnect(con_new)
