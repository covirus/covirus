

  ## covirus: #STAY_HOME
  
  ![PyPI](https://img.shields.io/pypi/v/covirus)  [![Build Status](https://travis-ci.com/maricatovictor/covirus.svg?branch=master)](https://travis-ci.com/maricatovictor/covirus)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
  
## What is it?
**covirus** is a Python library to centralize data and models related to COVID19 outbreak. Its goal is to make importing data and running models easier, allowing many researchers and also data enthusiasts to help understand how **COVID-19** is spreading worldwide and what to expect.

## Table of Contents

- [covirus: #STAY_HOME](#covirus-stayhome)
- [What is it?](#what-is-it)
- [Table of Contents](#table-of-contents)
- [Main Features](#main-features)
    - [Current](#current)
    - [Future](#future)
- [Installation](#installation)
- [Usage](#usage)
  - [Datasets](#datasets)
  - [Models](#models)
      - [SIR](#sir)
- [Documentation](#documentation)
- [References](#references)
  - [Data Sources](#data-sources)
- [Other COVID-19 projects](#other-covid-19-projects)
    - [Worldwide](#worldwide)
    - [Brazil](#brazil)
- [Contributing](#contributing-img-src%22httpswwwcodetriagecommaricatovictorcovirus%22-alt%22open-source-helpers%22)
  - [Code Style](#code-style)
  - [Running the Tests](#running-the-tests)
    - [Docker](#docker)
    - [Local](#local)
  - [Adding Dependencies](#adding-dependencies)
  - [Directory Structure](#directory-structure)
- [License](#license)

## Main Features

#### Current
* Datasets: we provide an Dataset object for each dataset inside the lib. Each object may have one or more `pd.DataFrame` and other useful infos about specific datasets available around the world.

* Models: i.e.: SIR, SEIR, Bayesian estimators will be provided to facilitate predictions and projections. These models should be validated by a health professional, i.e: epidemiologist.


#### Future
* Preprocessors: pipelines for working with datasets in the lib.

## Installation
The source code is currently hosted on GitHub at:
https://github.com/maricatovictor/covirus/tree/master/covirus

PyPI: https://pypi.org/project/covirus/

Run:
```sh
pip install covirus
```


## Usage

### [Datasets](https://github.com/maricatovictor/covirus/tree/master/covirus/data)

[wcota](https://github.com/wcota/covid19br) - Confirmed cases and deaths of COVID-19 in Brazil, at municipal (city) level. https://wcota.me/covid19br

```python
>>> from covirus.data import load_dataset
>>> data = load_dataset(country="BR", source="wcota") # Reference: covirus/data/
>>> data.cities.head()
>  country state             city   ibgeID  deaths  totalCases
0  Brazil    PA    Abaetetuba/PA  1500107       0           2
1  Brazil    CE       Abaiara/CE  2300101       0           1
2  Brazil    PE  Abreu e Lima/PE  2600054       0           1
3  Brazil    AC    Acrelândia/AC  1200013       0           9
4  Brazil    SP    Adamantina/SP  3500105       0           0
```

### [Models](https://github.com/maricatovictor/covirus/tree/master/covirus/models)

##### SIR
```python
>>> from covirus.models.compartiment import SIR
>>> sir = SIR()
>>> pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate = (
      1000,
      1,
      0,
      0.2,
      1 / 10, #1 recovered per 10 days
  )
>>> sir.fit(pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate)
>>> S, I, R = sir.predict(days=160)
>>> sir.plot()
>
```
Outputs:
![SIR-generated-2020-04-11](https://user-images.githubusercontent.com/11489228/79053576-d13f5400-7c14-11ea-8dc6-b01fea6f3ada.jpg)

## Documentation

Unfortunely, we still do not provide a documentation page :(

## References
#### Data Sources
Please for more specific data-sources info, [refer to `data/`](https://github.com/maricatovictor/covirus/tree/master/covirus/data)

#### Models
* [3778/COVID-19](https://github.com/3778/COVID-19)
* [SIR](https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/)

## Other COVID-19 projects
#### Worldwide
* [nCOV nextstrain](https://nextstrain.org/ncov/global?l=radial&s=Wuhan-Hu-1/2019) - Genomic & Bioinformatics analysis
* [Ventilador](https://www.codetriage.com/jcl5m1/ventilator) - Low-Cost Open-Source Ventilator-ish Device

#### Brazil
* [LOFT Report](https://docs.google.com/document/d/1c8U-eZSZQwr8m3KifQBndBOv0WlDDJ9aD0VPYATe3cg/edit) - LOFT analyses
*  [3778/COVID-19](https://github.com/3778/COVID-19) - Analyses

## Contributing [![Open Source Helpers](https://www.codetriage.com/maricatovictor/covirus/badges/users.svg)](https://www.codetriage.com/maricatovictor/covirus)

### Code Style
We use [Black](https://github.com/psf/black) code-style here.
Also, for Docstrings, please use [Google Docstring Styleguide](https://github.com/google/styleguide)




### Running the Tests

#### Docker
From project's root, run:
```sh
sh bin/test.sh
```

#### Local
From project's root, run:
```sh
pip install -r requirements.txt -r dev-requirements.txt
pytest [-s | -x | -log-level=INFO] covirus/tests/
```

### Adding Dependencies

Please add dependencies to `requirements.in` (or `dev-requirements.in`)

After that, from project's root, run:
```sh
sh bin/compile-requirements.sh
```

### Directory Structure

Source code in `covirus/`
A draft of how this project is structured.


| File or directory                              | Contents                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------- |
| 📁bin/                                          | Algorithm's implementation                                          |
| ├📄test.sh/                                     | Run Tests!                                                          |
| ├📄compile-requirements.sh/                     | Compile [dev-]requirements.in                                       |
| 📁covirus/                                      | Source code                                                         |
| ├📁tests/                                       | We love tests :)                                                    |
| &#124; &#124; ├📁{feature}                      | i.e: datasets                                                       |
| &#124; &#124; &#124; ├📄test_something.py       | One of the tests for the feature                                    |
| ├📁data/                                        | Where anything data related will be placed                          |
| &#124; &#124; ├📁countries/                     | Country-specific data                                               |
| &#124; &#124; &#124; ├📁brazil/                 | :brazil:                                                            |
| &#124; &#124; &#124; &#124; ├📁source/          | Where downloading and loading sources should be placed              |
| &#124; &#124; &#124; &#124; &#124; ├📄 wcota.py | One of the tests for the feature                                    |  |
| &#124; &#124;  ├📄 datasets.py                  | Where you will find Dataset class the is returned by `load_dataset` |
| &#124; &#124;  ├📄 `__init__.py`                | Holds `load_dataset`                                                |  |
| ├📁models/                                      | Where models **will** be placed                                     |


## License
[MIT](https://github.com/maricatovictor/covirus/blob/master/LICENSE)
