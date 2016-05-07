library(ggplot2)
library(gridExtra)
library(plyr)

data<-read.csv("D:\\rwork\\maxTwo\\communityTypePercent1-2-3(2016.2.24).csv",header = T) 
dt<-data
percent_dt<-ddply(dt,"community",transform,percent_count=count/sum(count)*100)
head(percent_dt)
#percent_dt$type<-factor(percent_dt$type,levels = c("Comprehensive","Engineering","Normal","Financial","Medical","Agriculture","Language","Law"))
percent_dt$type<-factor(percent_dt$type,levels = c("COM","ENG","NOR","FIN","MED","AGR","LAN","LAW"))

ppi<-300
png('phase123_community_type_Percent.jpeg',width=14*ppi,height=9.5*ppi,res=ppi)
xs <- split(percent_dt,f = dt$stage)
p<-ggplot(percent_dt,aes(x=reorder(community,communityOder),y=percent_count,fill=type))+
  geom_bar(stat="identity",colour="black",width=0.6)+
  ylab("Percent")+
  theme(
    legend.position=c(1.09,0.5),
    legend.title=element_blank(),
    legend.key.size=unit(0.73,'cm'),
    legend.text=element_text(colour="black",size=15,family="Times",face="italic"),
    plot.margin=unit(c(2,50,2,5),"mm"),
    panel.grid.major=element_blank(),
    panel.grid.minor=element_blank(),
    axis.text.x=element_text(colour="black",size=15,angle=0,,hjust=0.6,vjust=0.2),
    axis.text.y=element_text(colour="black",size=15),
    axis.title.x=element_text(colour="black",size=19,family="Times",face="italic"),
    axis.title.y=element_text(colour="black",size=19,family="Times",face="italic"),
    panel.background=element_rect(fill="white",colour="black",size=1)
  )+scale_fill_manual(values=c("#5555FF","#FF9555","#FFE00B","#AA55FF","#FFBFDF","#00D500","#55FFFF","#CCCCCC"))

p1<-p%+% xs$'a'+theme(axis.title.x=element_blank())
p2<-p %+% xs$'b'+theme(axis.title.x=element_blank())
p3<-p %+% xs$'c'+xlab("Group ID Number")

grid.arrange(p1,p2,p3,heights=c(5,5,5.5))
dev.off()



