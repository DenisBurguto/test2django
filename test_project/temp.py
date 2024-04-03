CREATE TABLE `a`(`mbid` string, `artist_mb` string, `artist_lastfm`
string, `country_mb` string, `country_lastfm` string, `tags_mb` string,
`tags_lastfm` string, `listeners_lastfm` int, `scrobbles_lastfm` int,
`ambiguous_artist` boolean) row format delimited fields terminated by ',' stored as textfile;



CREATE TABLE try4 (id int, name string, host_id int,
host_name string, neighbourhood_group string, neighbourhood string,
latitude float, longitude float, room_type string, price int,
minimum_nights int, number_of_reviews int, last_review date, reviews_per_month float,
calculated_host_listings_count int, availability_365 int) row format delimited fields terminated by ',' stored as textfile;

load data inpath '/AB_NYC_2019.csv' into table try4;


