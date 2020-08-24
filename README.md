# EveOut: Reproducible Event Dataset for Studying and Analyzing the Complex Event-Outlet Relationship

## Introduction

> We present a dataset of 77,545 news events collected between January 2019 and May 2020. We selected the top five news outlets based on Alexa Global Rankings and retrieved all the events reported in English by these outlets using the Event Registry API. Our dataset can be used as a resource to analyze and learn the relationship between events and their selection by the chosen outlets. It is primarily intended to be used by researchers studying bias in event selection. However, it may also be used to study the geographical, temporal, categorical and several other aspects of the events. We demonstrate the value of the resource in developing novel applications in the digital humanities with motivating use cases such as the Outlet Prediction task given the event details and analysis of event-selection bias.

### Due to the size of the dataset, it is hosted on Zenodo and is available at: https://zenodo.org/record/3953878

## Python Dependencies

To run the tool, Python 2.7+ must be downloaded.
The easiest way to download all necessary Python packages is using pip. To do so, navigate to the project root directory and run:
```
pip install -r requirements.txt
```

## Dataset Generation 

> Download glove.6B.300d.txt file and place it in the data/external/glove folder.

```
python3 main.py
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



