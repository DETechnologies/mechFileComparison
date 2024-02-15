## extract yaml file data
import pandas as pd

#preamble
RXNS=['H+O2=O+OH','O+H2=H+OH','OH+H2=H+H2O','O+H2O=OH+OH','H2+M=H+H+M','O2+M=O+O+M','OH+M=O+H+M','H2O+M=H+OH+M','H+O2(+M)=HO2(+M)','HO2+H=H2+O2','HO2+H=OH+OH','HO2+O=OH+O2','HO2+OH=H2O+O2','H2O2+O2=HO2+HO2','H2O2+O2=HO2+HO2','H2O2(+M)=OH+OH(+M)','H2O2+H=H2O+OH','H2O2+H=H2+HO2','H2O2+O=OH+HO2','H2O2+OH=H2O+HO2H2O2+OH=H2O+HO2']
yamls=["Burke2012.yaml","Hong2011.yaml","sandiego20161214_H2only.yaml","sandiego20161214.yaml"]

main=pd.DataFrame(columns=["RXN","A","b","Ea","YamlSource"])

for yam in yamls: 
    f=open(yam,'r')
    d=f.read()
    data=d.replace(" ","").replace("<=>","=")
    for rx in RXNS: 
        if data.find(rx) != -1: 
            index=data.index(rx)
            rc_ind=data.index("rate-constant:{",index)+15
            next_eq=data.index("}",rc_ind)
            coeffs=data[rc_ind:next_eq]
            A=coeffs[(coeffs.index("A:")+2):(coeffs.index(","))]
            b=coeffs[(coeffs.index("b:")+2):(coeffs.index(",",(coeffs.index("b:")+2)))]
            Ea=coeffs[(coeffs.index("Ea:")+3):len(coeffs)]
            main.loc[main.shape[0],:]=[rx,A,b,Ea,yam]          
    f.close()
    
    main.to_csv("mechfile_comparison.csv")   