#8481 * 4 (start,end,speaker,number) = 33924
#86443 - 33924 = 52519
#9274 coefficents, 52519 words
#9274/52519 = 0.1766 tokens to words

#twotokenratio
#human = 0.3908, program = 0.6092

library(ggplot2)

tokens <- read.csv("twotokentext.csv")

coef <- read.csv("coef.csv")

bottwenty <- coef[9254:9274,]
toptwenty <- coef[1:20,]

wplot <- ggplot(taxe) + aes(Year, tax, color=Bracket)
wplot <- tplot + geom_path()
wplot <- tplot + geom_abline(intercept = 0.0, slope =0)
wplot <- tplot + xlab("Year") + ylab("Individual Income Tax Rate") + ggtitle("Enjoy Your Taxes, Truffle Nibblers")
