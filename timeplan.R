
timeplan <- function(inputmonth){


fullmonth = months(as.POSIXct(paste(inputmonth, "01", sep = "-")))

output <- character(0)
i=1
while(i<31){
  date = as.Date(paste(inputmonth, i, sep = "-"))
  readabledate = paste(inputmonth, i, sep = "-")
  line = paste(readabledate," ","which is a ",weekdays(date), "in", fullmonth, "\n")
  output=c(output, line)
  i=i+1

}
return(paste(output, collapse = ""))
}