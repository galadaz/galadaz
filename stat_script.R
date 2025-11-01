---
  title: "r_stat_popytka1"
author: "Adelia"
output: html_document
---
  ```{r}
library("lmtest")
library("stats")
library("readxl")
library("scales")
library("vars")
library("moments")
library("pastecs")
library("car")
library("psych")
library("Hmisc")
library("gclus")
library("nortest")
library("foreign")

APS <- read_excel("C:/Users/evere/Desktop/STUDYSTAT/stat_test_in_process.xlsx")

#```{r}
# Дескриптивный анализ данных

APS$TypeOfTravel <- as.factor(APS$TypeOfTravel)
APS$Class <- as.factor(APS$Class)
APS$Satisfaction <- as.factor(APS$Satisfaction)
is.factor(APS$TypeOfTravel)
is.factor(APS$Class)
is.factor(APS$Satisfaction)

# Описательная статистика для всех переменных
summary(APS[1:9])

#Круговые диаграммы для качественных переменных
tab <- table(APS$TypeOfTravel)
perc <- tab/sum(tab) * 100 
colors1 <- c('thistle2', 'plum2')
labs1 = c("Деловые поездки", "Личные поездки")
pie(perc, col = colors1, main = "Цель полёта", labels = labs1)

tab <- table(APS$Class)
perc <- tab/sum(tab) * 100 
colors2 <- c('thistle2', 'plum2', 'palevioletred')
labs2 = c("Бизнес", "Эконом Плюс", "Эконом")
pie(perc, col = colors2, main = "Класс полёта ", labels = labs2)

tab <- table(APS$Satisfaction)
perc <- tab/sum(tab) * 100 
labs2 = c("Удовлетворен", "Нейтрально или недоволен")
pie(perc, col = colors1, main = "Уровень удовлетворенности авиакомпании", labels = labs2)

# Описательная статистика для переменной FlightDistance
summary(APS$FlightDistance)
range(APS$FlightDistance)
describe(APS$FlightDistance)
#Квантили с уровнями кратными 10
quantile(APS$FlightDistance, seq(from=0, to=1, by=0.1))
#кратными 0.5
quantile(APS$FlightDistance, seq(from=0, to=0.1, by=0.005))
#кратными 5
quantile(APS$FlightDistance, seq(from=0.5, to=1, by=0.05))
#кратными 25
quantile(APS$FlightDistance, seq(from=0, to=1, by=0.25))


# Дисперсия
var(APS$FlightDistance)
# Стандартное отклонение
sd(APS$FlightDistance)
# Стандрартная ошибка средней
sd(APS$FlightDistance)/sqrt(length(APS$FlightDistance))
# Интерквартильный интервал
IQR(APS$FlightDistance)
# Коэффициенты асимметрии и эксцесса
kurtosis(APS$FlightDistance, na.rm = TRUE)
skewness(APS$FlightDistance, na.rm = TRUE)
#Критерий Жака-Бера
jarque.test(APS$FlightDistance)

#done

#Гистограмма и график плотности нормального распределения
hist(APS$FlightDistance, breaks = 10, freq = FALSE, col = "darkslategray3", main = "Дистанция", xlab = "расстояние", ylab = "частоты")
curve(dnorm(x, mean = mean(APS$FlightDistance), sd = sd(APS$FlightDistance)), add = TRUE, col = "darkslategrey", lwd = 2)


#Ящик с усами
boxplot(APS$FlightDistance, col = "pink", border = "sienna2")

```

