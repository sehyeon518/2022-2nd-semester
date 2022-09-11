mydata = read.csv("st_data.csv")
print(nrow(mydata))
print(ncol(mydata))

finaldata = mydata[mydata$final == 50,]
print(finaldata)
print(finaldata[c('ID', 'final', 'midterm')])