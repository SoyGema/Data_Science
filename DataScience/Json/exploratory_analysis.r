##IMPORT JSON DATA

library(jsonlite)
data <- fromJSON("data_file.json")
#if file deal with NDJSON
data <- stream_in(file("data_file.json")

##FLATTEN DATA FRAME  -organize data-

head(data_file, 10)
str(data_file)
data_flat <- flatten(yelp)
str(data_flat)

library(tibble)
data_tbl <- as_data_frame(data_flat)
data_tbl

##SEE NESTED LISTS INSIDE JSON
data_tbl %>% mutate(categories = as.character(categories)) %>%
select(categories)                  

##REMOVE UNNECESSARY VARIABLES

data_tbl %>%
  select(-starts_with("variable", -starts_with("attribute"))
