## Datasets

One of main goals of **covirus** is provide ready-to-use [Datasets](https://github.com/maricatovictor/covirus/blob/master/covirus/data/dataset.py)

## Currently Available Datasets

| country | source | Description | Objects
|--|--|--|--|
|   | `johns_hopkins`  | Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE. <br>Available at: https://github.com/CSSEGISandData/COVID-19 | iso_codes, <br> who_report, <br> timeline["deaths"], timeline["recovered"], <br> timeline["confirmed"] , timeline["US"]["deaths"], timeline["US"]["confirmed"], <br> daily_reports available on report("%d-%m-%Y") or report(datetime)
|   | `cbc_news`  | You might find many insights with more than 3,500 CBC news articles. It contains the authors, the title, the publish date, the description about the story, the main story, and the url. <br>Available at: https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26  | Returns a pd.DataFrame.
| `BR`  | `wcota`  | Casos e óbitos confirmados por dia, utilizando informação oficial pelo  [Ministério da Saúde](https://covid.saude.gov.br/), dados no nível municipal do  [Brasil.IO](https://brasil.io/dataset/covid19/caso)  e dados mais recentes reportados pela equipe do  [@CoronavirusBra1](https://twitter.com/CoronavirusBra1). <br>Disponível em:  [https://wcota.me/covid19br](https://wcota.me/covid19br) | cities, cities_time, states, total
