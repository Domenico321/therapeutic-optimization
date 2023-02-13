# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:31:30 2022

@author: Utente
"""
# This code calculates the attractors of the network in which the genes 
# VIM, HSP90AB1, TK1, CSNK2B, YWHAB have been constantly silenced (set to zero).
# Use the data from the excel file "Supplementary Table S2" sheet "Attractor_1"
# The use of python version 2.7 is recommended.

import boolean2 as b2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab
import pandas as pd


list=[]
while True:
    try:
        #insert name and extension file excel with binary values
        Table=raw_input("Please enter the excel file name: ")
                
        #get a dataframe from the excel sheet
        df=pd.read_excel(Table)
        
        try:
            #indicate the cell in which to look for attractors
            cellname=raw_input("Please enter the cell name: ")
            
            #tranforms the values of the columns to be processed from "1" and"0"
            #to "True" and "False"
            df['TF']=df[cellname].apply(lambda x : 'True' if x == 1 else 'False')
        except IOError:
            print("The cell name is incorrect")
            
    except IOError:
         print("The file name is incorrect")
         continue
    break

#create a new dataframe with only two columns,the name of the genes and 
#their Boolean value "True" or "False"
mod_df=df[['gene_name','TF']]

#create a list with values in columns of the dataframe "mod_df"
#interspersed with the symbol "="
for i in mod_df.index:
    list.append(mod_df["gene_name"][i] + " = " + mod_df["TF"][i]+"\n")

#tranformation of the list format into a string required for processing
model_definition1='  '.join(list)


#print(model_definition1)
    



# Update rule  
model_definition2= '''
TRIB3* = not TP53
PLAU* = (TP53 or NFKB1 or HIF1A or ATF2 or ETS1 or PLAUR or ST14 or RELA) and not HDAC1
IFI16* = TP53
BTG3* = TP53
LAPTM5* = TP53
ST14* = (TP53 or PPARD or STAT1 or ST14) and not RELA
EPHA2* = (TP53 or AKT2 or ETS1 or CREB1) and not(MTA1 or RELA)
PML* = (TP53 or IRF9 or STAT5A or STAT1 or RB1 or STAT3) and not CSNK2B
STAT5A* = (ERK1 or HSP90AB1 or RELA ) and not(UBE2D1)
CD82* = TP53 or HIF1A
TP53* = TP53
PLK2* = TP53
CTSD* = TP53 or CTSD
KRT15* = TP53
DDR1* = TP53 or E2F1 or DDR1 or TM4SF1
SERPINA3* = TP53 or NFKB1 or STAT3 or STAT1 or RELA
EZH2* = (E2F1 or STAT3 or REL or HSP90AB1 or STAT5A or SAT1) and not(TP53 or RB1)
RELA* = CSNK2B and (E2F1 or ATF2 or BRCA1 or PARP1 or EZH2 or ARRB1 or AKT2 or HIF1A or CREB1 or FOS) and (not TP53) and  (not STAT1 or not PML or not SQSTM1 or not TRIB3 or not HDAC1 or not DAXX) 
ETS1* = (FOS or HIF1A or ARNT) and not(TP53 or RB1 or RELA or DAXX)
MCM7* = (E2F1 or CCND1) and not(TP53 or RB1)
ACTB* = (HSP90AB1 or SYNPO) and not TP53
VIM* = VIM
MTA1* = RELA and not(TP53 or PARP1)
ITGB4* = (NFKB1 or ERBB2 or AKT2) and not(TP53 or HDAC1)
CAV1* = (STAT3 or ETS1 or EGFR or ARNT or PLAUR or CD82 or RELA) and not(TP53 or SQSTM1)
SETDB1* = AKT2 and not TP53
KRT17* = (FOS or STAT1) and not(TP53 or BRCA1 or EZH2)
HSP90AB1* = HSP90AB1
CCND1* = (CREB1 or NFKB1 or E2F1 or FOS or ATF2 or STAT1 or PARP1 or REL or EZH2 or ETS1 or STAT5A or MTA1 or EGFR or RELA) and not(HDAC1 or TP53 or PML or CAV1 or PSMD4 or HINT1 or TNRC6A or HIF1A or NR3C1)
E2F1* = (CREB1 or E2F1 or ARRB1 or BIRC2) and not(TP53 or HDAC1 or PARP1 or IFI16 or BTG3 or RELA or NFKB1 or HDAC1 or SETDB1 or RB1 or E2F4)
BCL2L1* = (CREB1 or NFKB1 or STAT3 or FOS or HIF1A or ATF2 or STAT1 or REL or ETS1 or STAT5A or NFE2L2 or GABP or RELA or AR) and not(TP53 or HDAC1 or ERBB2 or BCL2L1 or BAD or BCL2 or BCL2L11 or PMAIP1)
BRCA1* = (CREB1 or PARP1 or NFE2L2 or AKT2 or GABP or ERK1) and (not TP53 or not HDAC1 or not RB1 or not MTA1 or not PML)
HIF1A* = (CREB1 or NFKB1 or STAT3 or REL or HSP90AB1 or ARRB1 or MTA1 or ARNT or RELA or ATF2 or E2F1 or HIF1A or PARP1 or HDAC1 or SAT1 or BCL2) and (not TP53) and (not PSMD4 or not MCM7 or not SQSTM1 or not STAT1)
PLAUR* = (NFKB1 or FOS or HIF1A or ATF2 or PLAU or RELA or CAV1) and not(TP53 or HDAC1)
STAT1* = (CREB1 or BRCA1 or SETDB1 or RXRA or TRADD) and not(ARRB1 or PML or HDAC1)
STAT3* = (CREB1 or STAT3 or FOS or ATF2 or EZH2 or MTA1 or HIF1A or NFKB1 or SETDB1 or CD44 or RELA) and (not RB1 or not PML or not CAV1 or not CCND1 or not DAXX or not P21)
TGFB1* = (CREB1 or NFKB1 or STAT3 or HIF1A or FOS or ATF2 or PPARD or RELA or REL or AR) and not(HSP90AB1 or NFE2L2)
RB1* = (CREB1 or E2F1 or ATF2 or BRCA1 or GABP or PML) and not(HDAC1 or BCL6)
FOS* = (CREB1 or E2F1 or STAT3 or FOS or ATF2 or STAT1 or PARP1 or STAT5A or NFE2L2 or IKBKG) and not HDAC1 
CREB1* = (CREB1 or ARRB1 or AKT2) and not DAXX
PLAT* = CREB1 or ATF2 or RELA or FOS 
SQSTM1* = NFKB1 or RELA or NFE2L2 or FOS 
REL* = HIF1A and not NFKB1
NFKB1* =  RELA and (FOS or BRCA1 or PARP1 or PSMD4 or HIF1A or ETS1) and (not E2F1 or not HDAC1 or not ARRB1)
CD44* = (FOS or NFKB1 or ETS1 or RELA) and not E2F1
TK1* = TK1
PARP1* = ETS1 and not(AKT2 or PARP1 or HDAC1 or CASP3 or CASP9)
SOD1* = (NFE2L2 or RELA) and not(HDAC1 or CAV1 or PSMD4)
HDAC1* = RELA and (STAT3 or CSNK2B or EZH2 or RB1 or STAT5A or MTA1 or CCND1 or DAXX) 
LDHB* = STAT3 or PPARD
CSNK2B* = CSNK2B
KRT5* = FOS and not BRCA1
TGFBR2* = FOS or TGFB1
ARNT* = (HIF1A or RELA or BRCA1) and not STAT5A
YWHAB* = YWHAB 
ARAF* = CSNK2B
NFE2L2* = (CSNK2B or BRCA1 or NFE2L2 or AKT2) and not(EZH2 or PML or CAV1 or RELA)
S100A10* = STAT1
PSMD4* = PARP1
HMGCR* = PARP1
AKT2* = (ARRB1 or HSP90AB1 or CAV1) and not(BRCA1 or EZH2 or TRIB3)
TNRC6A* = HSP90AB1
ERBB2* = HSP90AB1 or EGFR or HSPB1 or ITGB4 or ETV1
IKBKG* = (HSP90AB1 or ANXA1 or MAP3K7 or SQSTM1 or BIRC2) and not (CASP8 or CASP6)
ATF2* = RB1 or BRCA1
PPARD* = not HSP90AB1 and not RELA
SLC3A2* = NFE2L2 or RELA
UBQLN1* = GABP
SYNPO* = YWHAB
BAX* =   (BCL2L11 or BID or BAK) and not (BCL2L1 or BCL2 or MCL1)
EGFR* = EGFR or ERBB2
ETV1* = ERBB2
MAP3K7* = MAP3K7 or TGFBR1
TGFBR1* = (TGFB1 or TGFBR2 or YWHAB) and not CAV1
SMAD4* = not MAP3K7
MAP3K4* = GADD45B
INSR* = PPARG
A2M* = PPARG
PAX6* = PPARG
CYP3A4* = NR3C1
NEDD9* = NR3C1
GADD45B* = REL or TP53 or E2F1 or MYC
PPARG* = (NCOA4 or AKT2) and not SMAD3
NR3C1* = AR and not DAXX
SMAD3* = PPARG
AR* = not (DAXX or CASP8)
CASP9* = (APAF1 or CASP3) and not (AKT2 or BIRC5 or BCL2L1 or XIAP or BIRC2)
APAF1* = CYC and not CASP3
BAD* = BCL2 and not (YWHAB or BCL2L1)
BCL2* = (BRCA1 or TP53) and ( not BAD or not TP53 or not BCL2L11 or not PMAIP1)
BID* = (CASP3 or TP53 or CASP9 or CASP10 or STAT1 or CASP8) and not HIF1A
MCL1* = (HIF1A or CAV1) and not (BCL2L11 or PMAIP1 )
CASP8* = (BCL2 or RXRA or FADD or CASP3 or STAT1 or CASP10 or SQSTM1) and not BIRC2
BAK* = (BCL2 or BCL2L11 or TP53 or BAX or MCL1) and not (BCL2A1)
BCL2L11* =  not (BCL2 or YWHAB)
BCL2A1* = not BCL2L11
CASP2* = CASP8 or STAT1
XIAP* = (STAT5A or AKT2) and not (TP53)
CASP3* = (CASP9 or CASP6 or CASP8 or CASP10) and (not XIAP or not P21) and (not BIRC2)
DAXX* = TGFBR2 and not HSPB1
FADD* = CASP8 or TRADD
CASP6* = (CASP3 or CASP7 or CASP10) and not XIAP
CASP7* = (CASP6 or CASP9 or CASP10) and not (XIAP or BIRC2)
BIRC2* = HIF1A and not CASP8
CASP10* = CASP8 or FADD or CASP6 or CASP3 
CYC* = PARP1
DIABLO* = not (XIAP or BIRC2)
BIRC5* = not (XIAP or DIABLO)
PMAIP1* = not (BCL2 or MCL1)
MAP3K5* = DAXX and not ARRB1
P21* = not TK1
ERK1* = VIM




'''
#union of the two defined strings
model_definition = model_definition1 + model_definition2

#Refers to the text containing in the model definition and the model update
model = b2.Model(text=model_definition, mode='sync')
model.initialize()
#Number of iteration
model.iterate(steps=20)



#p1 = pylab.plot( model.data["HDAC1"] , 'ob-')
#pylab.legend([p1], ["HDAC1"])

#pylab.show()  



for node in model.data:
    print node, model.data[node]
#Cheking for fixed states
model.report_cycles()

#Save the result
model.save_states('attractor_1.xls')