mydata = read.csv("st_data.csv")

mid = mydata$midterm

print(range(mid))
print(as.integer(mean(mid)))
print(as.integer(var(mid)))
print(as.integer(sd(mid)))

breaks = seq(0, 100, by=10)
mid.cut = cut(mid, breaks, right=FALSE)
mid.freq = table(mid.cut)
print(cbind(mid.freq))

bmp(file="aa.bmp")
hist(mid, right=FALSE, main="Frequency", xlab="Midterm Exam", ylab="Count", col = NULL)
aa <- dev.off()

bmp(file="bb.bmp")
fin = mydata$final
plot(mid, fin, main="Scatter", xlab="Midterm Exam", ylab="Final Exam")
bb <- dev.off()