import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import xlrd
from PIL import Image

def main():
    col1,col2=st.beta_columns([1,2])
    with col1:
        img = Image.open("rig.jpeg")
        st.image(img, width=200)
    with col2:
        st.title("Porosity calculation Using Neutron-Density Crossplot")
    xlrd.xlsx.ensure_elementtree_imported(False,None)
    xlrd.xlsx.Element_has_iter=True
    df=pd.read_excel(r"CNL_1pt1.xlsx")
    X=df.iloc[:,:2]
    Y=df["PHIT_ND"]
    knn1=KNeighborsRegressor(n_neighbors=3)
    knn1.fit(X,Y)
    st.subheader("Select the type of your file:")
    s=st.radio("",('CSV','Excel'))
    st.subheader("NOTE: Data file should contain the following columns shown for your guidance!!")
    sample=pd.read_excel(r"Sample_data.xlsx")
    st.write(sample)
    if s=='Excel':
        file=st.file_uploader("Upload the file here: ")
        if(st.button("Calculate")):
            df_test=pd.read_excel(file)
            depth=df_test.iloc[:,0]
            x=df_test.iloc[:,1:3]
            y=knn1.predict(x)
            fig, ax = plt.subplots()
            plt.plot(y,depth,label='Porosity')
            plt.scatter(y,depth,label='Porosity')
            plt.legend()
            plt.xlabel("Porosity")
            plt.ylabel("Depth")
            st.pyplot(fig)
            d=pd.DataFrame({"Depth":depth,"Porosity":y})
            st.write(d)
    elif s=="CSV":
        file=st.file_uploader("Upload the file here: ")
        if(st.button("Calculate")):
            df_test=pd.read_csv(file)
            depth=df_test.iloc[:,0]
            x=df_test.iloc[:,1:3]
            y=knn1.predict(x)
            fig, ax = plt.subplots()
            plt.plot(y,depth,label='Porosity')
            plt.scatter(y,depth,label='Porosity')
            plt.legend()
            plt.xlabel("Porosity")
            plt.ylabel("Depth")
            st.pyplot(fig)
            d=pd.DataFrame({"Depth":depth,"Porosity":y})
            st.write(d)       
if __name__ == '__main__':
    main()
