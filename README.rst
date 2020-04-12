## covirus: #STAY\_HOME

|PyPI| |Build Status| |Code style: black|

What is it?
-----------

**covirus** is a Python library to centralize data and models related to
COVID19 outbreak. Its goal is to make importing data and running models
easier, allowing many researchers and also data enthusiasts to help
understand how **COVID-19** is spreading worldwide and what to expect.

Table of Contents
-----------------

-  `covirus: #STAY\_HOME <#covirus-stayhome>`__
-  `What is it? <#what-is-it>`__
-  `Table of Contents <#table-of-contents>`__
-  `Main Features <#main-features>`__

   -  `Current <#current>`__
   -  `Future <#future>`__

-  `Installation <#installation>`__
-  `Usage <#usage>`__
-  `Datasets <#datasets>`__
-  `Models <#models>`__

   -  `SIR <#sir>`__

-  `Documentation <#documentation>`__
-  `References <#references>`__
-  `Data Sources <#data-sources>`__
-  `Other COVID-19 projects <#other-covid-19-projects>`__

   -  `Worldwide <#worldwide>`__
   -  `Brazil <#brazil>`__

-  `Contributing <#contributing-img-src%22httpswwwcodetriagecommaricatovictorcovirus%22-alt%22open-source-helpers%22>`__
-  `Code Style <#code-style>`__
-  `Running the Tests <#running-the-tests>`__

   -  `Docker <#docker>`__
   -  `Local <#local>`__

-  `Adding Dependencies <#adding-dependencies>`__
-  `Directory Structure <#directory-structure>`__
-  `License <#license>`__

Main Features
-------------

Current
^^^^^^^

-  Datasets: we provide an Dataset object for each dataset inside the
   lib. Each object may have one or more ``pd.DataFrame`` and other
   useful infos about specific datasets available around the world.

-  Models: i.e.: SIR, SEIR, Bayesian estimators will be provided to
   facilitate predictions and projections. These models should be
   validated by a health professional, i.e: epidemiologist.

Future
^^^^^^

-  Preprocessors: pipelines for working with datasets in the lib.

Installation
------------

| The source code is currently hosted on GitHub at:
| https://github.com/maricatovictor/covirus/tree/master/covirus

PyPI: https://pypi.org/project/covirus/

Run:

.. code:: sh

    pip install covirus

Usage
-----

`Datasets <https://github.com/maricatovictor/covirus/tree/master/covirus/data>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`wcota <https://github.com/wcota/covid19br>`__ - Confirmed cases and
deaths of COVID-19 in Brazil, at municipal (city) level.
https://wcota.me/covid19br

.. code:: python

    >>> from covirus.data import load_dataset
    >>> data = load_dataset(country="BR", source="wcota") # Reference: covirus/data/
    >>> data.cities.head()
    >  country state             city   ibgeID  deaths  totalCases
    0  Brazil    PA    Abaetetuba/PA  1500107       0           2
    1  Brazil    CE       Abaiara/CE  2300101       0           1
    2  Brazil    PE  Abreu e Lima/PE  2600054       0           1
    3  Brazil    AC    Acrelândia/AC  1200013       0           9
    4  Brazil    SP    Adamantina/SP  3500105       0           0

`Models <https://github.com/maricatovictor/covirus/tree/master/covirus/models>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SIR
'''

.. code:: python

    >>> from covirus.models.compartment import SIR
    >>> sir = SIR()
    >>> pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate = (
          1000,
          1,
          0,
          0.2,
          1 / 10, #1 recovered per 10 days
      )
    >>> sir.fit(pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate)
    >>> S, I, R = sir.predict(days=360)
    >>> sir.plot()
    >

| Outputs:
| |SIR-generated-2020-04-11|

Documentation
-------------

Unfortunely, we still do not provide a documentation page :(

References
----------

Data Sources
^^^^^^^^^^^^

Please for more specific data-sources info, `refer to
``data/`` <https://github.com/maricatovictor/covirus/tree/master/covirus/data>`__

Models
^^^^^^

-  `3778/COVID-19 <https://github.com/3778/COVID-19>`__
-  `SIR <https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/>`__

Other COVID-19 projects
-----------------------

Worldwide
^^^^^^^^^

-  `nCOV
   nextstrain <https://nextstrain.org/ncov/global?l=radial&s=Wuhan-Hu-1/2019>`__
   - Genomic & Bioinformatics analysis
-  `Ventilador <https://www.codetriage.com/jcl5m1/ventilator>`__ -
   Low-Cost Open-Source Ventilator-ish Device

Brazil
^^^^^^

-  `LOFT
   Report <https://docs.google.com/document/d/1c8U-eZSZQwr8m3KifQBndBOv0WlDDJ9aD0VPYATe3cg/edit>`__
   - LOFT analyses
-  `3778/COVID-19 <https://github.com/3778/COVID-19>`__ - Analyses

License
-------

`MIT <https://github.com/maricatovictor/covirus/blob/master/LICENSE>`__

.. |PyPI| image:: https://img.shields.io/pypi/v/covirus
.. |Build Status| image:: https://travis-ci.com/maricatovictor/covirus.svg?branch=master
   :target: https://travis-ci.com/maricatovictor/covirus
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |SIR-generated-2020-04-11| image:: https://user-images.githubusercontent.com/11489228/79053576-d13f5400-7c14-11ea-8dc6-b01fea6f3ada.jpg
