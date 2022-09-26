mydata = read.csv("st_data.csv")

myrange = range(mydata$midterm)
mymean = mean(mydata$midterm)
myvar = var(mydata$midterm)
mysd = sd(mydata$midterm)
print(myrange)
print(as.integer(mymean))
print(as.integer(myvar))
print(as.integer(mysd))

mid = mydata$midterm
breaks = seq(0, 100, by=10)
mid.cut = cut(mid, breaks, right=FALSE)
mid.freq = table(mid.cut)
print(cbind(mid.freq))

bmp(file="aa.bmp")
hist(mid, right=FALSE, main="Frequency", xlab="Midterm Exam", ylab="Count")
dev.off()

bmp(file="bb.bmp")
fin = mydata$final
plot(mid, fin, main="Scatter", xlab="Midterm Exam", ylab="Final Exam")
dev.off()