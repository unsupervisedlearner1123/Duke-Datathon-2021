# Duke Datathon 2021 💻💙 <img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">  
### Winning Submission  

## Insights from the Asian Barometer Survey: A Latent Factor Approach
This is the team repository for the Duke Annual Datathon, 2021. 

## The Asian Barometer Survey
Asian Barometer Survey (ABS) is a series of random surveys conducted across 18 Asian countries conducted by the National Taiwan University East Asia Democratic Studies department to gather data on political and socio-economic opinions of individuals from each country. These surveys have been through several rounds (or waves) over the past two decades and the data provided for the purpose of this analysis spans over two waves - the first wave from 2001 to 2003, and the second wave from 2005 to 2008. The ABS is aimed to gather public opinions, foster conversations between scholars, and share any insights with various organizations (Fu Hu Center, 2021). We aim to conduct cross-wave analyses and augment the ABS data by generating latent factors that can be used as meaningful research objectives. In order to do so, we statistically derive consolidated indicators to represent abstract individual characteristics like “faith in government” or “economic optimism”. We intend to uncover insights to suggest further deep-dives that scholars can leverage to answer specific questions, such as whether demographic variables are significant predictors of these factors. 

## Methodology
We utilize **Factor Analysis (FA)** to uncover latent constructs that manifest in the observed survey responses. The goal of this analysis is to not only find these constructs, but also estimate which survey items load onto which latent variables. This enables us to make sense of the bigger picture hidden in the data that has been quantified with several hundreds of measurable survey questions. The number of latent variables is determined by fitting a **Principal Component Analysis** and visually examining the scree plot. We find the optimal number of components to be around three for all countries in the study.
In order to help Asian Barometer with its goal of strengthening the intellectual and institutional capacity for research on democracy as well as generating reliable and comparable data, we want to find out how demographic variables are associated with the latent factors uncovered through the FA. If it was possible to predict which population subgroups are highly likely to hold extreme opinions or feel treated unequally, the Hu Fu Center could conduct more in-depth research about which circumstances foster these attitudes. To achieve this goal, we fit a **linear regression model** to regress the latent variables on demographic attributes, which are available without conducting costly surveys.

## Results
For most of the countries, the factor analysis is able to estimate interpretable factor loadings for at least one of the three latent dimensions. For the detailed assessment of the results a discussion of the predictive performance of the linear model which regresses the latent factors on demographic characteristics, see the full report file `40_docs/Report_final.pdf` or click [HERE](https://github.com/unsupervisedlearner1123/Duke-Datathon-2021/raw/main/40_docs/Report_final.pdf)  

This Analaysis was chosen as the winning entry to the Duke Datathon 2021 by the panel of judges comprised of Duke faculty.


## Team Members
| Name | Reference |
|----|----|
|Anna Dai | [GitHub Profile](https://github.com/dai-anna)|
|Deekshita Saikia |[GitHub Profile](https://github.com/unsupervisedlearner1123)|
|Moritz Wilksch | [GitHub Profile](https://github.com/moritzwilksch)|
|Satvik Kishore | [GitHub Profile](https://github.com/satvikk)|
