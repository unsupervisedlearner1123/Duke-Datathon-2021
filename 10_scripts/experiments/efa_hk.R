library(arrow)
library(data.table)
library(magrittr)
library(lavaan)

hk = arrow::read_parquet("20_intermediate_files/W1_countries/Hong Kong.parquet") %>% as.data.table
hk$country = NULL
hk$`__index_level_0__` = NULL

origna = sum(is.na(hk))
orignas = sapply(hk, function(z) sum(is.na(z)))

hk$q001 %<>% factor(ordered = T, levels  = c("Very Bad","Bad","So so","Good","Very Good"))
hk$q002 %<>% factor(ordered = T, levels  = c("Much Worse","A little Worse","About the same","A little Better","Much Better"))
hk$q003 %<>% factor(ordered = T, levels  = c("Much Worse","A little Worse","About the same","A little Better","Much Better"))
hk$q004 %<>% factor(ordered = T, levels  = c("Very Bad","Bad","So so","Good","Very Good"))
hk$q005 %<>% factor(ordered = T, levels  = c("Much worse now","A little worse now","About the same","A little better now","Much better now"))
hk$q006 %<>% factor(ordered = T, levels  = c("Much Worse","A little Worse","About the same","A little Better","Much Better"))
hk$q007 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q008 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q009 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q010 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q011 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q014 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q016 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
hk$q024 %<>% factor(ordered = T, levels = c("One can't be too careful in dealing with them","Both","Most people can be trusted"))
hk$q024 %<>% factor(ordered = T, levels = c("One can't be too careful in dealing with them","Both","Most people can be trusted"))
hk$q027 %<>% factor(ordered = T, levels = c("No","Yes"))
hk$q029 %<>% factor(ordered = T, levels = c("No","Yes"))
hk$q030 %<>% factor(ordered = T, levels = c("No","Yes"))
hk$q056 %<>% factor(ordered = T, levels = c("Not at all interested","Not very interested","Somewhat interested","Very interested"))
hk$q061 %<>% factor(ordered = T, levels = c("No impact at all","A little impact","Quite some impact","A great deal of impact"))
hk$q064 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q066 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q068 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q069 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q074 %<>% factor(ordered = T, levels = c("Never done","Once","More than once"))
hk$q075 %<>% factor(ordered = T, levels = c("Never done","Once","More than once"))
hk$q076 %<>% factor(ordered = T, levels = c("Never done","Once","More than once"))
hk$q098 %<>% factor(ordered = T, levels = c("Not at all satisfied","Not very satisfied", "Fairly satisfied", "Very satisfied"))
hk$q104 %<>% factor(ordered = T, levels = c("Veryl dissatisfied","Somewhat dissatisfied","Half and Half", "Somewhat satisfied", "Very satisfied"))
hk$q113 %<>% factor(ordered = T, levels = c("Much worse","Somewhat worse", "Much the same", "Somewhat better","Much better than before"))
hk$q114 %<>% factor(ordered = T, levels = c("Almost everyone is corrupt","Most officials are corrupt", "Not a lot of officials are corrupt", "Hardly anyone is involved"))
hk$q116 %<>% factor(ordered = T, levels = c("No","Yes"))
hk$q119 %<>% factor(ordered = T, levels = c("Democracy is definitely more important","Democracy is somewhat more important","They are both equally importment","Economic development is somewhat more important","Economic development is definitely more important"))
hk$q121 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q123 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q125 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q126 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q127 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q130 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q131 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q132 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q133 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q134 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q135 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q136 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q137 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q138 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q139 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q140 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q142 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q143 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
hk$q145 %<>% factor(ordered = T, levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
finna = sum(is.na(hk))
finnas = sapply(hk, function(z) sum(is.na(z)))
hk$q062 = NULL

f3_formulation = 


ph = arrow::read_parquet("20_intermediate_files/W1_countries/Philippines.parquet") %>% as.data.table
ph$country = NULL

ph$q013 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
ph$q017 %<>% factor(ordered = T, levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
ph$q057 %<>% factor(ordered = T, levels = c("Practically never","Not even once a week","Once or twice a week","Several times a week","Everyday"))
ph$q077 %<>% factor(ordered = T, levels = c("Never done","Once","More than once"))
ph$q115 %<>% factor(ordered = T, levels = c("Almost everyone is corrupt","Most officials are corrupt", "Not a lot of officials are corrupt", "Hardly anyone is involved"))












