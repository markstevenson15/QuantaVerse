#!/usr/bin/python

from datetime import date
import pandas as pd
import sys

interval = int(float(sys.argv[2]))
chunk = int(float(sys.argv[1]))

class AML:
    def __init__(self, ident):
        self.ident = ident
          
    def evaluate_criteria2(self, rdate,sdate,ramt,samt):
        
        fname = "bridging_"+str(chunk)+"_"+".txt"
        with open(fname, "a") as f:
            if ((rdate-sdate).days) >=0 and ((rdate-sdate).days) < 8 and ramt/samt <.80 and ramt/samt >.60 :
                
                output = self.ident+","+str(sdate)+","+str(samt)+","+str(rdate)+","+str(ramt)
                f.write(output+'\n')
                #return(output)
                             
    def find_bridge(self):
        
        sender_list = original_dat[original_dat['SENDER'] == self.ident]
        receiver_list = original_dat[original_dat['RECEIVER'] == self.ident]
        sender_date = [sender_list.iloc[i,1] for i in range(0,sender_list.shape[0])]
        sender_amt = [sender_list.iloc[i,2] for i in range(0,sender_list.shape[0])]
        receiver_date = [receiver_list.iloc[j,1] for j in range(0,receiver_list.shape[0])]
        receiver_amt = [receiver_list.iloc[j,2] for j in range(0,receiver_list.shape[0])]
        
        [self.evaluate_criteria2(receiver_date[j],sender_date[i],receiver_amt[j],sender_amt[i]) for i in range(0,sender_list.shape[0]) for j in range(receiver_list.shape[0])]
           
if __name__ == "__main__":
    
    original_dat = pd.read_csv('./transactions.csv',sep = '|',header = 0, skiprows = (chunk-interval),nrows = chunk)
    original_dat.columns =['TRANSACTION', 'TIMESTAMP', 'AMOUNT', 'SENDER','RECEIVER']
    original_dat['TIMESTAMP'] = pd.to_datetime(original_dat['TIMESTAMP'], format='%Y-%m-%d', errors='coerce')
       
    senders = original_dat.SENDER
    receivers = original_dat.RECEIVER
    bridges = list(set(senders) & set(receivers))
    [AML(bridges[i]).find_bridge() for i in range(0,len(bridges))]