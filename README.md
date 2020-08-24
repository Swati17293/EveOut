# EveOut: Reproducible Event Dataset for Studying and Analyzing the Complex Event-Outlet Relationship

## Introduction

> We present a dataset of 77,545 news events collected between January 2019 and May 2020. We selected the top five news outlets based on Alexa Global Rankings and retrieved all the events reported in English by these outlets using the Event Registry API. Our dataset can be used as a resource to analyze and learn the relationship between events and their selection by the chosen outlets. It is primarily intended to be used by researchers studying bias in event selection. However, it may also be used to study the geographical, temporal, categorical and several other aspects of the events. We demonstrate the value of the resource in developing novel applications in the digital humanities with motivating use cases such as the Outlet Prediction task given the event details and analysis of event-selection bias.

### Due to the size of the dataset, it is hosted on Zenodo and is available at: https://zenodo.org/record/3953878

## Python Dependencies

> To run the tool, Python 2.7+ must be downloaded.
The easiest way to download all necessary Python packages is using pip. To do so, navigate to the project root directory and run:
```
pip install -r requirements.txt
```

## Dataset Generation

> To replicated the reported dataset run:
```
python3 main.py eventRegistry_apiKey
```

> To generate custom dataset, pass the values as the commandline arguments:

--category (<Optional> set one or more category, default=['news/Business', 'news/Politics', 'news/Technology','news/Environment', 'news/Health', 'news/Science','news/Sports', 'news/Arts_and_Entertainment'])
--source (<Optional> set one or more news source, default=['nytimes.com', 'indiatimes.com', 'washingtonpost.com', 'usatoday.com', 'chinadaily.com.cn'])
--date_start (<Optional> set event start date, default='2019-01-01')
--date_end (<Optional> set event end date, default='2020-05-31')
--lang (<Optional> set language, default='eng')

> For example, to retrieve events in the 'Business' category in the 'Slovene' language reported by 'Delo' run:
```
python3 main.py eventRegistry_apiKey --lang slv --category news/Business --source delo.si
```
    
## License
> MIT License

## Citation
> If this data set is used in publication, please cite:
```
@dataset{swati_2020_3953878,
  author       = {Swati and
                  Tomaž Erjavec and
                  Dunja Mladenić},
  title        = {{EveOut: Reproducible Event Dataset for Studying 
                   and Analyzing the Complex Event-Outlet
                   Relationship}},
  month        = aug,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {version 1.0.0},
  doi          = {10.5281/zenodo.3953878},
  url          = {https://doi.org/10.5281/zenodo.3953878}
}
```



