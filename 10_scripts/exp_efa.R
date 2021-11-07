qs = c("q005","q006","q007","q008","q009","q010","q027","q028","q098","q105","q106","q121",
       "q123","q127","q128")

we = function(cn, v){
  sum(is.na(wv1_merge[country==cn,v,with=FALSE]))/sum(wv1_merge$country==cn)
}

missi = outer(unique(wv1_merge$country), qs, FUN = Vectorize(we))
colnames(missi) = qs
missi = missi*100
missi = round(missi, digits=2)
missi = data.frame(missi)
rownames(missi) = unique(wv1_merge$country)
for (var in names(missi)){
  attr(missi[[var]],"label") = attr(wv1_merge[[var]], 'label')
}

sapply(wv1_merge[,qs[qs!="q028"],with=F],function(z) sum(z>90,na.rm=T)/length(z))


cor(wv1_merge[,qs[qs!="q028"],with=F], use = "pa")

w1 = wv1_merge[,c(qs[qs!="q028"],"country","age",""),with=F]


w1 = arrow::read_parquet("20_intermediate_files/W1mergeddata.parquet") %>% as.data.table
w1 = w1[country=="Philippines"]
w1$q028 = NULL
w1$country = NULL
w1$yrsurvey = NULL
w1$agegroup = NULL
w1$maritalstatus = NULL
w1$educationyear = NULL
w1$income_quantile %<>% factor(ordered = T, levels = c("lowest quintile","2nd quintile", "3rd quintile", "4th quintile", "5th quintile"))
w1$q007 %<>% factor(ordered = T, 
                    levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
w1$q008 %<>% factor(ordered = T, 
                    levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
w1$q009 %<>% factor(ordered = T, 
                    levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
w1$q010 %<>% factor(ordered = T, 
                    levels = c("None at all","Not very much trust", "Quite a lot of trust", "A great deal of trust"))
w1$q006 %<>% factor(ordered = T, 
                    levels = c("Much Worse","A little Worse", "About the same", "A little Better", "Much Better"))
w1$q098 %<>% factor(ordered = T, 
                    levels = c("Not at all satisfied","Not very satisfied", "Fairly satisfied", "Very satisfied"))
w1$q128 %<>% factor(ordered = T, 
                    levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
w1$q005 %<>% factor(ordered = T, 
                    levels = c("Much worse now","A little worse now", "About the same", "A little better now","Much better now"))
w1$q105 %<>% factor(ordered = T, 
                    levels = c("Much worse","Somewhat worse", "Much the same", "Somewhat better","Much better than before"))
w1$q106 %<>% factor(ordered = T, 
                    levels = c("Much worse","Somewhat worse", "Much the same", "Somewhat better","Much better than before"))
w1$q121 %<>% factor(ordered = T, 
                    levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
w1$q127 %<>% factor(ordered = T, 
                    levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
w1$q123 %<>% factor(ordered = T, 
                    levels = c("Strongly disagree","Somewhat disagree", "Somewhat agree", "Strongly agree"))
w1$q027 %<>% factor(ordered = T, 
                    levels = c("No","Yes"))

pw1 = lapply(w1,as.numeric) %>% as.data.frame
pw1 = pw1[!is.na(rowSums(pw1)),]
p_out = prcomp(pw1[,qs[qs %ni% c("q028")]])


library(lavaan)
`%ni%` = function(x,y) !(x %in% y)
f4_formulation = "
efa('block1')*f1 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f2 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f3 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f4 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
"

f5_formulation = "
efa('block1')*f1 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f2 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f3 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f4 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
efa('block1')*f5 =~ q007 + q008 + q009 + q010 + q006 + q098 + q005 + q027 + q128 + q105 + q106 + q121 + q123 + q127
"

f5_model = lavaan(model = f5_formulation, data=w1, auto.var = TRUE, auto.efa = TRUE)









