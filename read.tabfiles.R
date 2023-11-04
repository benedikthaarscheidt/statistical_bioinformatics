read.tabfiles<-function(dir){
 x=1
 #this initializes an empty data frame
 data.all = NULL
 files = list.files(dir,full.names = FALSE)
 for(file in files){
   data=read.table(file,sep=";")   
   if (is.null(data.all)){
     data.all=data
   } else {
     data.all=rbind(data.all,data)
   }
   x=x+1   
 }
 return(dim(data.all))
 return(data.all)
}
   
  
  
  
  
  
  
}