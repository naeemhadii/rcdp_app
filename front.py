import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


class Front:
    def __init__(self):
        self.uploaded_file = './data/clients.xls'
        # Initialize the session state
        if 'page' not in st.session_state:
            st.session_state['page'] = 'front'  # Default state

        # Call the correct page function based on the session state
        if st.session_state['page'] == 'front':
            self.front()
        elif st.session_state['page'] == 'next':
            self.next_page()

    def front(self):
        # Render HTML header and UI components for the front page
        components.html(
            "<h1 style='text-align:center;font-family:sans-serif;'>Excel File</h1><hr>", height=100
        )
        
        # Allow user to upload Excel files
        self.uploaded_file = st.file_uploader(
            label='Upload Excel File',
            type=['xls', 'xlsx']
        )

        # Handle uploaded files
        if self.uploaded_file:
            try:
                # Read the uploaded Excel file
                data = pd.read_excel(self.uploaded_file)  # Load the data into a DataFrame
                self.df = pd.DataFrame(data)

                # Check if the DataFrame is empty
                if self.df.empty:  # Use the DataFrame's .empty attribute to check if it's empty
                    st.warning(f"The uploaded file  is empty.")
                else:
                    if self.uploaded_file.type:
                        st.success(f"File Loaded successfully.")
                        if st.button("Next",use_container_width=True):
                            st.session_state['page'] = 'next'
                            return self.uploaded_file
                    elif not self.uploaded_file.type:
                        st.warning('upload a valid excel file')
                        
                        # return self.df
                        # self.clients = 
                    # st.table(df)  # Show data in a table
            except Exception as e:
                # If there is an error while processing
                st.error(f"Error processing the file '{self.uploaded_file.name}': {e}")
        else:
            st.info('Please upload Data')
            # Navigation Button to move to the next page

    def next_page(self):
        # Render the next page content
        # st.subheader("Next Page")
        # st.write("You are now on the next page. Here you can implement other logic.")
        # st.dataframe(self.df)

        st.sidebar.markdown(
            "<h1 style='padding:0px;'>Key Features</h1>",
            unsafe_allow_html=True
        )
        st.sidebar.html(body='<hr>')
        credit = st.sidebar.selectbox(label='Select Credit Officer',options=['','Hafiza Shamim Younas','ZOBIA ABAD','Mr Shahid co','Sarazar Asif','Saddam.Hussain','Nadeem Afzal','Mr.Muhammad Naeem'])
        search = st.text_input(label='Search',placeholder='Search by Client ID',label_visibility='collapsed')
        if st.button(label='Search',use_container_width=True):
            ids = int(search)
            df = pd.read_excel(self.uploaded_file)
            df[(df == ids).any(axis=1)]

        st.html(body=f'<h2>{credit}</h2>')
        list = [' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        product = ['','CED','BEL','EDF','LSF','LSF-15','LSF-18','SME','SME-2']
        install_wise = st.selectbox(
            label='installment wise',
            options=[x for x in list],
            placeholder='Choose an option',
        )

        if credit:
            try:
                ids = credit
                df = pd.read_excel(self.uploaded_file)
                filter = df[(df == ids).any(axis=1)]
                if install_wise:
                    install = install_wise
                    filter[(df==install).any(axis=1)]


            except:
                st.error('nothing to founds')


        product_wise = st.selectbox(
            label='Product wise',
            options=[x for x in product],
        )
        if credit:
            try:
                ids = credit
                df = pd.read_excel(self.uploaded_file)
                filter = df[(df == ids).any(axis=1)]
                if install_wise:
                    prod = product_wise
                    filter[(df==prod).any(axis=1)]


            except:
                st.error('nothing to founds')



        # Navigation button to return to the front page
        if st.button("Go to Front Page",use_container_width=True):
            st.session_state['page'] = 'front'

    
    def clicked(self,value):
        st.text(body=value.data)
# Instantiate the class
Front()
