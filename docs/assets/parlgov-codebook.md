# ParlGov Codebook

Created on 22 February 2026, 16:21 from ParlGov database documentation entries.

Döring, Holger and Philip Manow. 2024. Parliaments and governments database (ParlGov): Information on parties, elections and cabinets in established democracies.

- [parlgov.org](https://parlgov.org)
- [dataverse.harvard.edu/dataverse/parlgov](https://dataverse.harvard.edu/dataverse/parlgov)
- [github.com/hdigital/parlgov-snippets](https://github.com/hdigital/parlgov-snippets)

## Coding rules

### References

- Döring, Holger. 2013. “The Collective Action of Data Collection: A Data Infrastructure on Parties, Elections and Cabinets.” European Union Politics 14(1): 161–78.
  - DOI: [10.1177/1465116512461189](https://www.doi.org/10.1177/1465116512461189)
  - [ presentation of technical concept ]
- Döring, Holger. 2016. “Mapping Established Democracies: Integrated Data on Parties, Elections and Cabinets.” Electoral Studies 44: 535–43.
  - DOI: [10.1016/j.electstud.2016.07.002](https://www.doi.org/10.1016/j.electstud.2016.07.002)
  - [ presentation of methodological design and operationalization ]

### Overview

We include elections and cabinets in _established democracies_. More specifically, we include democratic national lower house elections and EP elections for _all EU and most OECD members_. For the latter, we exclude presidential systems. We record all elections and succeeding cabinets after 1945 or after full democratization according to Boix ea. (2013).

We also include elections and cabinets before 1945. We record information after 1900 or after the last democratic transition (Boix ea. 2013). As of today, these observations are experimental and may need revision (e.g. largest party with no seats missing).

### Parties

#### Coding rules

We include parties winning _more than 1.0% vote share_ in elections we cover

Details

- winning 2 seats in an election (eg. member of an electoral alliance)
- party groups that form in parliament
  - more than 5.0% seat share (eg. [ITA FLI](https://parlgov.fly.dev/data/parties/ita/1477/))
  - forming in two parliamentary terms (eg. [FRA GDR](https://parlgov.fly.dev/data/parties/fra/2272/))
  - members of cabinet (eg. [SWE NP-AV](https://parlgov.fly.dev/data/parties/swe/2608/))
  - providing minority support to a cabinet
- electoral alliances and members with at least 2 election results
- no party affiliation
  - candidates with more than 1.0% vote share (eg. [IRL I-TJM](https://parlgov.fly.dev/data/parties/irl/2327/))
  - includes 'independent' (also for presidents)
  - one 'no party affiliation' included per country
- less than 1.0% vote share
  - winning 1 seat in 2 elections
  - 2 election results as largest party no seats (first loser)
- special categories: 'no-seat' and 'one-seat' (see [election](https://parlgov.fly.dev/docs/codebook/#elections))

We avoid including minor parties or candidates that win a seat only in one election due to low threshold requirements.

#### Party change

New parties are coded in two tables: 'party change' and 'party name change'.

Mergers and party splits are only added as a new party if the (largest) predecessor party won less than 75% of the combined vote of all preceding parties in the last election. Otherwise the largest party is just renamed (cf. Döring 2016, 539).

Details

- splits and re-mergers coded for original party (eg. [JPN DP](https://parlgov.fly.dev/data/parties/jpn/439/))
- see also Barnea/Rahat (2011, 311): 'a new label and that no more than half of its top candidates (top of candidate list or safe districts) originate from a single former party'

#### Party names

Party names are sentence case if no national (language) convention requires title case.

- eg. party names for Germany are title case (German and English)

Party names and delimiters

- '–' different languages
- '/' ('+') alliances
- '|' generic names
- [ space before and after delimiter ]

Year added to smaller party name if identical names exist in a country (eg. [ SVK SZ-92](https://parlgov.fly.dev/data/parties/svk/2235/)).

#### Party positions

We provide aggregated party positions in four major dimensions. These positions are time-invariant unweighted mean values of information from party expert surveys on a 0 to 10 scale. All expert surveys are linked with ids from the 'party' table and original values are rescaled before calculating the mean.

Missing party positions for each dimension are imputed by mean values for the respective party family. We distinguish mean and imputed values by the number of decimal places. Mean values based on external datasets have five decimal places and imputed values have one decimal place only.

Variables and sources

- left/right — Castles/Mair 1983 (_left/right_), Huber/Inglehart 1995 (_left/right_), Benoit/Laver 2006 – (_left/right_), CHES 2010 (_lrgen_ 1999 and 2002 and 2006)
- state/market — Benoit/Laver 2006 (_taxes/spending_), CHES 2010 (_lrecon_ 1999 and 2002 and 2006)
- liberty/authority — Benoit/Laver 2006 (_social_), CHES 2010 (_galtan_ 1999 and 2002 and 2006)
- EU anti/pro — Ray 1999 (_pos96_), Benoit/Laver 2006 (_euauthority_ or _eulargerstronger_ or _eujoining_), CHES 2010 (_position_ 1999 and 2002 and 2006)

#### Party families

We classify parties into families by their position in an economic (state/market) and a cultural (liberty/authority) left/right dimension.

The classification leads to eight party family categories: Communist/Socialist, Green/Ecologist, Social democracy, Liberal, Christian democracy, Agrarian, Conservative, Right-wing.

Parties that can not be classified into the eight categories are coded as 'spec' in the 'party' table with more details in the 'party family' table (e.g. [AUT Martin](https://en.wikipedia.org/wiki/Hans-Peter_Martin%27s_List)). These are mainly special issue parties without a clear left/right profile.

We use one classification for the entire history of a party and do not record changes (e.g. [FIN SP|P](https://parlgov.fly.dev/data/parties/fin/200/)).

We add further information about party families in a separate table (see 'party family').

### Elections

#### Coding rules

We include election results for

1. all parties that won _1.0% vote share_
2. all parties that won _2 seats_ (esp. alliance members)

Details

- a party that won _less than 1.0%_ vote share and _1 seat_
  - several election results — included into the list of ParlGov parties
  - single election result — coded as a 'one-seat' party (eg. [Poland](https://parlgov.fly.dev/data/elections/pol/1991-10-27/))
- a party that won _less than 1.0%_ vote share but was the _largest party that won no seats_ (first loser)
  - several election results — included into the list of ParlGov parties
  - single election result — coded as a 'no-seat' party (eg. [Austria](https://parlgov.fly.dev/data/parties/aut/2055/))
- parliamentary party groups – _see below_
  - party group seat compositions different to election results
  - significant changes in the composition of party groups (more than 5.0% seat share)
- mixed-member electoral systems
  - proportional (PR) tier _votes_ and _vote share_ recorded
- technical party "others"
  - only number of seats coded

#### Electoral alliances

Electoral alliances are coded by linking election results (variable 'alliance_id ') of alliance members to an alliance or the strongest party in an electoral alliance.

- each electoral alliance or alliance member coded as an individual party should include _2 elections_
- members of alliances with a dominant party are coded to this party
- alliances of parties that are part of a broader alliance are coded with a 'data_json' entry 'alliance_alliance_id' (eg. [Italy 1996](https://parlgov.fly.dev/data/elections/ita/1996-04-21/))
- _votes_ are coded at the level of electoral results for all alliance members
- _seats_ are coded for alliance members (parliamentary groups), if feasible
  - seats of an alliance that forms a parliamentary group with members running independently are coded for alliance members and with a 'parliament change' (eg. Germany [CDU/CSU](https://parlgov.fly.dev/data/parties/deu/1727/))
  - seats of alliance members are coded if no information about the parliamentary party group status is available
  - a 'data_json' entry 'seats_alliance' is added to the alliance to check data consistency
  - a 'one seat' party which is part of an electoral alliance is coded as an alliance member (eg. [Hungary 2014](https://parlgov.fly.dev/data/elections/hun/2014-04-06/))

#### Parliament composition

- changes (> 5%) in seats composition are recorded in 'parliament change'
  - esp. if changes affect cabinet majority support
- seats composition of parliament at a particular date is recorded in 'parliament composition'
  - esp. if composition is relevant for cabinet formation (eg. [JPN elections](https://parlgov.fly.dev/data/elections/jpn/1996-10-20/) after 1996)
- _coding incomplete_
  - significant changes only
  - lack of systematic and reliable sources

#### Data sources

National elections

- Main sources
  - official data source – national statistical office – see [country notes](https://parlgov.fly.dev/docs/codebook/#countries)
  - Nohlen — Elections: A Data Handbook – various volumes of elections around the world
  - Mackie/Rose (1945–1990) — only Western democracies
  - Essex elections data on Post-Communist Europe (1990–200x)
  - [EJPR Political Data Yearbook](http://www.politicaldatayearbook.com/) (1990–today)
  - [CEVIPOL Electoral results](http://dev.ulb.ac.be/cevipol/en/elections.html) — Europe and Latin-America
- Others
  - [Parline](http://www.ipu.org/parline-e/parlinesearch.asp)
  - Rokkan/Meyriat (1920–1965) — only Western democracies
  - Rose/Munro (1990–2001) — Post-Communist Europe

European parliament elections

1. official data source – national statistical office
2. European Parliament (EP) election report (esp. 1979–1999) — based on official statistics
3. EJPR yearbook (1990–today)

### Cabinets

#### Coding rules

We record a new cabinet for these events (cf. Budge/Keman 1993: 10)

1. any change of parties with cabinet membership
2. any change of the prime minister
3. any general election

All parties with ministers in cabinet are included (Indridason/Bowler 2014: 396)

1. right to attend cabinet meetings
2. right to cast vote before cabinet (if applicable)

Details

- three month rule
  - a continuation (caretaker) cabinet (subset of previous coalition, no new party) is coded once for any change lasting longer than three months
  - the three month rule refers to the exact day of the date, not the number of days
  - 'data_json' entry 'three_month_rule' (and 'cabinet_change')
  - see also examples section below
- any meaningful investiture procedure defines a new cabinet
  - a PM appointment without a cabinet appointment (eg. [ITA Andreotti I](https://parlgov.fly.dev/data/cabinets/ita/1972-02-17/), [POL Pawlak I](https://parlgov.fly.dev/data/cabinets/pol/1992-06-05/))
  - a constitutionally required new investiture during a parliamentary term (eg. LTU Skvernelis [II](https://parlgov.fly.dev/data/cabinets/ltu/2017-10-19/)+[III](https://parlgov.fly.dev/data/cabinets/ltu/2019-08-20/), see [LTU notes](https://parlgov.fly.dev/docs/codebook/#lithuania))
- any meaningful resignation defines a new cabinet
  - a formal resignation request (eg. [AUT Figl III](https://parlgov.fly.dev/data/cabinets/aut/1949-11-08/))
  - a successful dissolution request under negative parliamentarism (eg. [SWE Erlander VII](https://parlgov.fly.dev/data/cabinets/swe/1958-06-01/))
  - a lost vote of confidence (or early election vote) and change to caretaker status (eg. [SVK Radicova II](https://parlgov.fly.dev/data/cabinets/svk/2011-10-20/), [ISR Netanyahu II 1998](https://parlgov.fly.dev/data/cabinets/isr/1998-01-04/))
- first appointment event coded
  - successive appointments for one cabinet (e.g. [DNK Thorning-Schmidt I](https://parlgov.fly.dev/data/cabinets/dnk/2011-10-02/)
  - e.g. appointments of PM, cabinet, ministers
- cabinet parties not included
  - ministers without portfolio, interim or junior ministers
  - cabinet members without party affiliation (party family 'none') are only coded if the prime minister has no party affiliation (e.g. [DEU Papen I](https://parlgov.fly.dev/data/cabinets/deu/1932-06-02/))
  - parties supporting a (minority) cabinet are included in table 'cabinet support' — if information available
- splits and mergers of cabinet parties
  - coded as cabinet changes (eg. [AUS Schuessel III](https://parlgov.fly.dev/data/cabinets/aut/2003-02-28/), [CZE Klaus II](https://parlgov.fly.dev/data/cabinets/cze/1993-01-01/))
  - 'data_json' entry 'party_split' and 'party_merger'
- parliamentary groups and alliances
  - political parties are coded as parliamentary groups (eg. [DEU CDU/CSU](https://parlgov.fly.dev/data/parties/deu/1727/))
  - alliance members that join a parliamentary group are coded as support parties (eg. [POL Szydlo](https://parlgov.fly.dev/data/cabinets/pol/2015-11-16/) 2015)
- seats at cabinet formation date
  - not coded for each instance of cabinet formation
  - calculated based on
    1. 'election result' _or_ 'parliament compositiion' table – most recent date used
    2. 'parliament change' table entries after (1)
  - used in 'view cabinet' and stored in 'viewcalc parliament composition'
  - see Müller and Strom (2000), Bergman ea. (2019) and ERDDA for exact seats at cabinet formation
- duplicate prime minister names
  - first letter of first name added to PMs with the same last name (e.g. [DNK Rasmussen N](https://parlgov.fly.dev/data/cabinets/dnk/))
- country specific
  - Switzerland: changes in the identity of the President of the Swiss Confederation (Bundespräsident) do not define a new cabinet (cf. Kriesi/Trechsel 2008, 75-76)
  - Iceland: two [prime ministers](https://parlgov.fly.dev/data/cabinets/isl/1963-11-14/) named Bjarni Benediktsson (born 1908 and 1970)

Examples

- three month constraint
  - [POL Kaczynski](https://parlgov.fly.dev/data/cabinets/pol/2006-07-14/) (2006) — coded as one cabinet
    - SRP withdraws from cabinet on 22 September 2006 (party composition change) and re-enters on 16 October
    - SRP and LPR dismissal on 13 August 2007 (party composition change) — elections take place on 19 October 2007 (within three months)
  - [BEL Leterme III](https://parlgov.fly.dev/data/cabinets/bel/2010-06-13/) (2010) — coded as one cabinet (three month constraint)
    - Previous coalition collapses on 26 April 2010 (party composition change) — new elections on 13 June. Pre-election caretaker cabinets lasts for less and post-election cabinet for more than three months.
  - further examples: [AUT Gorbach II](https://parlgov.fly.dev/data/cabinets/aut/1962-11-18/) (1962), [NLD Balkenende V](https://parlgov.fly.dev/data/cabinets/nld/2010-02-23/) (2010)

Damgaard (1994: 194-95) and Müller/Strom (2000: 12) provide a more comprehensive discussion of cabinet definitions.

#### Caretaker

Cabinets with a limited legislative mandate (cf. McDonnell/Valbruzzi 2014, 664)

- non-partisan: cabinet members without partisan affiliation
- provisional: appointed post-transition cabinet
- technical: institutional reasons
- continuation: remaining in office (see 'three month rule' above)
  - resignation of PM or cabinet
  - dissolution of parliament
  - after election until new cabinet forms

#### Cabinet type

Cabinet status (minority, minimum winning or surplus majority) is determined only by the seat share of cabinet parties in parliament and not coded manually.

If there is an electoral alliance with separate seat shares but one of the parties is not a cabinet member, the cabinet will be treated as a minority cabinet (eg. UK 1951). Similarly, if any of the governing parties can be removed and the other governing parties still hold a majority in parliament, the cabinet is considered to be a surplus majority cabinet.

#### Cabinet termination

_Experimental version only_ — coding incomplete

The events that define a new cabinet are used to define the termination date. Cabinets may remain in office for a short period after the initial terminal event. The 'description' gives a short description of eventsthat led to the end of a cabinet.

#### Confidence votes

_Experimental version only_ — coding incomplete

Confidence votes are added for all recent cabinets but are not included for all cabinets in ParlGov.

- investiture (confidence) votes for new cabinets
- confidence votes that lead to the termination of a cabinet
- important (won) confidence votes.

Details

- cabinet description includes a brief entry for a confidence vote
- constructive vote of no confidence
  - coded for outgoing cabinet (eg. [DEU Schmitt III](https://parlgov.fly.dev/data/cabinets/deu/1980-11-05/), [ESP Rajoy IV](https://parlgov.fly.dev/data/cabinets/esp/2016-10-29/))

#### Presidents

Party-affiliated heads of state but not short-term acting presidents. See table 'president'.

#### Data sources

For new cabinets and revisions of observations, we derive information about cabinet termination from news sources, preferably from the news agencies Reuters, AFP or the main national news agency

For West European countries we double checked our initial observations with the data in Müller/Strom (2000). For Central- and Eastern European countries we compared our information to Müller-Rommel ea. (2008).

- EJPR yearbook (1990–today) — [politicaldatayearbook.com](http://www.politicaldatayearbook.com/)
- European Representative Democracy Data Archive — [erdda.se](http://erdda.se/index.php/projects/erd)
- Müller/Strom (2000) — Western Europe (1945–2000)
- Müller-Rommel ea. (2008) and Conrad/Golder (2010) — Central/Eastern Europe (1990—2009)
- Flora (1983) — inter-war cabinets
- Wikipedia

## Countries

### (\_) Country notes

Summary of main institutional rules and respective changes, data and news sources, references, coding comments, open questions and remaining tasks.

Electoral system information from [CLEA](http://www.electiondataarchive.org/) country descriptions (Appendix I), [ESCE](http://www.electoralsystemchanges.eu/) country summaries, [IPU-PARLINE](http://www.ipu.org/parline-e/parlinesearch.asp) electoral system summary, Mackie and Rose (1991), Rokkan and Meyriat (1969)

Cabinet information in Müller and Strøm (2000) and Bergman ea. (2019), see also [ERDDA.se ](http://www.erdda.se/) data.

Country information about democratisation from Boix ea. (2013).

_Abbreviations_ — proportional representation (PR), single transferable vote (STV)

_Additional sources_ — [V-Dem](https://v-dem.net/) and [PIPE](https://sites.google.com/a/nyu.edu/adam-przeworski/home/data) data – female suffrage (see [IPU](http://www.ipu.org/wmn-e/suffrage.htm))

_Note:_ This is an evolving and incomplete documentation of country specific information.

### Australia

Information

- federal parliamentary constitutional monarchy
- head of state is the monarch of UK
- independence in 1901
- full male suffrage by 1900, female suffrage in 1902
- alternative vote (AV) introduced in 1918

Data sources online

- [party register](http://www.aec.gov.au/Parties_and_Representatives/)
- [official election results](http://results.aec.gov.au/)
- [Parliamentary Handbook of the Commonwealth of Australia](http://www.aph.gov.au/library/handbook/)
- [federal election results 1901–2007](http://www.aph.gov.au/library/pubs/rp/2008-09/09rp17.htm)
- [Australian Government and Politics Database](http://elections.uwa.edu.au)

News in English

- [Radio Australia News](http://www.radioaustralianews.net.au/tags.htm?tag=region:australia)
- [The Australian](http://www.theaustralian.com.au/)
- [The Sydney Morning Herald](http://www.smh.com.au/national)

References

- Colin Hughes, und Bruce Desmond Graham. 1968. A handbook of Australian government and politics, 1890-1964. Canberra: Australian National University Press.
- Hughes, Colin. 1977. A handbook of Australian government and politics, 1965-1974. Canberra: Australian National University Press.
- ———. 1986. A handbook of Australian government and politics, 1975-1984. Sydney, New York: Australian National University Press.
- ———. 2002. A handbook of Australian government and politics, 1985-1999. Annandale N.S.W.: Federation Press.

Coding comments

- Barber (2008) distinguishes the number of eligible voters between 'enrolled' and 'enrolled divisions'. Enrolled figures represent the total number of eligible voters, while enrolled division figures include only eligible voters in contested districts. The distinction applies to elections between 1901 and 1943.

Todo later

- check and revise LDP election results 2010–2019
- coding of the special district Northern territory (see Barber 2008)

### Austria

Information

- federal parliamentary republic

Data sources online

- [Federal Chancellery](https://www.bundeskanzleramt.gv.at/en.html)
- [elections](http://www.bmi.gv.at/412/Nationalratswahlen/)
- [cabinets and ministers](http://www.parlament.gv.at/WWER/BREG/REG/)
- [Meldungen der APA - Austria Presse Agentur aus den Jahren 1955-1985](http://www.historisch.apa.at/cms/apa-historisch/start.html)
- [AEIOU Österreich-Lexikon cabinets](http://austria-forum.org/af/AEIOU/Bundesregierung)

News in English

- [The Local](http://www.thelocal.at/page/view/politics)

Open questions

- number of votes for VGO in 1983 election differ between BMI and statistical yearbook
- date of acceptance for the resignation of Figl III cabinet needed
- formal resignation dates for cabinets after 1996 needed, not covered by Müller/Strom 2000

### Belgium

Information

- federal parliamentary constitutional monarchy
- full male suffrage in 1893 election, female suffrage in 1948
- PR (D’Hondt) in 1900

Data sources online

- [Belgische verkiezingsuitslagen](http://www.ibzdgip.fgov.be) (French/Dutch)

News in English

- [Flandersnews](http://www.deredactie.be/cm/vrtnieuws.english)

Coding comments

- due to plural voting, the number of total votes is higher than the number of electorate in elections from 1904 to 1914
- data in IBZ and Nohlen/Stöver is not consistent

Open questions

- seat distribution of parties in electoral alliances
  - FDF-PPW alliance in 1991 election
  - PRL/FDF alliance in 1995 election
    - seat distribution
    - information about PPW (Pari pour la Wallonie)
  - SPA/Spirit in 2003 election
  - CD&V/N-VA in 2007 election

### Bulgaria

Information

- unitary parliamentary republic

Data sources online

- [official election results](http://www.cik.bg/)

News in English

- [Radio Bulgaria](http://bnr.bg/en/politics/list)
- [Novinite](http://www.novinite.com/articles/category/2/Politics)

Coding comments

- 1990 election is not coded since no official results are available (see Nohlen/Stöver 2010: 367). Consequently, the cabinets of Lukanov and Popov are not coded in ParlGov neither.

Open questions

- coding of BSP coalitions – national and EP
  - seat distribution of Democratic Left (1997) and Coalition for Bulgaria (2001, 2005, 2009), esp. seat share of BSP after 2005 election
  - BSP not running as coalition in 2019 EP election?
- missing cyrillic party names
- "electorate" 2009 EP election

Todo later

- double check Blue Coalition EP Elections 2009

### Canada

Information

- federal parliamentary constitutional monarchy
- head of state is the monarch of UK
- full male suffrage by 1900 and female suffrage in 1918

Data sources online

- [Elections Canada](http://www.elections.ca/res/rep/off/ovr2015app/home.html#1)
- [Canadian Elections Database](http://canadianelectionsdatabase.ca)
- [Prime Minister of Canada](https://pm.gc.ca/)

News in English

- [Radia Canada](http://www.rcinet.ca/english/news/)
  – [CBC](http://www.cbc.ca/)

Coding comments

- the data sources on election results before (and after) 1945 are often inconsistent

### Croatia

Data sources online

- [Croatian State Electoral Commission](https://www.izbori.hr/)

News in English

- [Total Croatia News](http://www.total-croatia-news.com/news/politics)

Coding comments

- official election results are not aggregated at the national level
- voting results for 10 MMC districts recorded
- votes cast on alliance level as votes cast for each alliance member do not add up to total votes cast for an alliance

Open questions

- status and seat strength of parliamentary groups (esp. for electoral alliances)
- seats LIBRA and DC after formation through split (relevant for cabinets)
- 2000 election: 3 no-party seats from ethnic minority district?
- 2007 election: results also recorded for 10 MMC districts only?

Todo later

Data sources are incomplete and inconsistent to meet ParlGov coding rules.

- aggregated number of votes for national, abroad and minority district needed
- information about all parties with more than 1.0% vote share needed
- primary sources about electoral alliances and members needed

### Cyprus

Information

- only _presidential system_ in ParlGov

Data sources online

- [election results](http://results.elections.moi.gov.cy)

News in English

- [Cyprus Mail](http://www.cyprus-mail.com)

Coding comments

- Cyprus has a presidential form of government. Therefore, cabinet start dates may not coincide with election dates. Presidential cabinets are coded according to ParlGov coding rules.

Open questions

- election 2001: official sources needed — votes from Parline do not add up

Todo later

- add primary sources for Wikipedia based coding (national elections: votes for parties with no seats)

### Czech Republic

Information

- Unitary parliamentary republic

Data sources online

- [official election results](http://www.volby.cz/index_en.htm)

News in English

- [Radio.cz](http://www.radio.cz/en/section-archive-calendar/news/) (archive 1998-today)
- [Prague Monitor](http://www.praguemonitor.com/news)
- [Prague Post](http://www.praguepost.com/news)

Open questions

- When crossed members of the rebel faction from ODS to US/DEU? – January 1998
- seat distribution LSU alliance 1992

### Denmark

Information

- unitary parliamentary constitutional monarchy
- full male suffrage in 1849 election, female suffrage in 1915
- plurality SMD in 1894
- cabinet responsibility in 1901
- PR (D’Hondt) in 1918

Data sources online

- [Danmarks Statistiks valghjemmeside](http://www.dst.dk/valg/index.htm) (election results)
- [Statistisk Årbog](http://www.dst.dk/aarbogsarkiv) (Statistical Yearbook)
- [Tal og Fakta](http://www.ft.dk/Dokumenter/Publikationer/Tal%20og%20Fakta.aspx) – Valg og tendenser, Regeringer 1953–2007
- [Den Store Danske Encyklopædi](http://www.denstoredanske.dk/)

News in English

- [The Local DK](http://www.thelocal.dk/page/view/politics)

References

- Elklit, J., 2002. The politics of electoral system development and change: The Danish case. In The evolution of electoral and party systems in the Nordic countries. New York: Agathon Press, pp. 15-66. [evolution electoral system]

Coding comments

- ['Grønland og Færøerne'](https://parlgov.fly.dev/data/parties/dnk/1634/) coded as one party to include results of regional parties from Greenland and Faroer Island
  - we add all parties which won at least one seat in Greenland or Faroer
  - we only code the seats of the affected parties
- coding of election results 1901 and 1903 based on Mackie and Rose (1991) due to missing data in Nohlen and Stöver (2010)

Todo later

- add election results for Greenland and Faroe Islands – currently coded as one party
- add causes of government termination and minority support parties from Damgaard (1994)

### Estonia

Data sources online

- [National Electoral Committee](http://www.vvk.ee/?lang=en)
- [History of Estonian Political Parties](https://www.erakonnad.info/)

News in English

- [Estonian Public Broadcasting](http://news.err.ee/)
- [The Baltic Times](http://www.baltictimes.com/news_estonia/)

Open questions

- seats EKK alliance members 1995
- founding of Parempoolsed in 1992 parliament
  - How many members defected?
  - When did the split happen?

References

- National Electoral Committee. 2016. [Elections in Estonia 1992-2015](https://www.riigikogu.ee/wpcms/wp-content/uploads/2015/02/Elections_in_Estonia_1992_2015.pdf). Tallinn.

Todo later

- coding of alliance members (eg. RKI 1992)

### Finland

Information

- independence in 1917
- universal suffrage in 1906
- PR (D’Hondt) in 1906, 200 seats, single-chamber [no fundamental changes]

Data sources online

- [Elections – Ministry of Justice Finland](https://vaalit.fi/etusivu)
- [official election results](http://tilastokeskus.fi/til/vaa_en.html)
- [cabinets and ministers](http://www.government.fi/tietoa-valtioneuvostosta/hallitukset/en.jsp)
- [registered parties](http://www.vaalit.fi/15485.htm)
- [parliamentary group changes](http://fi.wikipedia.org/wiki/Luettelo_eduskuntaryhm%C3%A4%C3%A4_vaalikauden_aikana_vaihtaneista_kansanedustajista)

News in English

- [YLE](http://www.yle.fi/uutiset/news/)
- [Helsinki Times](http://www.helsinkitimes.fi/finland/finland-news/politics.html)

References

- Sundberg, J., 2002. The electoral system of Finland: old, and working well. In The evolution of electoral and party systems in the Nordic countries. New York: Agathon Press, p. 67–100. [electoral system evolution]
- Törnudd, K., 1968. The electoral system of Finland, London: Evelyn. [electoral system evolution]

Coding comments

- ['Suomen Puolue / Perussuomalaiset'](https://parlgov.fly.dev/data/parties/fin/26/) coded as one parties
  - legally these are two parties – see comment in party observation
- RKP-SFP private government member in 'Sukselainen IV' coded

Open questions

- number of SD-o MPs supporting Sukselainen II cabinet

Todo later

- change "no seats" election result "description" entry into 'English party name (Finnish party name)'
- code registration and dissolution of parties since 1969
- Swedish party names for all parties (if appropriate)

### France

Information

- full male suffrage in 1848 and female suffrage in 1944 (Mackie and Rose 1991, 131-33)
- two round majority-plurality SMD and PR periods
  - 1889 SMD, 1919 mixed member system, 1928 SMD, 1945 PR, 1958 SMD, 1986 PR, 1988 SMD
- parliamentary system in 1870 and president elected by both chambers; semi-presidential system in 1958

Data sources online

- [Elections – Les résultats](http://www.interieur.gouv.fr/sections/a_votre_service/elections/resultats)
- [France Politique](http://www.france-politique.fr)
- Election results and parliament composition [1945-1958](http://www.assemblee-nationale.fr/histoire/leg4rep.asp) and [since 1958](http://www.assemblee-nationale.fr/histoire/leg5rep.asp)
- Cabinets [1945-1958](http://www.assemblee-nationale.fr/histoire/gvt4rep.asp) and [since 1958](http://www.assemblee-nationale.fr/histoire/gvt5rep.asp)

News in English

- [France 24](http://www.france24.com/en/france)
- [RFI](http://www.english.rfi.fr/france)

Coding comments

- "'Comparatively, France has the most poorly documented electoral statistics.' This statement of Daniele Caramani (2000) must be underlined for various reasons. (...)" (Nohlen 2010, 670). Hence, our coding may include inconsistencies and would profit from feedback by country experts.
- Mackie/Rose election data exclude Algeria and the overseas territories and departments
- Paloheimo (1984) cabinet parties that could not be identified: Gauche Democrats, Movement of Democrats, Payson
- seat strength for some cabinet parties before 1945 unknown – eg. [Painleve 1925](https://parlgov.fly.dev/data/cabinets/fra/1925-04-17/)

Open questions

- How many votes won the Southern League in the legislative election 2012?
- for pre 1945 Wikipedia lists several additional cabinets (no PM or party change), more information needed

Todo later

- double check and update cabinet coding with [ERDDA](https://erdda.org) update Müller/Strom (release in 2021)
- code composition of parliamentary groups (see Mackie and Rose 1991, 133)

### Germany

Information

- federal parliamentary republic

Data sources online

- [Bundeswahlleiter](http://www.bundeswahlleiter.de/de/bundestagswahlen/fruehere_bundestagswahlen/)
- [Wahlen in Deutschland](http://wahlen-in-deutschland.de)
- biographical information: [Munzinger-Archiv](https://www.munzinger.de/search/query?query.id=query-00)

News in English

- [Deutsche Welle](https://www.dw.com/en/top-stories/germany/s-1432)

Coding comments

- elections since 1945
  - only PR votes provided (no SMD votes from first tier)
  - before 1990 we don't include the MPs from Berlin (only procedural voting rights)
  - CDU and CSU recorded as alliance with individual results for election data and as [CDU/CSU party group](https://parlgov.fly.dev/data/parties/deu/1727/) for cabinet data
- elections 1919 to 1933
  - some parties won additional seats in a national district (upper tier)
  - upper tier votes are not included
  - see details in [Wahlen in Deutschland](http://www.wahlen-in-deutschland.de/wrtw.htm)
- confidence votes 1919 to 1933 not coded in ParlGov - data recorded in "Formative Stages of German Politics. The Contested Rise of Parliamentary
  Democracy, 1867-1967" by Philip Manow and Valentin Schröder
- successor parties from Weimar Republic (1933) to Federal Republic (1945) mainly based on personal continuity of MPs

References

- Stöss, R., 1986. Parteien-Handbuch: Die Parteien der Bundesrepublik Deutschland, 1945-1980, Sonderausgabe, Opladen: Westdeutsche Verlag. [core reference on post-war German parties]
- Lenski, S.-C., 2011. Parteiengesetz und Recht der Kandidatenaufstellung Handkommentar, Baden-Baden: Nomos-Verl.-Ges. [party law]

### Greece

Data sources online

- [Ministry of Interior - Elections](http://www.ypes.gr/en/Elections/)

News in English

- [Athens News Agency](https://www.amna.gr/en)
- [Kathimerini](http://www.ekathimerini.com)

Open questions

- latin name for Muslim list
- What is an "Alternative Minister"?
- specification of causes for formation and termination of caretaker governments (Grivas, Zolotas I, Zolotas II)

Todo later

- unify transliteration of greek party names
- coding of alliance members for [Coalition of the Radical Left](https://parlgov.fly.dev/data/parties/grc/45/) in election results
- add alliance members for 2004 and 2007 election — latter needs information about seats distribution

### Hungary

Data sources online

- [National Election Office](http://valasztas.hu)

Coding comments

- 'votes' and 'vote_share' coding based on list votes in territorial constituencies

### Iceland

Information

- home rule in 1904; sovereignty in 1918; republic in 1944
- universal suffrage in 1915 election
- presidential election since 1944

Data sources online

- [ Althingi 1963-2007](http://www.statice.is/?PageID=1316&src=/temp_en/Dialog/varval.asp?ma=KOS02121%26ti=Results+of+general+elections+to+the+Althingi+1963-2007++%26path=../Database/kosningar/althurslit/%26lang=1%26units=Number/percent)
- [Governments and ministers](http://www.althingi.is/vefur/ran.html)
- [Tímarit.is](http://timarit.is/) — historical documents (Icelandic)
- [Indridason 2005](http://onlinelibrary.wiley.com/doi/10.1111/j.1475-6765.2005.00234.x/abstract) — _gated_

News in English

- [Morgunbladet ](http://www.mbl.is/mm/frettir/english/)
- [Iceland Review](http://www.icelandreview.com/)

References

- Jónsson, Guðmundur and Magnús S. Magnússon, eds. 1997. Hagskinna: Sögulegar Hagtölur Um Ísland — Icelandic Historical Statistics. First Edition. Reykjavík: Hagstofa Íslands. [election results 1874 to 1991]
- Hardarson, Ólafur Th. 2002. ‘The Icelandic Electoral System 1844-1999’. Pp. 101–66 in The evolution of electoral and party systems in the Nordic countries. New York: Agathon Press. [evolution electoral system]

Coding comments

- transcriptions Icelandic letters into ascii: 'th' for 'þ', 'd' for 'ð', 'ae' for 'æ'

### Ireland

Information

- independence in 1922
- STV-PR in 1922

Data sources online

- [ElectionsIreland.org](http://electionsireland.org)
- [Iris Oifigiúil (Irish State News)](http://www.irisoifigiuil.ie/)
- [Register of Political Parties](http://www.oireachtas.ie/parliament/about/publications/registerofpoliticalparties/)

News in English

- [RTÉ News](http://www.rte.ie/news/)
- [The Irish Times](http://www.irishtimes.com/)

References

- Barberis, Peter. 2005. Encyclopedia of British and Irish Political Organizations: Parties, Groups and Movements of the 20th Century. New York; London: Continuum.
- Gallagher, Michael. 1993. Irish Elections 1922-44: Results and Analysis. Limerick: PSAI Press.
- Gallagher, Michael. 2009. Irish Elections 1948-77: Results and Analysis. Routledge.

Coding comments

- Outgoing chairperson of the lower house is automatically re-elected. Seat is added to the respective party ('data_json' keys: 'seats_uncontested', 'outgoing_chairperson').
- due to the STV-PR it is not possible to specify a certain number of absolute votes per party
- when coding the absolute votes per party we count the number of first preferences, which is common practice

### Israel

Information

- cabinet status of ministers (cf. Kenig 2014, 181)
  - cabinet ministers — are members of cabinet meetings with voting right in the cabinet plenum. This includes _ministers without portfolio_.
  - deputy ministers — _do not_ attend cabinet meetings and _do not_ have voting rights. This applies also in [rare] cases of deputy ministers in a government ministry without a minister "above" them.
  - Source: Ofer Kenig, Ashkelon College; personal communication, 28 March 2020
- direct election of prime minister between 1996 and 2003

Data sources online

- [Knesset election results](http://www.knesset.gov.il/description/eng/eng_mimshal_res.htm)
- [CBS · Elections and Knesset](http://www.cbs.gov.il/reader/?MIval=cw_usr_view_SHTML&ID=445)
- [cabinet ministers](http://www.knesset.gov.il/govt/eng/GovtByNumber_eng.asp) and [cabinet parties](http://www.knesset.gov.il/faction/eng/FactionGovernment_eng.asp) (minister list used for cabinet coding)
- [description events elections and governments](http://www.knesset.gov.il/history/eng/eng_hist_all.htm)
- [parliamentary groups](https://main.knesset.gov.il/EN/mk/apps/faction/faction-lobby)
- [changes in parliament](http://www.knesset.gov.il/faction/eng/FactionHistoryAll_eng.asp)

News in English

- [Times of Israel](https://www.timesofisrael.com/)

Coding comments

- ministers without portfolio coded as cabinet parties and deputy ministers as cabinet support parties (see above and thanks to Or Tuttnauer for support in 2020)
- cabinets continuing in office (no resignation or lost confidence vote) after an early dissolution of parliament are coded as "continuation caretaker cabinet" (e.g. [Netanyahu 2014](https://parlgov.fly.dev/data/cabinets/isr/2014-12-02/))
- cabinet support parties coded for deputy ministers and Arab satellite lists
- all changes in parliament included based on [Knesset information](http://www.knesset.gov.il/faction/eng/FactionHistoryAll_eng.asp)
- seats for alliance members of United Torah Judaism to be included with a 'data_json' key if available
- minor differences in the composition of party lists (esp. electoral alliances)
  - not coded as "party change" for consecutive elections
  - changes of the name and composition are mainly recorded in "description"

### Italy

Data sources online

- [Archivio Storico delle Elezioni](http://elezionistorico.interno.it/) — Ministero dell'Interno
- [Annuario statistico italiano 2002](https://www.istat.it)
- [Composition parliament](http://it.wikipedia.org/wiki/Deputati_della_XV_Legislatura_della_Repubblica_Italiana)
- [dati.camera.it](http://dati.camera.it/it/)

News in English:

- [ANSA](http://www.ansa.it/web/notizie/rubriche/english/english.shtml)
- [Corriere della Sera](http://www.corriere.it/english/)

Coding comments

- Non-partisan prime ministers coded [PC](https://parlgov.fly.dev/data/parties/ita/2001/) to avoid false matches with election results.
- Parliamentary seats for foreign Italians and the seat of Aosta Valley are determined separately. They are added to the "normal" Italian results

Open questions

- coding of The Coalition electoral alliance

### Japan

Data sources online

- [Ministry of Internal Affairs and Communications](http://www.soumu.go.jp/senkyo/senkyo_s/data/index.html)
- [Cabinets since 1996](http://www.kantei.go.jp/foreign/archives_e.html)

News in English:

- [The Japan News](http://www.japantimes.co.jp/),
- [NHK World](http://www3.nhk.or.jp/daily/english/politics.html)

Coding comments

- elections since 1994
  - only PR tier votes provided

Open questions

- largest party that won no seats missing for most elections
- double check of party families by country expert
- change of party affiliations after 1972 election
- alternative source number of votes and valid votes for 1952 election. inconsistency in Mackie/Rose

Todo later

- update seat composition of parliament at formation of cabinets with EJPR data
- description and final coding of cabinet formation and termination 1958 until today
- add 'seats_smd' to 'data_json'

### Latvia

Data sources online

- [Central Election Commission of Latvia](https://www.cvk.lv/en)

News in English:

- [Latvian Public Media](http://www.lsm.lv/en/politics/politics/)

Open questions

- double check coding of electoral alliances, especially whether [Harmony Center](https://parlgov.fly.dev/data/parties/lva/1100/) is a party or an electoral alliance
- seat strength of parties in electoral alliances
- party family for [MPA-LNP](https://parlgov.fly.dev/data/parties/lva/1163/)

Todo later

- add alliance members for EP elections
- double check electorate and and total votes for 'EP 2009 election'

### Lithuania

Information

- PM and cabinet must each pass an investiture vote (article 92 constitution; Matonyte 2019, 309-10).
- Government returns its power after presidential elections (article 92 constitution; Matonyte 2019, 309).

Data sources online

- [The Central Electoral Commission of the Republic of Lithuania](http://www.vrk.lt/en/)

News in English

- [Lithuanian News Agency](https://www.elta.lt/en)
- [Delfi.en](https://en.delfi.lt/)
- [Lithuania Tribune](http://www.lithuaniatribune.com/)
- [Baltic Times](http://www.baltictimes.com)

Coding comments

- cabinet start date coded for PM investiture vote (incomplete, see below)
- new cabinet coded for resignation and investiture after presidential elections
- public election committees (visuomeninis rinkimų komitetas)
  - A legal form to run in an election used since 2015 as an alternative to parties
  - We add a prefix to name ("VRK –"), name short ("K-") and english name ("PEC --") (e.g. [K-AMT](https://parlgov.fly.dev/data/parties/ltu/2760/) 2019)
  - We also add 'data_json' entries '{"party_type": "election_committee", "new_party": false}'

Open questions

- cabinet investiture votes not documented adequately with media reports
- party family (ideological classification) of public election committees
- seats for Lithuanian Liberal Union and The New Union differ between vrk and Wikipedia/Essex
- coding of 1990 elections [96 Sajudis candidates](http://www3.lrs.lt/pls/inter/w5_show?p_r=281&p_d=3248&p_k=2)
- seat strength of _Sajudzio koalicija_ in first four cabinets and status of PM

Todo later

- cabinets
  - complete and harmonise coding all PM and cabinet investiture votes
  - consistent coding of cabinet start dates for investiture vote of PM
  - coding of acting prime ministers (see Conrad/Golder 2010, 142)
- add 'seats_smd' to 'data_json'

### Luxembourg

Information

- full male suffrage in 1893 election, female suffrage in 1918

Data sources online

- [elections.public.lu](http://www.elections.public.lu)
- [governments](http://www.gouvernement.lu/gouvernement/gouvernements-precedents/index.html)

News in English

- [Luxembourg Times](https://luxtimes.lu/luxembourg)

Coding comments

- turnout and electorate (registered votes) numbers not available for 1922-1945 (Nohlen 2010, 1245)
- multiple votes per voter, 'data_json' keys: 'multiple_votes' and 'votes_total'
- party names are coded in Luxembourgish with a few historical exceptions in French
  - French and German party names are coded in 'data_json'

### Malta

Information

- self-government in 1947, UK rule in 1958, independence in 1964
- STV-PR in 1921

Data sources online

- [Electoral Commission Malta](https://electoral.gov.mt/Elections)
- [Elections in Malta](http://maltadata.com)

News in English

- [Times of Malta](http://www.timesofmalta.com/sections/view/local)

Coding comments:

- due to STV-PR it is not possible to specify absolute votes per party
- when coding the absolute votes per party we count the number of first preferences
- see bonus seats in [1987 election](https://parlgov.fly.dev/data/elections/mlt/1987-05-09/)

### Netherlands

Information

- full male suffrage in 1917 and female suffrage in 1919
  - 1970: compulsory voting abolished
- two round majority-plurality SMD in 1896
- PR (Hare) in 1918

Data sources online

- Elections
  - [Databank verkiezingsuitslagen ](http://www.verkiezingsuitslagen.nl)
  - [Dutch election results since 1918](http://www.nlverkiezingen.com/index_en.html)
- Cabinets
  - [Kabinetten per tijdvak](http://www.parlement.com/9353000/1/j9vvhy5i95k8zxl/vhnnmt7jmhzl)
  - [Kabinetten sinds 1945](https://www.rijksoverheid.nl/regering/inhoud/over-de-regering/kabinetten-sinds-1945)
- Parties
  - [Small political parties, 1918–1967](http://www.historici.nl/Onderzoek/Projecten/KPP/Partijen)

News in English

- [DutchNews.nl](http://www.dutchnews.nl/category/politics/)

Open questions

- Drees I — VVD defector party?

### New Zealand

Information

- self-government (dominion) in 1907
- full male suffrage in 1879 and female suffrage in 1893
- plurality SMD in 1853 (majority-plurality SMD in 1908 and 1911)
- mixed member PR in 1994

Data sources online

- [Electoral Commission](http://www.elections.org.nz/events/past-events)
- [Te Ara: The Encyclopedia of New Zealand](http://www.teara.govt.nz)

News in English

- [Radio New Zealand](http://www.radionz.co.nz/news)
- [The New Zealand Herald](http://www.nzherald.co.nz)

Coding comments

- cabinet under same PM after elections starts when the cabinet is sworn in; legally no new cabinet (eg. [Key II](https://parlgov.fly.dev/data/cabinets/nzl/2011-12-14/))
- data sources on election results before 1945 are inconsistent; Vowles provides the most extensive information
- for elections before 1945 electorate shows the number of registered voters in European constituencies; there was no electoral register in the four Maori constituencies

### Norway

Information (Rokkan and Meyriat 1969, 262)

- full male suffrage in 1900 and female suffrage in 1907 (1913)
- indirect elections in 1815
- two round majority-plurality SMD in 1906
- PR (D’Hondt) in 1921

Data sources online

- [Data on the Political System — PolSys](http://www.nsd.uib.no/polsys/en/)
- [Statistical Yearbook of Norway](http://www.ssb.no/english/yearbook/aarbok.html)
- [Stortingsvalget (Storting Elections)](http://www.ssb.no/histstat/publikasjoner/histemne-24.html#P5850_140889)
- [Governments since 1814](https://www.regjeringen.no/en/the-government/previous-governments/governments/id410056/)
- [Archive of Ministers](https://www.nsd.no/polsys/en/)
- [Store norske leksikon](http://www.snl.no/)

News in English

- [Norway News](http://www.norwaynews.com/)
- [News in English](http://www.newsinenglish.no/category/news/)

References

- Svasand, L., 1985. Politiske partier, Oslo: Tiden Norsk Forlag. [parties]
- Nordby, T., 1985. Storting og regjering 1945–1985: Institusjoner, rekruttering, Oslo: Kunnskapsforlaget. [cabinets]
- Aardal, B., 2002. Electoral Systems in Norway. In The evolution of electoral and party systems in the Nordic countries. New York: Agathon Press, pp. 167–224. [evolution electoral system]

Todo later

- code results for joint lists
- update pre-1973 election data with results from official election reports
- code all cabinet appointment and resignation dates from regjeringen.no

Coding comments

- Bokmål used for original names

### Poland

Data sources online

- [PKW](http://www.pkw.gov.pl) — National Electoral Commission

News in English:

- [Polskie Radio (Polish Radio)](http://www.thenews.pl)
- [The Warsaw Voice](http://www.warsawvoice.pl)

References

- Paszkiewicz, K., 2004. Partie i koalicje polityczne III Rzeczypospolitej 3rd ed., Wroclaw: Wydawnictwo Uniwersytetu Wroclawskiego. [party almanac]

Coding comments

- Müller-Rommel ea. (2004) and Conrad/Golder (2010) code the 28/29 April 1993 as the begin of Suchocka II government. However, the Suchocka I government failed a confidence vote on 28 May 1993 and continued as a caretaker cabinet until its resignation on 18 October 1993.
- German Minority Party (MN) support not included in 'cabinet_support' table. Bergman ea. (2019) mention that since 1991 every government has been supported by the MN.

Open questions

- seats of 'Democratic Left Alliance' and 'Labor Union' in parliament after [2001 election]
  - coding of [split alliance](http://en.wikipedia.org/wiki/Democratic_Left_Alliance-Labor_Union)
- SDLP 2005 election — Zieloni and UP on SDLP list or an alliance
- should Pawlak I government be kept? — needs more explicit cabinet definition
- exact date of PPPP split into PPG and MP unknown
- party name change — UW to PD: exact day/month of the change?

Todo later

- double-check and revise party coding (esp. successor/predecessor) with Paszkiewicz (2004)
- re-coding of 1989 election
- coding of SLD alliance members for elections
- coding of changes in composition of parliament as documented in EJPR Political Data Yearbook

### Portugal

Data sources online

- [Portuguese National Election Commission](http://eleicoes.cne.pt)

News in English

- [The Portugal News](http://www.theportugalnews.com/news/news)

Open questions

- Should 1975 assembly election and succeeding cabinets be excluded?
- How long was ID party member of CDU alliance since 1987 election?
- double checking of 1980 election – PSD and PS alliance and district seats
- Who and from which party was the third successful candidate in the CDU alliance in the EP election in 1987?
- Should BE election results be coded as electoral alliance with separate observations for alliance members?

Todo later

- find primary sources for members of electoral alliances (currently Mackie/Rose (1991) and Wikipedia)

### Romania

Information

- district-ordered list system in 2008 and 2012 election
- party-list PR since 2016
  - multi-seat districts (M=7)
  - 5% threshold for parties and 8 to 10% for electoral alliances

Data sources online

- [Biroul Electoral Central](http://www.bec.ro/)

News in English

- [AGERPRES](http://www.agerpres.ro/english/index.php/english.html)
- [ACTMedia](http://www.actmedia.eu/)

Todo later

- [seat distribution](http://www.cdep.ro/pls/parlam/structura.gp?leg=1996&idl=2) in parliament after elections

### Slovakia

Data sources online

- [official election results](https://slovak.statistics.sk/)
- [Statistical Yearbooks of the Slovak Republic](http://portal.statistics.sk/showdoc.do?docid=16037)

News in English

- [The Slovak Spectator](http://spectator.sme.sk) (online archive starting in 1995)
- [Radio Slovakia International](http://en.rsi.rtvs.sk/articles/news)

Open questions

- Party of the Hungarian Coalition (MK)
  - seats distribution and parliamentary party group status in 1990
  - parliamentary party group status in 1990
- exact seat strength of split parties in Moravcik cabinet
- parliamentary status of Simko SDKU splinter group

### Slovenia

Data sources online

- [Election Results](http://volitve.gov.si/en/index.html)
- [Cabinets](http://www.vlada.si/si/o_vladi/prejsnje_vlade/)

News in English

- [Sta](https://english.sta.si/)
- [Slovenia Times](http://www.sloveniatimes.com)
- [Radio Free Europe](http://www.rferl.org) — esp. online archive from 1996 onwards

Todo later

- consistent coding of cabinet start dates for investiture vote of PM or cabinet (see Krašovec/Krpič 2019, 482–83)
- number of votes and total votes for Italian and Hungarian national community seats

### Spain

Data sources online

- [Official Bulletin of the State](https://www.boe.es/)
- [Info Electoral – Ministerio del Interior](http://www.infoelectoral.mir.es/)

News in English

- [El Pais](http://www.elpais.com/english/)

Coding comments

- official results include blank votes into valid votes ('Votos Válidos') – ParlGov 'votes_valid' are based on 'Votos a Candidaturas'
- regional parties which are affiliated with national parties such as the Catalan branch of the [PSOE](https://parlgov.fly.dev/data/parties/esp/902/) are not coded separately as an individual party in elections
- (most) regional parties and green parties in ParlGov not coded as alliance members in EP elections

Open questions

- more detailed information about types of support for minority cabinets
- information about parliamentary boycott of HB (esp. 1989 election and Gonzalez cabinet)

Todo later

- harmonize and define coding electoral alliances

### Sweden

Information

- full male suffrage in 1909 and female suffrage in 1922
- PR (D’Hondt) in 1909, 230 seats
  - 1952: Saint-Laguë; 1969: unicameral, 350 seats, upper tier, 4.0% threshold
- cabinet investiture
  - negative parliamentarism since 1. Jan. 1975
  - no absolute majority against cabinet
  - see [Instrument of Government (1974: 152)](https://www.riksdagen.se/globalassets/07.-dokument--lagar/regeringsformen-eng-2021.pdf) Chapter 12, Art. 3 (page 13)

Data sources online

- Official election results
  - [Valstatistik 1871–1999](http://www.scb.se/Pages/List____292050.aspx)
  - [Valstatistik 2002–](http://www.scb.se/Pages/PublishingCalendarStartPage____259921.aspx?PublishingType=Pub&type=PUB&amne=ME)
- Swedish Election Authority
  - [ election results](http://www.val.se/)
  - [registered parties](http://www.val.se/det_svenska_valsystemet/partier/lista_registrerade_partibeteckningar/index.html)
- [Statistisk årsbok för Sverige](http://www.scb.se/Pages/List____283991.aspx)

News in English

- [Radio Sweden](http://sverigesradio.se/sida/gruppsida.aspx?programid=2054&grupp=3582)
- [Swedish Wire](http://www.swedishwire.com/politics/)
- [The Local](http://www.thelocal.se/news/7/)

References

- Esaiasson, Peter. 1990. Svenska Valkampanjer 1866-1988. Stockholm: Allmänna förlaget.

Open questions

- should the 1970 election be considered an 'early' election?
- parties supporting minority governments and type of support
- party change after elections of 1964 & 1968
  - what was the exact date of change or the date of opening session of the parliamentary term?

### Switzerland

Information

- federal semi-direct democracy under multi-party parliamentary directorial republic
- full male suffrage in 1848 and female suffrage in 1971
- two round majority-plurality SMD in 1900
- PR (Hagenbach-Bischoff) in 1919

Data sources online

- [Statistical Office of Switzerland](https://www.bfs.admin.ch/bfs/de/home.html)
- [The Federal Assembly — The Swiss Parliament](http://www.parlament.ch/e/wahlen-abstimmungen/Pages/default.aspx)
- [Parliamentary Groups](https://www.parlament.ch/en/organe/groups)
- [Referenda](http://www.swissvotes.ch/)
- [Historisches Lexikon der Schweiz](http://www.hls-dhs-dss.ch/index.php) [German]

News in English

- [Swiss Broadcasting Corporation (SBC)](http://www.swissinfo.ch/eng)

Coding comments

- number of votes based on adjusted votes ('fiktive Stimmen') calculated by Statistical Office of Switzerland
- cabinets are coded for each legislative term
  - no prime minister position is attached to a party – one year Bundespräsident is primus inter pares
  - 'starting_date' is the election of the Bundesrat

Open questions

- more information and independent verification about [PSU](https://parlgov.fly.dev/data/parties/che/38/) needed

Todo later

- add French names to all parties
- add largest party no seats for elections before 1967 (source needed)

### Turkey

Information

- presidential system since 2018

Data sources online

- [Supreme Election Council](http://www.ysk.gov.tr/en/past-elections/1852)

News in English

- [Hürriyet](http://www.hurriyetdailynews.com/)

Todo later

- decision about future inclusion after change to a presidential system in 2018

### United Kingdom

Information

- universal suffrage in 1918

Coding comments

- no statistics about number of invalid votes existing until 1964 (see Thrasher/Rallings 2009)

Data sources online

- [Electoral Commission](https://www.electoralcommission.org.uk/our-work/our-research/electoral-data)
- [United Kingdom Election Results](http://www.election.demon.co.uk/)
  - includes a list of [references](http://www.election.demon.co.uk/pollinks.html) on parties, elections and MPs

References

- Barberis, Peter. 2005. Encyclopedia of British and Irish Political Organizations: Parties, Groups and Movements of the 20th Century. New York; London: Continuum.
- Butler, D., 2010. British Political Facts 10th ed., Palgrave Macmillan.
  - core reference on governments, ministers, parties and MPs
- Thrasher, M. & Rallings, C., 2009. British Electoral Facts, Total Politics.
  - an updated version of F.W.S. Craig's classical collection of election results in the UK

Todo later

- 2011 coding – to be checked and updated
- source to validate number of votes cast ('votes_cast') – data until 1959 needed
- 'votes_total' needed for 2015 and some earlier elections

## Contributors

### Project leaders

- Holger Döring 2005–2024
- Philip Manow 2004–2024

### Institutional affiliation

- University of Bremen 2010–2024
- GESIS Leibniz Institute for the Social Sciences 2021–2023
- European University Institute (EUI) 2009–2010
- University of Heidelberg 2009–2010
- University of Konstanz 2007–2009
- Max Planck Institute for the Study of Societies (MPIfG) 2004–2007

### Data editors

- Pawel Szczerbak 2010–2011
- Timm Frerk 2011–2013
- Alina Grünwald 2012–2013
- Volker Lindhauer 2012–2012
- Patrick Statsch 2013
- Julian Limberg 2014–2015
- Lina Schwarz 2014–2017
- Aaron Thatje 2018
- Lukas Warode 2019–2021
- Maike Hesse 2021–2023
- Alexandra Quaas 2021–2023

### Major contributors

- Conor Little (University of Limerick) 2011–2018
- Constantin Huber (University of Bremen) 2021–2023
- Dominic Heinz (MPIfG and University of Bonn) 2006–2007
- Hendrik Zorn (MPIfG) 2004
- Jan Biesenbender (University of Konstanz) 2008–2010
- Jens Hoffmeister (underline webdesign Berlin) 2010
- Jonathan Bright (European University Institute) 2011–2013
- Lukas Warode (University of Bremen) 2021
- Mathias Steudtner (Mittweida) 2007–2008
- Valentin Schröder (University of Bremen) 2010–2019

### Open source software

- Python — programming language
- Django — web application framework
- Bootstrap — front–end framework for web development
- R and RSQLite, SQLite
- Font Awesome

### Contributors

We would like to thank the following people for contributing facts, support, ideas, and encouragement.

- Aaron Thatje (University of Bremen) 2018
- Alexander Trechsel (European University Institute) 2009–2016
- Alexia Katsanidou (GESIS Cologne) 2011
- Aline Grünewald (University of Bremen) 2011
- Andrea Pedrazzani (University of Bologna) 2018
- Armin Schäfer (MPIfG) 2005–2007
- Ben Stanley (University of Social Sciences and Humanities, Warsaw) 2016
- Bjørn Høyland (University of Oslo) 2009
- Christian Breunig (MPIfG and University of Seattle) 2006–2008
- Christina Zuber (University of Konstanz) 2015–2024
- Christine Arnold (University of Maastricht) 2012
- Daniel Bochsler (University of Copenhagen) 2016
- David Willumsen (University of Innsbruck) 2019
- Diego Garzia (University of Siena) 2011
- Dimiter Toshkov (Leiden University) 2019
- Dominik Kunert (University of Konstanz) 2011
- Doru Frantescu (VoteWatch Europe) 2013
- Eva Onnudottir (University of Mannheim) 2014
- Fabio Franchino (University of Milan) 2008–2010
- Florian Beyer (University of Konstanz) 2008–2009
- François Briatte (Catholic University of Lille) 2019
- Frank Henze (Brandenburg Technical University of Cottbus) 2005–2011
- Georg Lutz (University of Lausanne) 2012
- Guinaudeau Isabelle (Sciences Po Bordeaux) 2021
- Guido Tiemann (IHS Vienna) 2006–2011
- Hanna Bäck (University of Mannheim) 2010–2016
- Indridi H. Indridason (UC Riverside) 2017
- Jan Rose (Berlin) 2005–2011
- Jan Schwalbach (University of Bremen) 2015
- Jef Smulders (KU Leuven) 2013–2016
- Johan Hellström (University of Umeå) 2009–2024
- Johannes Freudenreich (University of Potsdam) 2009–2011
- Johannes Kleibl (University of Essex) 2010
- Jonathan Polk (University of Gothenburg) 2014
- José M. Abad (El País) 2017
- Julia Sievers (University of Bremen) 2006–2024
- Julian Limberg (University of Bremen) 2013–2015
- Jürgen Lautwein (MPIfG) 2007
- Kevin Deegan-Krause (Wayne State University) 2014–2019
- Lars Brückner (University of Bremen) 2010
- Lea Kaftan (University of Cologne) 2014
- Lina Schwarz (University of Bremen) 2014–2017
- Luca Verzichelli (University of Siena) 2007–2016
- Lukas Warode (University of Bremen) 2018–2021
- Madeleine Schneider (Swiss Federal Statistical Office) 2012
- Marco Frisone (University of Bologna) 2012
- Marco Giuliani (University of Milano) 2019–2021
- Maria Thürk (University of Bremen) 2013–2015
- Mark Franklin (European University Institute) 2009–2010
- Mattan Sharkansky (University of Rochester) 2015
- Micha Bächle (University of Konstanz) 2009
- Mihail Chiru (Central European University) 2012–2013
- Mikko Mattila (University of Helsinki) 2009
- Monika Mühlböck (IHS Vienna) 2009–2010
- Moritz Muth (University of the Arts Bremen) 2013
- Nina Wiesehomeier (Swansea University) 2008–2024
- Ofer Kenig (The Israel Democracy Institute, Jerusalem) 2014, 2020
- Or Tuttnauer (University of Mannheim) 2019–2020
- Osnat Akirav (Western Galilee College) 2016–2019
- Patrick Dumont (University of Luxembourg) 2010–2012
- Patrick Statsch (University of Bremen) 2013
- Pawel Szczerbak (Heidelberg University) 2010–2011
- Peter Mair (European University Institute) 2009–2010
- Peter Meißner (University of Konstanz) 2015
- Peter Söderlund (Åbo Akademi) 2015
- Philipp Harfst (University of Greifswald) 2007-2013
- Philipp Köker (University College London) 2016
- Phillip Hocks (University of Bremen) 2015
- Phillip Rehm (WZB Berlin Social Science Center and Duke University) 2007
- Pola Lehmann (WZB Berlin Social Science Center) 2014–2019
- Quinton Mayne (Harvard University) 2009–2010, 2018
- Rick Well (Leiden University) 2022
- Ryan Bakker (University of Georgia) 2014
- Sarah Engler (University of Bern) 2015–2017
- Sebastian Eppner (University of Potsdam) 2009–2015
- Sebastian Hübers (MPIfG and University of Tübingen) 2006
- Sebastian Jäckle (University of Freiburg) 2011
- Sigita Trainauskiene (Government Strategic Analysis Center, Vilnius) 2020
- Simon Franzmann (University of Cologne) 2006–2012
- Sinziana Popa (MPIfG and Duke University) 2007
- Steffen Stell (University of Konstanz 2021)
- Steffen Ganghof (MPIfG and University of Potsdam) 2005–2012
- Svanur Kristjansson (University of Iceland) 2014
- Sven Regel (WZB Berlin Social Science Center) 2011–2023
- Thomas Mustillo (Purdue University) 2014–2024
- Timm Frerk (University of Bremen) 2011–2013
- Tom Fleming (University of Oxford) 2016
- Tom Louwerse (Leiden University) 2022
- Volker Lindhauer (University of Bremen) 2011
- Zsófia Papp (HAS Centre for Social Sciences, Budapest) 2014

## Changes

### Version 2024

Stable version on 12 August 2024 with data updated until June 2023

- release manager: Holger Döring
- data update: Alexandra Quaas, Maike Hesse

#### New information

- new elections and cabinets from January 2022 to June 2023

#### Documentation

- added pdf-version codebook (Markdown based)
- added data editors section to credits
- added tables to SQLite database release
  - 'info_data_source_country'
  - 'cabinet_confidence_vote', 'info_page_content' and 'info_variable_json' (experimental version)
- minor codebook revisions

#### Corrections and updates

- added no-seat party: DEU 1919–1933, EST 2009-EP, GBR 1983, ITA 2004-EP, POL 2019, SVN 2019, ROU 1990. SVN 2000, SWE 2018, TUR 2015
- renamed cabinet names into ascii: AUT Dollfuss, FIN Kivimaki, FRA Debre, DEU Mueller, DEU Bruening, NOR Lovland
- corrected English spelling party names: AUT I-Nat, CYP SYM, DNK AE, IRL FG, ISR Noam, LVA LKPP, NZL CP, SVN SOPS
- AUT election: recoded Nat-WA into I-Nat
- BGR cabinet 2017: added none with PM
- BGR party: renamed party short R into V (party id 2640)
- CHE cabinet 1902: removed PM coding
- CHE election 2019: only one no-seat party
- CYP cabinet 1976: recoded none
- FIN election 2015: recoded one-seat into AS
- MLT election 2017: added PD
- NLD cabinet 1946: removed VVD
- ROU election EP 2019: corrected seats PLUS

#### Webpage

- added Markdown version codebook
- prepare archiving of legacy Django implementation
- prepare minimal new Django implementation

### Version 2022

Stable version on 29 April 2022 with data updated until December 2021

- release manager: Holger Döring
- data update: Constantin Huber, Alexandra Quaas, Maike Hesse, Lukas Warode

#### New information

- new elections and cabinets from April 2020 to December 2021
- validated Central- and Eastern European cabinets with Bergman ea. (2019)
- validated West European cabinets with Bergman ea. (2021)
- see also [news](https://parlgov.fly.dev/docs/news/)

#### Corrections and updates

- NLD cabinet 1946: removed VVD (party id 1409)
- AUS party: recoded CN-QLD into C
- CAN election 2019: recoded votes "none"
- CYP cabinet 2018: removed none
- EST cabinet 1995: recoded party composition
- EST election 1995: added parliament changes
- FRA cabinet 1997: added PRS, V, MC
- FRA cabinets 2016: recoded EELV into PE
- FRA party: recoded RCV into PRS
- ISR elections 2015–2020: added AY and DeTo as alliance members of YaToMe
- ITA party: recoded PdL results from CeD into FI-PdL for 2008 national and 2009 EP election
- JPN election 2012: added HRP
- LTU cabinet 2009: corrected cabinet name (Kubilius)
- LVA election 2018: added KP seats
- NLD election 2010: recoded no-seat into one-seat
- NLD election EP 1984: corrected "party_id" results CP and EuGro
- NLD election EP 1989: recoded CP into CD
- NOR election 1918: recoded one-seat into none
- NZL cabinet 2017: recoded Greens to cabinet support instead of cabinet member
- ROU cabinet 2019: removed (three month rule)
- ROU election EP 2019: recoded and linked USR and PLUS to USR-PLUS (electoral alliance)
- ROU party: recoded PLR into PLR|ALDE
- TUR election 2018: recoded SP into Nation Alliance alliance member

#### Webpage

- use static page at parlgov.org
- use Docker to run ParlGov web page locally
- retire public version of legacy Django implementation

### Version 2020

Stable version on 8 December 2020 (Covid-19 delay) with data updated until March 2020

- release manager: Holger Döring
- data update: Lukas Warode

#### New information

- new elections and cabinets from April 2018 to March 2020
- AUS and DEU pre-1945 elections and cabinets added
- added EP elections and EU Commission 2019
- added SQLite database file into ParlGov Dataverse (includes experimental version)
- depreciated Twitter news tracker on 1 June 2020

#### Documentation

- [unified codebook](https://parlgov.fly.dev/docs/codebook/) (coding rules, country notes, changes, credits) for stable versions
- [ParlGov snippets](https://github.com/hdigital/parlgov-snippets) with usage (code) examples
- specified coding rules continuation caretaker cabinet

#### Corrections and updates

- AUT cabinet 2016: corrected party composition
- AUT election EP 1996: corrected date
- BGR party: recoded ONS into DPS
- CHE elections 1975–1983: added V as alliance member of RB
- CYP cabinet 1977: corrected start date and added caretaker status
- CYP cabinet 2018: added Anastasiades IV
- DNK election 2001: added CD and corrected vote share of DF and FrP
- ESP cabinet 1994: added PM to Tarand
- ESP cabinets 2018–2020: removed PSC-PSOE
- ESP election 2011: removed regional party branches and recoded affected election results
- ESP election 2016: added Unidos Podemos to replace Podemos for alliance
- ESP elections 1982, 1996, 2000: added "no-seat" results
- ESP elections EP: clean-up and minor recoding of regional parties alliances
- FRA cabinets: added PM to Chautemps II (1933), Queuille II (1950), Valls II (2014)
- GBR election 1918: removed ColCon, recoded into Con, added Con-18, added parliament change
- GBR election 1945: recoded Nat into others
- GBR election EP 2004: corrected votes cast
- HRV election 2016: SPH alliance seats at members level
- HRV elections 2003–2016: added SDSS 3 seats to ethnic
- HRV party HPS: renamed Croatian People's Party (Hrvatska pucka stranka, ID 2203) into Croatian Popular Party
- HRV party: removed SU, duplicate of HSU
- IRL cabinet 2016, 2017: added IA
- IRL election 1994: added parliament changes
- IRL elections: corrected number of seats and included seat of the chairman
- ISL election 2017: corrected date
- ISL party: recoded OL into Sfvm
- ISR cabinet 2016: removed YH as cabinet support and added it to cabinet
- ISR cabinets 2011 and 2012: removed MHH and corrected appointment dates
- ISR cabinets 2013 and 2014: added YB
- ISR cabinets: added support parties for all cabinets
- ISR election 2013: corrected parliament change (L, YB)
- ISR election 2013: Likud and YB seats for joint parliament group and split
- ISR parties: name short not based on "Ha" and "Le" prefix
- ITA election 2013: added 13 seats others
- ITA elections 2001–2013: recoded election results
- ITA party: recoded BN into PLI
- ITA party: recoded DINI-RI into RI
- ITA party: recoded LA into PRC
- ITA party: recoded PdA into MpA
- ITA party: recoded UDN into PLI
- JPN election 2012: recoded PLF into TPJ
- LTU cabinets: added new cabinet after presidential elections
- LTU election 1996: added vacant seat and parliament change
- LTU election 2000: added LDDP+LSDP merger
- LTU party: recoded KDT into LSDSP
- LTU party: recoded LLiS into LiCS
- LTU party: removed LDDP
- LUX parties: changed party names to Luxembourgish name only (French and German party names are coded as json)
- LUX party: recoded GAP into Greng
- LUX party: recoded GLA into GLEI
- MLT cabinet 1976: renamed to Mouskos
- MLT cabinet 2017: corrected party
- MLT cabinets: corrected index of some cabinet names
- MLT cabinets: removed president Mouskos 1960–1974
- NLD cabinet 2017: corrected PvdA party ID
- NLD cabinet 2018: added Rutte V government
- NLD cabinets 1933, 1935, 1939: replaced LU with LSP
- NLD election 1929: added MPSL
- NLD party PVV: recoded party family
- NZL cabinet 2017: corrected party composition
- PRT election 1980: corrected AD and PS votes
- PRT party: recoded FRS into PS
- ROU cabinet 1990: recoded into Roman II, corrected start date, added Roman I
- SVK cabinet 1919: added SOS, updated source

#### Webpage

- [codebook unified](https://parlgov.fly.dev/docs/codebook/) to aggregate documentation
- [country notes](https://parlgov.fly.dev/docs/codebook/#countries) public

#### Database

- "polarization_vote" and "polarization_seats" in "viewcalc_election_parameter"
- harmonized "short" name to all lowercase and '-' (instead of '\_') in "info_id"

### Version 2018

Stable version 1 May 2018

#### Data

##### New information

- elections and cabinets until March 2018
- pre-1945 elections and cabinets

##### Corrections and updates

- corrected election date: FIN 1979; IRL 1954, 2002; PRT 1979; SWE 1956, 1998
- specified coding rule cabinet members electoral alliance
- removed imputed "eu_anti_pro" party positions for countries not in CHES

- BEL party: recoded PD into CV
- BEL election 1939: corrected results
- BGR election 2013: added KzB alliance members
- CZE election 2010: corrected TOP09 seats
- ESP party: recoded EP into EP-V
- EST party: split EER into EER and EER-91
- FRA election 1928: added RI seats
- FRA election EP 2014: added CSP
- FRA party: recoded MoDem into UDF
- GBR cabinet: added Churchill war ministries
- GBR election 1923: corrected vote share all parties
- GBR party: recoded LD and Alliance into Lib
- GRC cabinet 2012: added PASOK and DIMAR (non-partisan ministers)
- HRV election 2011, 2015: corrected election results on alliance level
- HRV election 2015: corrected election results based on ejpr
- HRV party: deleted HDS and MS
- ITA party: deleted DL
- ITA party: PSUf recoded into PSI
- LTU election 2012: corrected LSDP and TT seats
- LUX election 1925: corrected IL vote share
- LVA election 1995: corrected KDS seats
- NLD party: renamed "ChristianUnion -- Reformed Political Party" into "ChristianUnion"
- NZL election 1931: corrected RP vote share
- POL election 2015: recoded PR into Razem
- PRT election 1975: corrected 'one seat' seats
- SVK cabinet 2006: corrected party composition Dzurinda III
- EU added Gabriel to Juncker (2014)

#### Database

- fixed issue in calculated county-year weights -- "viewcalc_country_year_share"

### Version 2015

Stable version 12 March 2016

#### Data

##### New information

- 2015 elections and cabinets
- [ParlGov Dataverse](https://dataverse.harvard.edu/dataverse/parlgov)
- pre-1945 election results -- _development version_

##### Corrections and updates

- tables (csv and xlsx) in _stable version_ include only information from 1945 to 2015
- database includes also pre-1945 information from _development version_

- AUT party: removed ApE
- BGR election 2013: recoded NDSV into CSD
- BGR party: corrected several short party names
- CHE party: renamed FraP into FGr-ASF
- CYP party: removed A+D+E
- DNK election 2005: corrected seats GrFa
- EST elections 1992 and 1995: removed electoral alliances Left Alternative and Oigus
- FRA election: recoded election dates to last date of election
- HUN election 1994: added KP
- HUN party: recoded CP into KDNP
- ISL election 1987: added FM and Thod
- ISR cabinet 1996: Netanyahu I split into three cabinets
- ISR election 1996: separate seats for Likud-Gesher-Tzomet alliance
- ISR election 2006: added HY
- ISR party: recoded Gahal into Likud
- ITA party: recoded SI and PSI-07 into P|SDI
- JPN party: recoded PLP into PLFP
- LTU election 1992: added electoral alliance For a United Lithuania
- LVA election 1995, 1998: added electoral alliance KDT/LSDA
- LVA election 1995: added new party LZ, added electoral alliance LSP+L
- LVA election 1998: removed LZS+KDS, alliance of LZP, KDS and Labor Party added
- LVA election 2006: recoded Motherland into SDLP
- LVA president 2007: added Valdis Zatlers
- NLD cabinet 1977: recoded KVP and ARP into CDA
- NOR election 2009: corrected date
- POL election 1991, 1993: recoded WAK and O into ZChN, removed WAK and O
- POL election 1997: UPRz recoded into UPR, removed UPRz, added PC, PCD, PL to AWS
- POL party: recoded PJKM into UPR|KNP
- ROU election 1990: removed electoral alliance AUL
- SVK party: removed SD
- SVN election 1990: SOPS added
- SVN party: DZL and ZEO added

#### Webpage

- relaunch with new [Bootstrap 3](http://getbootstrap.com/) based layout (Dec 2014)

#### Database

- fixed issue in data dump -- 2014 stable version excluded ISR and TUR election and cabinet data
- Excel spreadsheet export of main tables

### Version 14/12

Stable version 29 December 2014

#### Data

##### New information

- country added: TUR, ISR
- added presidents
- updated from seats to votes level data: HUN, CHE, EST (completing votes level for all countries)

- elections added: EP elections 2014, HUN 2014, BEL 2014, SVN 2014, SWE 2014, NZL 2014, LVA 2014, BGR 2014, JPN 2014
- cabinets added: LVA Straujuma I, CZE Sobotka, DNK Thorning-Schmidt II, ITA Renzi, ROU Ponta III, CYP Anastasiades II, EST Roivas, FIN Katainen II, FRA Valls, HUN Orban III, FIN Stubb, FRA Valls II, BGR Bliznashki, BEL Di Rupo II, SVN Cerar, FIN Stubb II, POL Kopacz, BEL Michel, SWE Loefven, NZL Key III, LVA Straujuma II, BGR Borisov II, ROU Ponta IV, ISR Netanyahu VI, JPN Abe IV
- added EU Commission 2014

##### Corrections and updates

- removed countries not fully covered: ALB, GDR, LIE, NIR, SCO, WAL; CHL, KOR, MEX, USA, EU
- PRT vote shares updated to calculated values (CNE source reports share based on total votes)
- FRA EP elections 1979 to 2009 revised and updated
- EST electoral alliances revised

- AUS election 1945: recoded election date
- AUS party: recoded VdU into FPO
- AUT party: recoded ALP (1910-14) into CLP
- AUT party: recoded ALP (1922) into LP
- AUT party: recoded NCL-NSW into LLP
- BEL party: recoded FDF+RW into FDF
- BEL party: recoded PRL/FDF into PRL
- BGR party: recoded NAPRED into ZNS
- BGR party: recoded PDS into PBSD
- CHE party: recoded FDP into FDP-PRD
- CYP cabinet: Clerides III, IV recoded etc into LP
- CZE party: recoded LEV21 into CSS
- CZE party: recoded SNK into SNK-ED
- CZE party: recoded ULD into US
- DEU election: added largest party no seat (first loser) with less than 1.0% vote share
- DEU party: recoded Gruene into B90/Gru
- DEU party: recoded Linke into Li/PDS
- ESP party: added CV with election results and alliance membership
- EST party: recoded EDP into ESE
- EST party: recoded EME into ERa
- EST party: removed ESDTP, RKI+SP
- FIN election 1927 to 1939: added 'no seat' party results
- FIN election 1927-1936: added 'electorate', 'total_votes', 'valid_votes'
- FIN party: added PMP and updated election results
- FIN party: recoded SKP and VAS into DL/VAS
- GRC party: unified 'party_name_short' to Greek party names
- HUN election EP 2009: recoded seats Fidesz and KDNP
- HUN party: recoded MSZMP into MMP
- IRL election EP: recoded 'none' into MEPs winning seats twice
- ISL election 1963: corrected 'electorate' and 'votes_total' (swapped)
- ISL party: Ab - updated information about alliance members and seats distribution
- ITA cabinet 1970: split PSU into PRI and PSU
- ITA party: recoded FDP into PCI
- ITA party: recoded FSN into PD
- ITA party: recoded Lib/Rep into PRI
- ITA party: recoded PSI/AD into PSI
- JPN party: recoded RP into DP
- JPN party: recoded TPJ into PLF/TPJ
- JPN party: removed SPJ, PLP
- LTU election 1992: corrected election date
- LTU party: recoded L+L+L into LKDP
- LTU party: recoded SK into TS-LK
- LTU party: recoded TS-LKD into TS-LK
- NLD cabinet: recoded Balkenende I-VI (split Balkenende I)
- NLD party: recoded DMP into NMP
- NZL cabinet: recoded start date Key II
- POL party: recoded PPPP into PPG and removed MP
- POL party: recoded RuPa into ROP
- POL party: recoded UD into UW-PD
- ROU party: recoded ARD into PL-D
- ROU party: recoded FDSN into PSD
- ROU party: removed ADA, PSD/PC, USL
- SVK election EP 2009: corrected 'electorate'
- SVK party: split SDL into SDL and SDL-05
- SVN election 2000: corrected 'electorate'
- SVN party: recoded NDS into SDZ
- SVN party: recoded SKD into NSI

#### Webpage

- _maintenance_ dev.parlgov.org

#### Database

- added table 'politician_president'
- added view 'view_variable' for documentation of main tables
- table 'viewcalc_election_parameter' -- added variable 'turnout'
- removed table 'election_ep'

### Version 13/12

#### Data

##### New information

- country added: HRV (since 2000)
- elections added: NLD 2012, LTU 2012, ROU 2012, JPN 2012, ITA 2013, MLT 2013, NOR 2013, DEU 2013, AUT 2013, AUS 2013, LUX 2013,
  CZE 2013
- cabinets added: NLD Rutte III, ROU Ponta II, JPN Abe III, MLT Muscat, ITA Letta I/II, GRC Samaras II, CZE Rusnok, CYP Anastasiades, NOR Solberg, AUS Abbott, LUX Bettel, AUT Faymann II, DEU Merkel III

- updated from seats to votes level data: ISL, MLT, LUX, BGR, CAN, ROU, IRL, CZE, ESP, GRC, LTU, SVN, SVK, FRA, NLD and all EP elections

##### Corrections and updates

- compact version of stable release only
- recoding party families
  - all parties are classified into main categories first
  - additional party families in table 'party_family' only
  - imputation of missing party positions by party family
- Chapel Hill Expert Survey (CHES) party ids updated for 2010 survey
- Commissioners: updated variable 'elected'
- fixed issue in calculation of 'viewcalc_parliament_composition'
- Changed all party names to include only ascii characters for respective variables
- BGR cabinet: updated all cabinet sources and descriptions
- DEU: added CDU/CSU party group to parliament changes and cabinets
- ITA elections 1994 to 2008:
  - recoded major alliances into Centre Left and Centre Right
  - recoded smaller parties (alliances) only recorded as alliances
  - removed parties only recorded as alliance members (no seats, no votes)
  - no nesting of alliances in alliances for election results (data_json entry now)

- AUT election: fixed typos in several election descriptions
- AUT party: recoded K/L into KPO
- AUT party: recoded WdU into VdU
- BEL party: recoded CD&V into CVP
- BGR cabinet 1995: Videnov recoded BSP, BZNS, PKE into SDS
- BGR election 2009: updated source
- CAN party: recoded RPC into CA
- CZE cabinet 1993: Klaus II added KDS
- CZE cabinet 1998: Tosovsky recoded ODS into US and PM party into 'none'
- EST party: recoded MKE into K-EUR
- FRA cabinet 1988: Rocard I+II added MRG
- FRA cabinet 2012: recoded V into PRG
- FRA election EP 2009: updated turnout data
- GBR election EP 1979 to 2004: updated turnout data
- GBR election EP 1999: added turnout data and SF
- GRC election EP 1981: updated results
- ISL election 1942, 1959 and 1979: recoded date of election to last election date
- ISL election 1943 to 1963: added votes
- ISL election 1943 to 1991: updated source
- ITA cabinet 1994: Berlusconi I added UdCe
- ITA party: recoded CI into PdCI
- ITA party: recoded LAD into R
- JPN party: removed 'votes' and 'vote_share' for 'others'
- LTU cabinet 2006: Kirkilas recoded 'start_date'
- LTU party: recoded VP/NDP into LVLS
- LVA party: recoded DT and LSA into LSDSP
- MLT party: recoded DA into AD
- NLD party: recoded RKSP into RKP
- NOR party: recoded R into RV
- NZL election 1978: updated 'electorate'
- POL election 1993: recoded S into SRP
- PRT cabinet 1975: added Pinheiro de Azevedo cabinet
- SVK party: recoded ESWS into SMK-MKP
- SVK party: recoded SDKU into SDKU-DS

#### Webpage

- _maintenance and polishing_ dev.parlgov.org
- added favicons

#### Database

- _none_

### Version 12/10

Stable version 15 October 2012

#### Data

##### New information

- elections added: DNK 2011, LVA 2011, POL 2011, ESP 2011, NZL 2011, CHE 2011, SVN 2011, SVK 2012, FRA 2012
- cabinets added: CYP Christofias IV, JPN Noda, DNK Thorning-Schmidt, LVA Dombrovskis IV, SVK Radicova II, ITA Monti, GRC Papademos, POL Tusk II, NZL Key II, ESP Rajoy, CHE Bundesrat 2011, BEL Di Rupo, SVN Jansa II, ROU Ungureanu, SVK Fico II, NLD Rutte II, CZE Necas II, ROU Ponta, SVK Pahor, FRA Ayrault I+II

- updated from seats to votes level data: AUT, NZL
- AUS: elections and cabinets 1901 to 1945
- CHE: elections and cabinets 1919 to 1943

- seats data in 'view_cabinet' take into account changes in parliament composition (if data available)
- added application to calculate political composition of the European Union

##### Corrections and updates

- party clean up: removed minor parties without election results or two external data points
- party positions: fixed error in calculating party positions based on Benoit/Laver (2006)
- threshold including election results: removed election results for parties with less than 1.0% vote share (no seats)
- CHE election 1947 to 2007: updated source

- AUS election 2010: added results CLP
- AUT cabinet 1964 and 1997: Klaus I and Klima cabinet split into two cabinets -- three month constrain
- AUT cabinet 2011: Schuessel IV updated 'parliament_change' to include BZÖ seats
- AUT election 1953: coded VdU and ApE as alliance members of WdU
- AUT party: split VdU/FPO into VdU and FPO
- BEL cabinet 2008 to 2001: recoded CD&V/N-VA into CD&V for Rompuy, Leterme II, Leterme II
- BEL cabinet: added Van and Vanden to names of respective PMs
- BEL cabinet: removed roman number from cabinet names for PMs with single term
- BEL cabinet: renamed Eyskens into Eyskens G
- BGR cabinet 1995: Videnov added coalition partners BZNS and PKE
- CAN election 1979: added SCP and corrected seats NDP
- CAN election 2008 and 2011: added official election results
- CAN election: updated source
- CHE cabinet 2008: added BDP
- CHE party: merged PSU into PSA
- CYP cabinet 2008: Christofias I split into two cabinets due to EDEK withdrawal
- DEU cabinet: 'description' added results confidence votes
- DEU party: added 'uh' to cover changes in parliament composition due to resignation of MPs and surplus seats
- DNK election 1953: April -- corrected G/F seats
- DNK election 2001: recoded Mp into FrP
- DNK election EP 1979: corrected seats KF and seats_total
- DNK election EP 1984: corrected seats Sf and seats_total
- DNK election EP 1979 to 1989: updated source added parties with more than 1.0% vote share
- ESP election EP 1987: updated results
- FIN cabinet 1962: Karjalainen I added SK
- FIN cabinet 1971: one PM party in Karjalainen III only
- FIN election 1962: corrected vote share VI
- FRA election 2002: recoded ER/PRG into Droite and GE into V, added FN
- FRA election EP 1997: recoded ER/PRG into PRG
- GBR cabinet: updated source
- GBR election 2010: added Alliance (1 seat)
- GBR election EP 2009: removed UCU-NF (party_id 1243) and coded alliance with Uup
- GBR election EP 2009: UCU-NF added UUP and CNI alliance members
- GRC election 2007 and 2009: updated source
- ISL cabinet 1942: added Thordarson
- ISL election 1942: added results
- ITA cabinet 1996: split Dini into Dini I and Dini II -- three month constrain
- ITA cabinet 1999 and 2000: D'Alema I and Amato II split DINI into RI and SDI
- ITA cabinet: recoded non-partisan PMs from 'none' into 'PC'
- ITA election: corrected and updated some results
- JPN cabinet 1947: added NCoP
- JPN cabinet 1993: added DRP
- JPN cabinet 2003: removed NCP
- LTU cabinet 2010: split Kubilius II into Kubilius II and Kubilius III -- party change
- LTU election 1996: corrected and updated results
- LUX election 1948 and 1951: updated partial election results
- LUX election EP 1979 to 2004: updated results
- LVA election 2010: corrected vote share
- NLD election EP 1994: corrected GroenLinks vote share
- NLD election EP 1994: recoded SGP into SGP/GPV/RP, corrected seats added alliance members
- NLD election EP 1999: SGP/GPV/RP added alliance members
- NLD election EP 2009: corrected GroenLinks and ChristenUnie-SGP votes
- NOR election 1973 to 2009: extended to 1.0% coding threshold
- NOR election 1973: minor corrections of vote share and updating data source
- NOR election 1977: minor corrections and additions
- POL election 1991: removed PPG and MP and added seats to PPPP
- ROU cabinet: removed Dejeu 1998, Athanasiu 1999, Bejinariu 2004 -- three month constrain
- ROU cabinet 1996 to 1999: Ciorbea, Vasile, Isarescu cabinet parties recoded USD into PD and PSDR, CDR into PNT-CD and PNL
- ROU cabinet 2000: split Nastase into Nastase I and Nastase II -- party change
- ROU cabinet 2009: split Boc II into Boc II and Boc III -- party change
- ROU election 1992: split CDR seats into alliance members
- ROU election 2008: corrected ADA alliance members; corrected etnice; updated source
- SVK election EP 2009: corrected SDKU-DS vote share
- SVN cabinet 1993: Drnovsek II recoded DS into SDS
- SVN election 2008: updated source, added votes, turnout data and LIPA, LPR, LZCPV and KDS.
- SWE election 1998 and 2002: updated source
- SWE election EP 1995: updated source, corrected 'electorate'
- SWE election EP 2004: updated source

#### Webpage

- party -- added information about the calculation of party positions
- party -- put information about parties (and their names) in external data sets to bottom of page
- party -- removed information about party seats from index page of all parties per country
- election, election index -- using new names for effective number of parties
- election, election index -- disproportionality and advantage ratio with two digits
- election index -- party with absolute majority of seats underlined
- cabinet index -- show only one election date
- home section -- show 'Quick links' first and add 'Data section' with examples
- documentation -- removed key list from list of data sources (kept in experimental version)
- download section -- added direct links to csv files of party, election and cabinet table

#### Database

- new table -- 'parliament_composition', 'viewcalc_parliament_composition', , 'viewcalc_country_year_share'
- table 'cabinet' and 'election' -- fixed bug in determining non-existent previous ids
- table 'cabinet' -- added columns 'appointment_date', 'resignation_date' (experimental version)
- table 'cabinet_party' -- added column 'description' and moved (most) 'comment' entries into it
- table 'election' -- added columns 'dissolution_date', 'wikipedia' (experimental version)
- table 'election_result' -- added column 'description' and moved (most) 'comment' entries into it
- table 'party' -- added column 'dissolution_date' (experimental version)
- table 'viewcalc_election_parameter' -- renamed 'enep' into 'enp_votes' and 'enlp' into 'enp_seats'
- table 'viewcalc_election_parameter' -- removed results for party family 'none' from calculation
- table 'viewcalc_party_position' -- renamed 'eu_pro_contra' into 'eu_anti_pro'
- table 'viewcalc_party_position' -- don't overwrite missing 'left_right' with 'state_market'
- table 'view_party' -- renamed 'eu_pro_contra' into 'eu_anti_pro'
- table 'view_cabinet', 'view_election', 'view_party' -- added 'country_name'
- table 'view_cabinet' -- 'seats' now based on 'viewcalc_parliament_composition' instead of 'election_result'

### Version 11/07

Stable version 26 July 2011

#### Data

##### New information

- elections 2011 added: CAN, CYP, EST, FIN, IRL, PRT
- cabinets added: CAN Harper III, CYP Christofias II, EST Ansip IV, FIN Katainen, FRA Fillon III, IRL Kenny, PRT Coelho, SVN Pahor II
- added NIR -- parties only

- updated from seats to votes level data: AUT, CYP, POL
- JPN: added elections and cabinets from 1945 to 1958

##### Corrections and updates

- recoded nationalist, fascist and right-wing populist party families into 'right wing' and added former classifications as additional party families to table 'party family'
- removed some entries used to define full party names from table party_change and added the information to json field in party table (eg. DEU: CDU, CSU; SWE: SAP)
- replaced missing 'left_right' party positions with 'state_market' values if available (esp. relevant for Benoit/Laver 2006 data)
- corrected documentation of variable 'date' in 'election' table
- CYP: removed elections and cabinets prior to 1976 (Polity IV score)
  - added Kyprianou III, Kyprianou V, Vassiliou II, Klerides II, Klerides IV, Papadopoulos II

- AUT cabinet 1945: Figl I split into two cabinets
- AUT cabinet 2002: Schuessel I split into two cabinets -- three month constrain
- AUT cabinet 2003: Schuessel II split into two cabinets taking into account FPÖ split (FPÖ, BZÖ)
- AUT election 1949 to 1962: coded KPO as Communist alliance
- AUT election 1999 and 2002: corrected seats total
- AUT election 1995: added turnout data, votes and Nein party, changed vote share
- AUT election 2008: corrected vote share
- AUT election EP 1996: corrected vote share
- AUT election EP 1999: corrected valid votes
- BEL cabinet 1991: recoded Martens IX starting date -- three month constrain
- BEL cabinet 2007: Verhofstadt II split into two cabinets -- three month constrain
- BEL cabinet 2010: Leterme III set start of cabinet to date of election (2010-06-13) -- three month constrain
- BEL party: KPB-PCB split in 1989 coded (KP and PC); reassigned Ray party expert identifier to PC
- BGR election 1991: added parties
- BIH party: EU Profiler removed all links to Croatian parties -- ticket:72
- BIH party: Benoit/Laver removed Croatian HDZ link
- CHE cabinet 2008: added Bundesrat 2008 -- ticket:60
- CHE election 1983: added 'others' to election, updated seat composition
- CHE party: recoded LdU-AdI (party_id 1646) into LdU-ADI (party_id 1264)
- CYP cabinet 2008: recoded ADK into EDEK
- CYP election 2006: corrected KISOS and updated (votes) results
- CYP election EP 2004: added votes and EDEK result
- CYP party: added 'EDEK' to party name of Movement for Social Democracy and updated short party name
- CZE cabinet 2006: recoded start date of Topolanek I
- CZE cabinet 2009: updated start date of Fisher cabinet to PM appointment
- CZE election 2002: recoded date of election to last election date
- DEU cabinet 1960: Adenauer V split into two cabinets taking into account DP split
- DEU election 1949: added SSW
- DEU election 1953 to 2005: corrected valid votes -- ticket:67
- DEU election 1961: recoded GB/BHE into an electoral alliance (GDP) between GB/BHE and DP
- DEU election 2009: corrected electorate, total votes, valid votes
- DEU election EP 1979 to 2004: updated from seats to votes level data
- DEU election: electoral alliance added for CDU/CSU -- election results still coded at the the CDU and CSU level
- DEU party: updated predecessor/successor entries Linke and added 2005 electoral alliance
- DNK election 1945 to 1950: updated sources
- DNK election 1945 to 1994: corrected number of seats
- DNK election 1947: added HV
- DNK election 1957: corrected total seats
- DNK election 1973 to 1977: added SV as alliance member
- DNK election 1973: added DU as alliance member
- DNK party: recoded party family Dansk Folkeparti
- ESP cabinet 1977 and 1979: Gonzalez renamed into Suarez
- ESP election 1977: corrected and updated results
- ESP party: recoded CHA (party_id 1675) into CA (party_id 1367)
- EST cabinet 2009: Ansip II split into two cabinets
- EST election 1992 and 1995: updated source, added turnout data, corrected and updated results
- EST party: added V, EPL, Metsa, ERKL, KunRoh, ETRE, OIG, TEE
- FIN election 1948 to 1983: updated data sources for RKP-SFP and AS
- FIN election 1958 and 1962: removed SKL
- FIN election 1966: added SKDL/TPSL alliance
- FIN election 1987: corrected SKDL vote share
- FIN election 1991 and 1995: recoded SKYP results into SEP
- FIN election 1995: added VSL
- FIN election 2003: corrected election date
- FIN election EP 1999: corrected number of seats
- FIN party: minor updates on party names and predecessor/successor parties
- FIN party: SKP-97 party names changed into SKP-Y
- FRA election 2007: corrected vote share and seats, added votes
- FRA election EP 2009: corrected number of seats Gauche
- FRA party: added UEM
- FRA party: recoded UMP Benoit/Laver ID
- FRA party: removed The Right (party_id 157) duplicate of Other Right (party_id 285)
- GBR election 1974 to 1987: calculated 'vote_share' for some parties from Northern Ireland -- ticket:66
- GBR election 1983 and 1987: recoded LD as Alliance
- GBR election EP: added notes about vote share in regions
- GBR election EP 1999: corrected vote share and number of valid votes
- GBR party: updated EES IDs for SNP, Plaid, UKIP, PWCL
- GDR cabinet 1990: Maizere coded changes in party composition and defectors
- GDR election 1990: coded electoral alliances and its members, corrected number of votes
- GDR party: updated all entries; coded party changes (including DEU parties)
- GRC party: added names for KODISO
- GRC party: recoded and merged EK into EDIK
- ISL cabinet 1944 and 1946: Thors II, Thors III recoded Ab into So
- ISL cabinet 1979: Groendal changed into caretaker cabinet
- ISL election 1946 to 1953: replaced Ab by So
- ISL election 1967: added OS and updated source
- ISL party: corrected 'þ' transcription into 'th' and removed remaining capitalisation of party names
- ISL party: recoded Thjo (party_id 1637) into Pjo (party_id 205)
- ITA election 1946 and 1948: recoded PLI results into UDN and BN (alliances), added alliance members
- ITA election 1963 and 1968: recoded PNM results into PDIUM (new party)
- ITA party: updated party names and predecessor/successor entries for Socialist parties (PSI, PSDI, PSU)
- JPN cabinet 1980: Ito removed -- three month constrain
- JPN cabinet 1993: added NP
- JPN cabinet 1994: removed LP
- JPN cabinet 1998: split Obuchi into three cabinets
- JPN cabinet 2009: renamed Hatoyama into Hatoyama Y
- JPN election 1958: added votes
- JPN election 1960 to 1967: added number of votes
- JPN election 1969 and 1979: corrected number of votes
- JPN election 2005: corrected number of seats (all parties except LDP and DPJ)
- JPN election 2009: updated source and added NPD
- JPN party, election, cabinet: recoded DSP (party_id 1053) into SDP (party_id 940) for elections and cabinets after 1994
- JPN party: recoded NK into K(CGP)
- JPN party: unified short names to english version -- ticket:63
- LTU cabinet 2008: Kubilius II added TPP
- LTU election 1992: added votes and parties
- LTU party: added VPJST and LLL
- LVA election 2010: added seats total
- NLD cabinet 1977: Den Uyl II; set start of cabinet to date of election (1977-05-25) -- three month constrain
- NLD election 1977: CDA as electoral alliance (ARP, CHU, KVP)
- NLD election EP 1999: added electoral alliance SGP/GPV/RPF
- NOR cabinet 1940: removed Nygaardsvold II
- NOR cabinet 1945: Gerhardsen I coded as caretaker and parties added
- NOR election 1961 to 1969: recoded SV into SF
- NOR election 1973: added SV alliance members
- NOR party: updated RV names
- NZL election 1999: changed number of seats NZFP
- POL cabinet 1991: Olszewski recoded WAK into ZChN (alliance member) and removed PCD
- POL cabinet 1992 and 1993: Suchocka I and II added PSL, PCD and recoded WAK into ZChN (alliance member)
- POL party: removed L; recoded PD into UW-PD
- PRT election 1979: corrected seats of AD alliance members, added Ref and updated source
- PRT election EP 1994: corrected vote share
- PRT party: added PAN; recoded party family PSD; removed Benoit/Laver ID from PDC
- SVN party: removed SA and LU
- SWE election 1985: updated source, corrected turnout data, coded alliance member

#### Webpage

- party -- show information about electoral alliances and alliance members in election results (superscript symbol)
- party -- show party foundation date
- party -- show only year of party change if date is coded as 1 July (default for unknown day/month)
- election, cabinet -- show name of party for elections and cabinets based on information in table 'party_name_change' (if available)
- election -- moved information about 'Changes of party composition in parliament' into experimental version
- election -- show only results for more than 0.5% vote share
- cabinet -- don't show termination date (experimental version observation only)
- external -- corrected publication year references for Castles/Mair, Ray and EU Profiler
- data sources -- cleaned up names of some of the entries

#### Database

- new table -- 'cabinet_support' to include parties that support (minority) cabinets (experimental version)
- new table -- 'party_family' to include additional party families for a party
- tables 'party', 'party_change', 'party_name_change' -- added column 'data_source'
- table 'party' -- added column 'description'
- table 'party' -- added column 'foundation_date' (experimental version)
- table 'party_change' -- added variable 'type_id' (experimental version)
- 'view_cabinet' -- fixed issue in view definition to include all cabinets -- ticket:65
- 'view_election' -- added variable 'previous_cabinet_id'

### Version 10/11

Stable version 16 November 2010

#### Summary

- complete database refactoring -- recoding of table/variable names and all id variables -- see below
- new web design -- Jens Hoffmeister (underline webdesign Berlin) 2010
- new data: European Election Study (2009) party ids added; Belgium, United Kingdom, Portugal, Latvia updated from seats to votes level data; Swiss cabinets since 1945 added
- recent elections and cabinets until October 2010 and data corrections -- see below

#### Data

##### New information

- elections 2010 added: HUN, GBR, CZE, NLD, SVK, BEL, SWE, AUS, LVA
- cabinets 2010 added: NLD Balkenende V, ROU Bejinariu, HUN Orban II, GBR Cameron, JPN Kan, FIN Kiviniemi, AUS Gillard, SVK Radicova, CZE Necas, SWE Reinfeldt, AUS Gillard II, LVA Dombrovskis III,

- updated from seats to votes level data: BEL, GBR, PRT, LVA

- European Election Study (2009) party ids added
- CHE all cabinets since 1945 added
- POL parliament_change -- specification of party composition changes in 2007 parliament

##### Corrections

- BEL cabinet -- recoded party ids for CVP and SP to CD&V/N-VA and SPA/Spirit for all cabinets after 2003 election
- BEL cabinet -- removed orphaned observations from 'cab_party' (old_cabID 19600, 19731, 19732, 19760)
- BEL cabinet -- renamed Eyskens 1981 into 'Eyskens M'
- BGR cabinet -- Stanishev cabinet coding of BSP as KzB
- BIH party -- added parties (old_partyID: 11, 15, 21, 22, 26, 30) to match all CMP parties
- CAN cabinet -- Diefenbaker II and III added
- CAN cabinet -- St-Laurent split into I, II, II
- CAN cabinet -- King III dates corrected
- CZE cabinet -- Tosovsky coded as 'caretaker'
- CZE election -- recoding 'election_date' to last date of election and adding 'opening_date' to 'datajson'
- CZE party -- recoded and removed HSD/SMS duplicate ('old_partyID' 52)
- ESP election ep -- 2004 and 2009 EP election results updated with official sources
- ESP party -- recoded I ('old_partyID' 71) into IU/PCE ('old_partyID' 57)
- EST parties -- RKI (1992); RKI/ERSPI, ERSP, I (1995) and affected elections/cabinets -- revising
- FIN cabinet -- Aura II corrected 'start_date' and 'end_date'
- FIN cabinet -- Barre I, Barre II added observations for non-partisan prime ministers ('pm') to 'cabinet_party'
- FIN cabinet -- Fagerholm II, added L (Liberals)
- FIN cabinet -- Fagerholm III and Virolainen added Liberals
- FIN cabinet -- Kekkonen II, added RKP
- FIN cabinet -- Lipponen I, added VAS
- FIN cabinet -- Lipponen II, split into II and III following resignation of VIHR
- FIN cabinet -- Paasikivi, Fieandt, Kuuskoski, Lehto, Aura I, Aura II, Liinamaa added observations for non-partisan prime ministers ('pm') to 'cabinet_party'
- FIN cabinet -- Sukselainen, Karjalainen, Sorsa II, Sorsa III, Holkeri, Aho recoded as several cabinets due to change in party composition
- FRA cabinet -- Fillon I,II corrected cabinet name
- FRA cabinet -- Barre II 'starting_date' recoded
- GBR cabinet -- Eden government split into Eden I and Eden II
- GBR election -- 1945 corrections
- GER cabinet -- Adenauer II split into several cabinets and coding of party changes
- GRC cabinet -- renamed Karamanlis cabinets to avoid duplicated cabinet names
- HUN cabinet -- Bajnai corrected cabinet name
- HUN cabinet -- Gyurcsan III removed SzDSz
- ITA cabinet -- Prodi I and Amato II added observations for non-partisan prime ministers ('pm') to 'cabinet_party'
- ITA cabinet -- Moro I government split into I, II, III and recoded later Moro governments into IV and V
- ITA cabinet -- Spadolini and Craxi government split into I and II
- ITA party -- PdL duplicate recoded and removed ('old_partyID' 151)
- ITA party/alliance -- CCD/CDU unified; recoded old_partyID 140 into 53
- JPN cabinet -- Hatoyama I added DSP and KS
- JPN cabinet -- Koizumo II 'start_date' recoded to 2003-11-19; previous coding was linked to 2000 election results
- JPN cabinet -- Ohira I corrected 'start_date'
- LTU cabinet -- renamed Vagnorius cabinets by adding I and II
- LTU party -- LSDP split into two parties and recoded pre 2001 election results of LSDP to new party ID
- LVA cabinet -- 1998 legislative term correction of party composition for cabinets
- LVA cabinet -- Dombrovskis 2009 added
- LVA cabinet -- Skele I and Skele II added observations for non-partisan prime ministers ('pm') to 'cabinet_party'
- LVA election -- revision of election results (esp. 2002) during update to vote level data
- NLD cabinet -- coding of 'defector' parties
- MLT cabinet -- renamed cabinets to avoid duplicated cabinet names
- NLD cabinet -- Den Uyl government split into Den Uyl I and Den Uyl II (caretaker)
- NZL cabinet -- Howard I split into two cabinets taking 1951 election into account
- POL cabinet -- Kaczynski I, II, III, IV recoded into one cabinet -- following more specified cabinet coding rules
- POL cabinet -- Marcinkiewicz II corrected 'startingDate' from 2005 to 2006
- POL cabinet -- Pawlak I -- added party
- POL cabinet -- Suchocka II coded as 'caretaker'
- POL election -- LiD dissolution in April 2008 coded
- POL election -- 1992 PO recoded into POC
- POL party -- recoding of some party families
- ROU cabinet -- Athanasiu, Bejinariu coded as 'caretaker'
- SVN cabinet -- Jansa 'startingDate' recoded to 2004-12-03; previous coding was linked to 2000 election results
- SVN cabinet -- Peterle parties recoded
- SVN cabinet -- Drnovsek II removed ZS
- SVN election -- 1990 election added
- SVN election -- added two seats to each election one for Italian and the other for Hungarian national community seat
- SVN party -- SLS/SKD recoded into SLS

- corrected differences between coded and calculated (votes/votes_valid) vote shares (except PRT) -- ticket:56

#### Webpage

- new web design

- further information about cabinet below list of parties in cabinet
- list 'comment' in documentation of table variables
- show 0 seats on election result pages
- government type (minority, minimum winning, oversized) on cabinet pages and cabinet index -- ticket:36
- legend for tables on index pages of elections and cabinets
- Famfamfam silk icons for links to downloads
- information about recalculated seat shares in cabinet page
- smaller font size for election date on list of cabinets

#### Database

- complete database refactoring
  - renaming of tables and variables
  - unique primary keys in all tables (variable 'id')
    - old id variables are kept in core tables with prefix 'old\_' (eg. 'old_partyID' in party table)
  - foreign key enforcement (in Django)
  - 'data_json' variable for additional information in some tables (experimental version)
  - coding of all 'id' variables in 'info_id' -- except variables with an own table (e.g. country, party, election)
