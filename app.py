import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

files = './data/clients.xls'
rd = pd.read_excel(files)
dtf = pd.DataFrame(rd)

class Front:
    def __init__(self):
        self.build()
    def build(self):
        
        col1,col2 = st.columns(spec=[1,2])
        with col1:
            entry = st.text_input(label='Search',label_visibility='collapsed',placeholder='Search by Client ID')
        with col2:
            if st.button(label='Search',use_container_width=True):
                try:
                    if entry != '':
                        ids = dtf['Client ID']
                        client = dtf[int(entry)==ids]
            
                        st.markdown(
        body=f"""
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">
        </head>
        """,
        unsafe_allow_html=True
    )
                        st.markdown(
                                body=f"""
                                <div
                                style="
                                background-color:#f0f2f6;
                                height:275px;
                                width:100%;
                                border-radius:5px;
                                padding:10px 10px 0px 10px;
                                "
                                >
                                <div style="
                                display:flex;
                                justify-content:space-between;
                                ">
                                <div style="
                                height:45px;
                                width:45px;
                                border-radius:5px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                color: red;
                                font-size: 16px;
                                cursor: pointer;
                                background-color:#ffb3b3;
                                color:#ff4b4b;
                                size:25px;
                                " class="fa-solid fa-user">  
                                </div>
                                    <div style="
                                    height:100px;
                                    width:210px;
                                    border-radius:5px;
                                    color: red;
                                    cursor: pointer;
                                    color:#31333f;
                                    position: relative;
                                    bottom:5px;
                                    left:10px;
                                    "
                                    >
                                    <div style="
                                    font-size:16px;
                                    text-transform: uppercase;
                                    font-weight: bold;
                                    margin-bottom:0px;
                                    ">
                                    {client.iloc[0]['Client Name']}
                                    </div>
                                    <div style="
                                    position: relative;
                                    left:0px;
                                    text-transform: capitalize;
                                    "
                                    >
                                    {client.iloc[0]['Village']}
                                    </div>
                                    </div>
                                </div>
                                <div style="
                                display:flex;
                                justify-content:space-between;
                                position:relative;
                                bottom:30px
                                ">
                                <div style="
                                height:45px;
                                width:45px;
                                border-radius:5px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                color: red;
                                font-size: 16px;
                                cursor: pointer;
                                background-color:#ffb3b3;
                                color:#ff4b4b;
                                size:25px;
                                " class="fa-solid fa-venus-mars">  
                                </div>
                                    <div style="
                                    height:100px;
                                    width:210px;
                                    border-radius:5px;
                                    color: red;
                                    cursor: pointer;
                                    color:#31333f;
                                    position: relative;
                                    bottom:5px;
                                    left:5px;
                                    "
                                    >
                                    <div style="
                                    text-transform: uppercase;
                                    font-weight: bold;
                                    margin-bottom:0px;
                                    ">
                                    {client.iloc[0]['Spouse']}
                                    </div>
                                    <div style="
                                    position: relative;
                                    bottom:5px;
                                    left:5px;
                                    text-transform: capitalize;
                                    "
                                    >
                                    Father / Husband / Son 
                                    </div>
                                    </div>
                                </div>
                                <div style="
                                display:flex;
                                justify-content:space-between;
                                position:relative;
                                bottom:60px
                                ">
                                <div style="
                                height:45px;
                                width:45px;
                                border-radius:5px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                color: red;
                                font-size: 16px;
                                cursor: pointer;
                                background-color:#ffb3b3;
                                color:#ff4b4b;
                                size:25px;
                                " class="fa-solid fa-phone">  
                                </div>
                                    <div style="
                                    height:100px;
                                    width:210px;
                                    border-radius:5px;
                                    color: red;
                                    cursor: pointer;
                                    color:#31333f;
                                    position: relative;
                                    bottom:5px;
                                    left:5px;
                                    "
                                    >
                                    <div style="
                                    font-size:16px;
                                    text-transform: uppercase;
                                    font-weight: bold;
                                    margin-bottom:0px;
                                    ">
                                    Phone number
                                    </div>
                                    <div style="
                                    position: relative;
                                    left:5px;
                                    text-transform: capitalize;
                                    "
                                    >
                                    {client.iloc[0]['Contact ']}
                                    </div>
                                    </div>
                                </div>
                                <div style="
                                display:flex;
                                justify-content:space-between;
                                position:relative;
                                bottom:90px
                                ">
                                <div style="
                                height:45px;
                                width:45px;
                                border-radius:5px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                color: red;
                                cursor: pointer;
                                background-color:#ffb3b3;
                                color:#ff4b4b;
                                size:25px;
                                " class="fa-solid fa-address-book">  
                                </div>
                                    <div style="
                                    height:100px;
                                    width:210px;
                                    border-radius:5px;
                                    color: red;
                                    cursor: pointer;
                                    color:#31333f;
                                    position: relative;
                                    bottom:5px;
                                    left:5px;
                                    "
                                    >
                                    <div style="
                                    font-size:16px;
                                    text-transform: uppercase;
                                    font-weight: bold;
                                    margin-bottom:0px;
                                    ">
                                    Credit Officer
                                    </div>
                                    <div style="
                                    position: relative;
                                    bottom:5px;
                                    left:5px;
                                    text-transform: capitalize;
                                    "
                                    >
                                    {client.iloc[0]['CO NAME']}
                                    </div>
                                    </div>
                                </div>
                                </div>
        """,unsafe_allow_html=True
                        )
                except:
                    st.error('Client ID is not exist Please try again')

                    

Front()
