# Avails and Committed Title List specifications
## Avails and Committed Title Lists for The Roku Channel
Roku requests an initial launch list of titles/episodes/shortForm videos in the current library that are available to Roku at the time of onboarding and a schedule when the content will be refreshed. For ongoing production, Roku requests that a Committed Title List be provided **60** days prior to licensing window start and the content be delivered in accordance with [The Roku Channel Ingest Specification](https://go.roku.com/ingest-ovp-specs) at least 30 days before licensing window start to allow ample time for selection, ingest, processing, and QC of the content before it goes live on The Roku Channel.
### Roku content policies
#### Ad-supported content on The Roku Channel
The Roku Channel is looking for ad-supported content that is appropriate for our users and advertisers – for example, The Roku Channel does not want ad-supported content that contains excessive nudity or extreme/graphic violence. Please use your best judgement when sharing content. If an asset is questionable, please find an alternative to share. We reserve the right to remove or reject any content that we deem inappropriate.
#### Kids directed content policy
“Kids-Directed Content” is content that either: (i) is directed to children as defined by the applicable law of the jurisdiction in which the content is shown (e.g., The Children's Online Privacy Protection Act); or (ii) was made for viewing primarily by children within the jurisdiction in which the content is shown.
  * You may NOT submit or distribute Kids-Directed content without Roku’s express written approval.
  * Roku must be made aware of the intent to submit or distribute Kids-Directed content via submission of the avails and Committed Title List document populating the columns outlined below:
    * Kids-Directed column must be populated with the value "true"
    * The Rating Source column must be populated with a valid Rating Source
    * The Rating Value column must be populated with a valid parental [Rating](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#ratings) from that Rating Source
    * “UNRATED” and “Not Rated” are not acceptable ratings for kids directed content

##### Optional age demographics tags
Additional tags can be provided to help categorize kids-directed content around age demographics. Please use these tags to define different content directed age groups:
Ages | Tags
---|---
Ages 1-3 | ages_1-3
Ages 4-6 | ages_4-6
Ages 7-9 | ages_7-9
Ages 10+ | ages_10plus
### Avails
“Avails” is short for availability. It refers to the list of available content for licensing or distribution. The avails list is shared with Roku to aid in understanding what content is currently available for acquisition or distribution. Avails typically include information about the titles, such as the title name, genre, duration, rights availability (e.g., exclusive or non-exclusive rights), and any other relevant details about the content. Avails should be sent to the Content Partnerships team (trcpartnersupport@roku.com) for Selections review. Once the Content Partnerships team has reviewed the Avails, they will provide the Avails sheet back with Selections marked for review and any revisions. The agreed-upon list of Selected content becomes the Committed Title List
### Committed Title List:
A “Committed title list” (CTL) is a comprehensive list of all the titles that have been committed and made available to Roku as agreed upon through the Selections process. Similar to avails, a CTL includes information about each title, such as the title name, genre, duration, and any other relevant details. CTLs are used for content management purposes and provide an overview of the committed content catalog from the content Partner. CTLs should be finalized for ingestion into Roku's Rights Management system at least 60 days prior to the start date of the titles in the list. The data provided in the CTL will control the availability of titles on The Roku Channel.
_The descriptive metadata (Title, Synopsis, Genre, etc.) provided in the avails and/or title list will be used for selection purposes only. Descriptive metadata must be included at the time the content is delivered in accordance with[The Roku Channel ingest specifications](https://go.roku.com/ingest-ovp-specs)._
### Availability windows
An availability window is the length of time during which a title is viewable by a user on The Roku Channel. Availability windows can include several different attributes in a number of combinations. Each unique combination of attributes bound by a start and end time is considered its own availability window. Each availability window should be represented in the avails or Committed Title List on its own row. The availability attributes currently supported by Roku are:
  * License Type
  * Territory
  * Language

#### Availability date and time
Roku has the ability for content to display on-device and for user playback at a specific starting time. By default, content will go into window at 12:00 am (midnight) and expire at 11:59:59 pm in the users’ time zone.
If content is to go live at a time other than midnight or expire at a time other than 11:59:59 pm, the license window start or end values in the inbound metadata must include the desired times.
There are two types of specific time designations – relative and absolute.
  * Relative Time – a Saturday night premiere of a movie goes into window at 9pm local time for all users. A user in the Eastern Time Zone watches at 9pm but a user in the Pacific Time Zone, at the exact same moment (6pm PT), cannot watch that content.
  * Absolute Time – a new episode of a series goes into window at 9pm Eastern and becomes immediately available across all time zones. A user in the Pacific Time Zone can watch the content at 6 pm local time.
While time settings are dictated by the content owner, Roku will need the metadata as follows:
  * If the content has a relative start time, that time must be indicated in the ingest metadata and formatted as “yyyy-mm-ddThh:mm:ss” (2019-11-01T21:00:00)
  * If the content has an absolute start time, that time must be indicated in the ingest metadata. The time must be presented as UTC time and formatted as “yyyy-mm-ddThh:mm:ssZ” (2019-11-02T01:00:00Z).
  * In this example, 9 pm Eastern Time on November 1 is 1 am UTC (<https://www.thetimezoneconverter.com>)
  * If the metadata arrives without a time, Roku will assume a relative start time of 12:00:00 am and a relative end time of 11:59:59 pm

### Submitting Excel Avails/Committed Title Lists
Avails must be submitted via email to trcpartnersupport@roku.com for selection review. Committed Title Lists must be finalized at least 60 days prior to the intended licensing window start date of the titles within the list. In certain cases we may be able to accept avails and Committed Title Lists via Aspera. Please reach out to your Roku representative for current delivery options.
When submitting avails and Committed Title Lists via Excel workbook, all required fields must be populated. Roku has provided hints on row 2 of the Roku avails and Committed Title List template to highlight the required cells and any special formatting needed for each cell. Please refer to these hints when filling out the Roku avails and Committed Title List template. Other considerations when filling out the Roku Avails and Committed Title List Excel sheet include:
  * All data MUST begin on row 3. DO NOT DELETE THE HINTS ON ROW 2
  * Any formulas used must be converted to text prior to submission. Inclusion of a formula will result a rejection of the avails and Committed Title List sheet
  * Do not link to external data or Excel workbooks. All data must be self contained within the Excel workbook delivered to Roku
  * Do not add additional sheets to the workbook
  * Do not add additional columns to the workbook
  * Do not change any of the column header names
  * Do not supply a value of “N/A” or “n/a”. Required cells should contain valid data and optional cells may be left blank
  * Each row is considered a unique availability window for an episode/movie/shortForm video
  * Do not leave a blank row between entries in a worksheet. The system will terminate processing at the first empty row
  * Avails and Committed Title List sheets must be saved with .xlsx extension

## Avails and Committed Title List sheet field definitions
### Availability attribute fields
**Field** | **Description** | **Type** | **Accepted Values** | **Required**
---|---|---|---|---
Content Partner | Name of content owner/studio/network availing the content to The Roku Channel | string | Example:
Roku Originals | required
Content Type | Describes the content type of the program as defined below:

  * **episode** - TV program that is structured in a series/season/episode hierarchy
  * **movie** - Full length, long form, stand-alone program that is not intended to be nested in a series/season/episode hierarchy and exceeds roughly 15 minutes run time including stand-alone TV Specials
  * **shortForm** - Short duration, stand-alone program that does not exceed roughly 15 minutes run time and is not intended to be nested in a series/season/episode hierarchy

| enum | movie, episode, shortForm | required
License Type | Available distribution rights for the content. Multiple rights may be submitted on the same row so long as all availability attributes are identical across the rights listed. The License Type provided in the Avails or Committed Title List must adhere to the distribution rights for the content as it pertains to the agreement signed with The Roku Channel.

  * **AVOD** – Ad-Supported Video on Demand. Video will play for free for all users and will contain advertisements
  * **SVOD** – Subscription Video on Demand. Video will play for users with an active subscription. _Only to be used by Premium Subscriptions Partners on The Roku Channel_
  * **FVOD** – Free Video on Demand. Video will play for free for all users without monetization. FVOD windows must fall within an active SVOD window. _Only to be used by Premium Subscriptions Partners on The Roku Channel_
  * **Linear OTT** - Over-the-top linear streaming rights for inclusion on Roku-built channels

| enum | AVOD, SVOD, FVOD, Linear OTT | required
Excluded Rights | Distribution exclusions for the content. Multiple exclusions may be submitted on the same row so long as all availability attributes are identical across the rights listed.

  * **AVOD** – Ad-Supported Video on Demand. Video will play for free for all users and will contain advertisements
  * **SVOD** – Subscription Video on Demand. Video will play for users with an active subscription. _Only to be used by Premium Subscriptions Partners on The Roku Channel_
  * **FVOD** – Free Video on Demand. Video will play for free for all users without monetization. FVOD windows must fall within an active SVOD window. _Only to be used by Premium Subscriptions Partners on The Roku Channel_
  * **Linear OTT** - Over-the-top linear streaming rights for inclusion on Roku-built channels

| enum | AVOD, SVOD, FVOD, Linear OTT | optional
Start Date | Start of availability in YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS format. If the content has no set Start Date, “open” is an acceptable value. Start Dates without time values will assume a relative start time of 12:00:00 am on the Start Date listed | date string | YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or open | required
End Date | End of availability in YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS format. If the content has no set End Date, “open” or “end of term” are acceptable values. End Dates without time values will assume relative end times of 11:59:59 pm on the End Date listed | date string | YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, open, or end of term | required
Language | The language(s) that will be made available to users of The Roku Channel. Language values must conform to one of the enumerated [supported language codes](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#language-codes). Multiple language/localizationType combinations may be provided on the same row so long as all availability attributes are identical across the languages listed. When multiple languages are provided, the localization type related to that language must be included by appending a colon (":") and the localization type as defined below.

  * **dub** – indicates the language property refers to an audio track. Applicable to original voice audio
  * **sub** – indicates the language property refers to subtitle
  * **subdub** – includes both subtitles and dubbed audio
  * **any** – includes any combination of subtitles or dubbed audio (whatever is available)

| enum | Examples:
en:dub, fr:sub, de:subdub, es-mx:any | required
Localization Type | Applies to the Language column when only a single language code is provided. Indicates that the language property refers to either an audio track or a text track (subtitle). Localization Type would be “dub” for original voice audio. Valid values defined below:

  * **dub** – indicates the language property refers to an audio track. Applicable to original voice audio
  * **sub** – indicates the language property refers to subtitle
  * **subdub** – includes both subtitles and dubbed audio
  * **any** – includes any combination of subtitles or dubbed audio (whatever is available)

| enum | sub, dub, subdub, any | required when providing a single language in the Language column
Excluded Languages | The language(s) that must not be made available to users of The Roku Channel. Language values must conform to one of the enumerated [supported language codes](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#language-codes). Multiple language combinations may be provided on the same row so long as all availability attributes are identical across the languages listed. | enum | Example:
en, de | optional
Territory |  [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search) country code for the country or territory in which the content may be made available. Multiple territories may be submitted on the same row so long as all availability attributes are identical across the territories listed. | enum | Example:
US, CA, GB, MX, LATAM, WW | required
Excluded Territories |  [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search) country code for the country or territory for which the content should NOT be made available. Multiple territories may be excluded. | enum | Example:
DE, FR | optional
### Title metadata fields
**Field** | **Description** | **Type** | **Accepted Values** | **Required**
---|---|---|---|---
Series Title | Title of series for episodic TV content. Include only the name of the series as it should appear on platform. Do not include non-title parentheticals such as indicator of original/remake, year of release, or video format. Examples: (Classic), (1987), or (Season #) | string | Example:
Die Hart | required for tv
Series ID | Immutable, unique identifier for a TV series. IDs are to be generated and supplied by the Partner for content that is availed and delivered to Roku. The IDs in the avails and Committed Title List document should match the IDs provided in the metadata at the time of ingest into The Roku Channel.

  * Must not be the same as the unique episode ID
  * Must be included with all episodes of a series
  * Must be consistent for all episodes of a series
  * Must not exceed 50 characters
  * Allowable characters: alphanumeric characters, hyphens, and underscores only

| string | Example:
diehartshow | required for tv
50 characters maximum
Title | Title of the movie, episode, or shortForm video. Include only the name of the content as it should appear on platform. Do not include non-title parentheticals such as indicator of original/remake, year of release, season, or video format. Examples: (Classic), (1987), (Season 1), or (HD) | string | Example:
Pilot | required
Title ID | Immutable, unique identifier for a movie, episode, or shortForm video. IDs are to be generated and supplied by the Partner for content that is availed and delivered to Roku. The IDs in the avails and Committed Title List document should match the IDs provided in the metadata at the time of ingest into The Roku Channel. This will aid in tracking the content throughout Roku’s pipeline from avails and Committed Title List submission through publication on The Roku Channel.

  * Must not exceed 50 characters
  * Allowable characters:alphanumeric characters, hyphens, and underscores only

| string | Example:
dieharts1e1 | required
50 characters maximum
Season Number | Season number for the episode. Must follow the original broadcast/distribution sequence of seasons and must be a number. Letters are not allowed | integer | #, ##, … | required for tv
Episode Number | Episode number. Must follow the original broadcast/distribution sequence of episodes within a season and must be a number. Letters are not allowed.
Do not use production numbers (e.g. 201 for season 2 episode 1) | integer | #, ##, … | required for tv
Country of Origin | Defines the primary country where the film was produced and where the main creators, crew, and producers are established. Value must conform to one of the supported country codes as defined in the [ISO 3166-1 alpha 2](https://www.iso.org/iso-3166-country-codes.html) list of 2-character country codes. Please include 1 country only | enum | Example:
US, CA, DE | required
1 country only
Original Spoken Language | Language in which the content was produced. This is usually the primary language of the country of origin and the language that synchronizes exactly with the movements of the performers mouths as they speak. Must conform to one of the enumerated [supported language codes](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#language-codes). May include multiple languages separated by commas. | enum | Example:
en-us, fr-ca
| required
Run Time | Runtime of the content in whole minutes. Minimum runtime is 1 | integer | Example:
22 | required
Format | Highest video resolution available for the content. All lower resolutions will be assumed* | enum | SD, HD, UHD | required
DBO | Domestic Box Office Gross | string | $2,000,000 | optional
Closed Captioning | Communicating if captions are included with the content per [FCC guidelines](https://www.fcc.gov/consumers/guides/captioning-internet-video-programming). If captions are not included with the content, a Caption Exemption value must be provided | Boolean | true
false | required
Caption Exemption | US avails only. FCC exemption for closed caption requirement. Allowable value and their definitions:

  1. The content has never aired on television in the United States.
  2. The content has only aired on television in the United States without captions.
  3. The content has not aired on television in the United States with captions since September 30, 2012.
  4. The content does not consist of full-length video programming.
  5. The content does not fall within a category of online programming that requires captions under FCC regulations (49 C.F.R. § 79.4(b)).
  6. The FCC and/or U.S. Congress has granted an exemption from captioning requirements for this content.

| enum | 1, 2, 3, 4, 5, 6 | required if Caption Included is false
Audio Description** (see note below) | Communicating if an audio description track is included with the content. [Audio description](https://www.fcc.gov/audio-description) (also referred to as video description) is audio-narrated descriptions of a television program's key visual elements. These descriptions are inserted into natural pauses in the program's dialogue. Audio description makes television programming more accessible to individuals who are blind or visually impaired. If Audio Description is required for content, and is not provided, an Audio Description Exemption must be included. | Boolean | true
false | optional
Audio Description Exemption** (see note below) | Exemption reason for not providing audio description track where required. | string |  | optional
Original Release Date | Original date content was first made available in any presentation. Must include year of release at a minimum | date string | YYYY-MM-DD or YYYY | required
Genre | Genre classification of the content. May provide multiple genres separated by comma | enum | See [Genres](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#genres) for allowed values | required
Tags | Free form field to provide keywords, tags, categories, or keywords to be used to surface content on The Roku Channel UI. Please see our [Best Practices](https://developer.roku.com/trc-docs/video-on-demand/content-tags-and-metadata.md) page on how best to provide tags to The Roku Channel | string | exciting, timely, political | optional
Rating Source | Rating system applied to the edit of title within territory of avail. Rating systems should be formatted and paired with Rating Value as per [Ratings](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#ratings) | enum | See [Ratings](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#ratings) for allowed values | optional
Rating Value | Value representing the rating within the specified Rating Source. Ratings should be formatted and paired with Rating Source as per [Ratings](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#ratings) | enum | See [Ratings](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#ratings) for allowed values | optional
Kids-Directed | Indicator that the content is intended for young audiences/family audiences. Must adhere to guidelines defined in [Kids Directed Content Policy](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#kids-directed-content-policy) | Boolean | true, false | optional
Recommended Age Group | When Kids Directed is True, a recommended age range for the content can be supplied. Only one Recommended Age Group allowed. Allowable values:

  * **ages_1-3** - For viewers 1 to 3 years of age
  * **ages_4-6** - For viewers 4 to 6 years of age
  * **ages_7-9** - For viewers 7 to 9 years of age
  * **ages_10plus** - For viewers ages 10 and up

| enum | ages_1-3, ages_4-6, ages_7-9, ages_10plus | optional Used when Kids-Directed is true
Main Cast | Top billed cast of content separated by comma in Firstname Lastname format | list | Example:
Kevin Hart, John Travolta | required
Synopsis | A short synopsis of the content being availed for the purposes of content selection. Not to exceed 250 characters | string |  | required
External ID Source | Source entity for external ID provided. Allowable values:

  * **TMS** – Gracenote ID
  * **IMDb** – IMDb ID
  * **Wiki** – Wikipedia ID

May include IDs from multiple sources, separated by commas. ID originating from that source is indicated by appending a colon (":") and the ID | string | Example:
TMS, IMDb, Wiki
IDs from multiple sources examples:
TMS:E12345678, IMDb:tt12345678, Wiki:benson_s1_e1 | optional
Series External ID | 3rd party identifier of the series | string | Example:
diehartshowExtId | optional
External ID | 3rd party identifier of the content | string | Example:
dieharts1e1ExtId | optional
Screener Link | URL link to stream or download a screener for the content. Any passwords required should also be included. Inclusion of a screener is helpful for content selection | string | Example:
<https://urlLinkToScreener>
password: 1234 | optional
Exclusive | Indicator that the content is available exclusively on The Roku Channel | Boolean | true, false | optional
Notes | Free form field for additional avail notes. For linear content, runs and telecast restrictions, or any other specifics not captured in the avails and Committed Title List document should be recorded here | string |  | optional
Merchant of Record | Name of the entity to which financial transactions should be attributed if other than the Content Partner listed | string | Example:
Roku | optional
Day Parting | For Linear content ONLY
Any dayparting rules for the content | string |  | optional
*_Roku does not support the playback of UHD/4K content at this time but can accept UHD/4K as a source to make available for playback in the future._
_**The Roku Channel prefers to make as much content accessible to as many users as possible. Audio Description, while not currently required for all content by the FCC at this time, may be in the future._
### Ratings
A valid film or TV rating from the rating authority (Rating Source) of the Territory the title will be available in shall be provided for each movie, episode, or shortForm video. If the title has not been rated by that Territory’s official rating authority, a rating of NR (Not Rated) may be provided, however please note that Roku strongly prefers an actual rating on all content. Titles with a rating of NR (Not Rated) will be subject to manual verification which can delay the selection process and publishing to The Roku Channel. Discoverability on The Roku Channel may also be impacted for titles with the NR (Not Rated) rating and placement within the Kids & Family experience will be prohibited. In lieu of the NR (Not Rated) rating, the title should be self rated using the USA_PR rating system. Guidelines pertaining to the USA_PR ratings can be found [here](http://tvguidelines.org/)
#### Rating values by rating system and country
**Ratings Authority and Territory** | **Country** | **ratingSystem** | **Rating Value** |  |
---|---|---|---|---|---
British Board of Film Classification
United Kingdom | GB | BBFC | U
PG
12A | 12-A
12
15 | 18
NR[*](https://developer.roku.com/en-gb/trc-docs/video-on-demand/avail/title-avail-specifications.md#unrated-vs-not-rated)
R18
R-1
Canadian Home Video Rating System
Canada | CA | CHVRS | G
PG
14A | 14-A
18A
18-A | NR
RE
Motion Picture Associate of America
United States | US | MPAA | G
PG
PG13 | PG-13
R
NC-17 | NC17
NR
Canadian Parental Rating
Canada | CA | CPR | 14+
18+
C | C8
C-8
G | NR
PG
E
Dirección General de Radio, Televisión y Cinematografía
Mexico | MX | RTC | AA
A
B | B-15
B15
C | DD
D
NR
USA Parental Rating (V-Chip)
United States | US | USA_PR | TV-Y
TVY
TV-Y7
TVY7 | TV-G
TVG
TV-PG
TVPG | TV-14
TV14
TV-MA
TVMA
NR
### Genres
Below is the complete list of supported Genres for The Roku Channel
|  |  |
---|---|---|---
action
action sports
adventure
aerobics
agriculture
animals
animated
anime
anthology
archery
arm wrestling
art
arts/crafts
auction
auto
auto racing
aviation
awards
badminton
ballet
baseball
basketball
beach soccer
beach volleyball
biathlon
bicycle
bicycle racing
billiards
biography
blackjack
boat
boat racing
bobsled
bodybuilding
bowling
boxing
bullfighting
bus./financial
canoe
card games
cheerleading
children
children-music
children-special
children-talk
collectibles
comedy
comedy drama
community
computers
consumer
cooking
cricket | crime
crime drama
curling
dance
dark comedy
darts
debate
diving
docudrama
documentary
dog racing
dog show
dog sled
drag racing
drama
educational
entertainment
environment
equestrian
erotic
event
exercise
fantasy
faith
fashion
fencing
field hockey
figure skating
fishing
football
food
fundraiser
gaelic football
game show
gaming
gay/lesbian
golf
gymnastics
handball
health
historical drama
history
hockey
holiday
holiday music
holiday music special
holiday special
holiday-children
holiday-children special
home improvement
horror
horse | house/garden
how-to
hunting
hurling
hydroplane racing
indoor soccer
interview
intl soccer
kayaking
lacrosse
law
luge
martial arts
medical
military
miniseries
mixed martial arts
motorcycle
motorcycle racing
motorsports
mountain biking
music
music special
music talk
musical
musical comedy
mystery
nature
news
newsmagazine
olympics
opera
outdoors
parade
paranormal
parenting
performing arts
playoff
sports
poker
politics
polo
pool
pro wrestling
public affairs
racquet
reality
religious
ringuette
rodeo
roller derby
romance
romance comedy | rowing
rugby
running
sailing
science
science fiction
self improvement
shooting
shopping
sitcom
skateboarding
skating
skeleton
skiing
snooker
snowboarding
snowmobile
soap
soap special
soap talk
soccer
softball
special
speed skating
sports
sports talk
squash
standup
sumo wrestling
surfing
suspense
swimming
table tennis
talk
technology
tennis
theater
thriller
track/field
travel
triathlon
variety
volleyball
war
water polo
water skiing
watersports
weather
weightlifting
western
wrestling
yacht racing
### Language codes
The below list is the full set of language codes Roku currently supports for content ingest. This list is a simplified version of the [RFC 5646](https://datatracker.ietf.org/doc/html/rfc5646) specification.
Language Code | Language | Language Code | Language
---|---|---|---
af | Afrikaans | km | Khmer
sq | Albanian | rw | Kinyarwanda
am | Amharic | ko | Korean
ar | Arabic | ko-kr | Korean (Korea)
ar-dz | Arabic (Algeria) | ku | Kurdish
ar-bh | Arabic (Bahrain) | ky | Kyrgyz
ar-eg | Arabic (Egypt) | lo | Lao
ar-iq | Arabic (Iraq) | la | Latin
ar-jo | Arabic (Jordan) | lv | Latvian
ar-kw | Arabic (Kuwait) | lt | Lithuanian
ar-lb | Arabic (Lebanon) | mk | Macedonian
ar-ly | Arabic (Libya) | mg | Malagasy
ar-ma | Arabic (Morocco) | ms | Malay
ar-om | Arabic (Oman) | ms-my | Malay (Malaysia)
ar-qa | Arabic (Qatar) | ml | Malayalam
ar-sa | Arabic (Saudi Arabia) | mt | Maltese
ar-sy | Arabic (Syria) | mr | Marathi
ar-tn | Arabic (Tunisia) | mn | Mongolian
ar-ae | Arabic (U.A.E.) | nd | Ndebele
ar-ye | Arabic (Yemen) | ne | Nepali
hy | Armenian | no | Norwegian
as | Assamese | no-no | Norwegian (Norway)
az | Azerbaijani | or | Oriya
eu | Basque | om | Oromo
be | Belarusian | ps | Pashto
bn | Bengali | fa | Persian (Farsi)
bh | Bihari | pl | Polish
bs | Bosnian | pl-pl | Polish (Poland)
bg | Bulgarian | pt | Portuguese
bg-bg | Bulgarian (Bulgary) | pt-br | Portuguese (Brazil)
my | Burmese | pt-pt | Portuguese (Portugal)
ca | Catalan | pa | Punjabi
zh | Chinese | qu | Quechua
zh-hk | Chinese (Hong Kong) | rm | Rhaeto-Romanic
zh-cn | Chinese (PRC) | ro | Romanian
zh-sg | Chinese (Singapore) | ro-md | Romanian (Republic of Moldova)
zh-tw | Chinese (Taiwan) | ro-ro | Romanian (Romania)
zh-hans | Chinese (Simplified) | rn | Rundi
zh-hant | Chinese (Traditional) | ru | Russian
hr | Croatian | ru-md | Russian (Republic of Moldova)
hr-hr | Croatian (Croatia) | ru-ru | Russian (Russia)
cs | Czech | se | Sami
cs-cz | Czech (Czech Republic) | sa | Sanskrit
da | Danish | gd | Scottish (Gaelic)
da-dk | Danish (Denmark) | sr | Serbian
dv | Divehi | sn | Shona
nl | Dutch | ii | Sichuan Yi
nl-be | Dutch (Belgium) | sd | Sindhi
nl-nl | Dutch (Netherlands) | si | Sinhalese
dz | Dzongkha | sk | Slovak
en | English | sl | Slovenian
en-au | English (Australia) | sl-si | Slovenian (Slovenia)
en-bz | English (Belize) | so | Somali
en-ca | English (Canada) | st | Sotho
en-ie | English (Ireland) | es | Spanish
en-jm | English (Jamaica) | es-ar | Spanish (Argentina)
en-nz | English (New Zealand) | es-bo | Spanish (Bolivia)
en-za | English (South Africa) | es-cl | Spanish (Chile)
en-tt | English (Trinidad) | es-co | Spanish (Colombia)
en-gb | English (United Kingdom) | es-cr | Spanish (Costa Rica)
en-us | English (United States) | es-do | Spanish (Dominican Republic)
et | Estonian | es-ec | Spanish (Ecuador)
fo | Faeroese | es-sv | Spanish (El Salvador)
fi | Finnish | es-gt | Spanish (Guatemala)
fr | French | es-hn | Spanish (Honduras)
fr-be | French (Belgium) | es-mx | Spanish (Mexico)
fr-ca | French (Canada) | es-ni | Spanish (Nicaragua)
fr-lu | French (Luxembourg) | es-pa | Spanish (Panama)
fr-ch | French (Switzerland) | es-py | Spanish (Paraguay)
fy | Frisian | es-pe | Spanish (Peru)
ff | Fulfulde (Fulah) | es-pr | Spanish (Puerto Rico)
gl | Galician | es-es | Spanish (Spain)
ka | Georgian | es-uy | Spanish (Uruguay)
de | German | es-ve | Spanish (Venezuela)
de-at | German (Austria) | sw | Swahili
de-de | German (Germany) | sv | Swedish
de-li | German (Liechtenstein) | sv-fi | Swedish (Finland)
de-lu | German (Luxembourg) | sv-se | Swedish (Sweden)
de-ch | German (Switzerland) | tl | Tagalog
el | Greek | ty | Tahitian
el-gr | Greek (Greece) | tg | Tajik
gn | Guarani | ta | Tamil
gu | Gujarati | tt | Tatar
ht | Haitian (Creole) | te | Telugu
ha | Hausa | th | Thai
he | Hebrew | th-th | Thai (Thailand)
hi | Hindi | bo | Tibetan
hu | Hungarian | ti | Tigrigna
hu-hu | Hungarian (Hungary) | ts | Tsonga
is | Icelandic | tn | Tswana
ig | Igbo | tr | Turkish
id | Indonesian | tr-tr | Turkish (Turkey)
iu | Inuktitut | tk | Turkmen
ik | Inupiaq | uk | Ukrainian
ga | Irish | ur | Urdu
it | Italian | uz | Uzbek
it-it | Italian (Italy) | ve | Venda
it-ch | Italian (Switzerland) | vi | Vietnamese
ja | Japanese | vi-vn | Vietnamese (Vietnam)
ja-jp | Japanese (Japan) | cy | Welsh
kn | Kannada | xh | Xhosa
kr | Kanuri | yi | Yiddish
ks | Kashmiri | yo | Yoruba
kk | Kazakh | zu | Zulu
## Resources
Title | Link
---|---
Roku Avails and Committed Title List Excel Template | <https://go.roku.com/trc-avail-template>
US MPAA Ratings | <https://www.filmratings.com/>
US TV Ratings | <http://tvguidelines.org/>
UK BBFC Ratings | <https://bbfc.co.uk/>
Canadian Film Ratings | <https://www.mpa-canada.org/film-ratings/>
Canadian TV Ratings | <https://www.cbsc.ca/tools/for-english-ca-and-third-language-broadcasters/>
FCC Closed Captioning Guide | <https://www.fcc.gov/consumers/guides/captioning-internet-video-programming>
FCC Audio Description | <https://www.fcc.gov/audio-description>
Sample Avails/Committed Title Lists | <https://go.roku.com/avail-ctl-samples>
## Change Log
**v1.3 - 2024-04-22**
  * Defined Avails and Committed Title List
  * Added Ad-supported content guideline
  * Renamed "Rights Available" to "License Type"
  * Added availability windows section
  * Added distribution lists for delivery of avail and Committed Title List sheets
  * Clarified: Country of Origin, Language, Season Number, Episode Number fields
  * Separated field definitions into sections
  * Replaced Window Type with FVOD Right
  * Defined License Types
  * Clarified when and where to provide Localization Type
  * Fixed Localization Type list of supported values
  * Updated ratings table to the format used in the Ingest Specification
  * Updated language codes table to align with the list used in the Ingest Specification
  * Removed UR as a valid rating
  * Added preference that not rated content be self rated using USA_PR system
  * Removed Reference ID
  * Added maximum character limit for Series and Title IDs
  * Added Excluded Rights
  * Added Excluded Languages
  * Updated max character count for Synopsis to 250
  * Added requirement to remove links to external data in Excel workbooks
  * Updated example data
  * Updated Tags to reference Best Practices page
  * Updated template with Instructions and more hints on Row 2
  * Added zip file contains sample documents