

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Callejon futbol - Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")


column_widths = [2, 1, 2]
with st.container():
    st.title("")
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.image("scr/logocallejon.png",width=1200, use_column_width=True, output_format='auto')
        
    with col2:
        st.text("")
          
    with col3: 
        st.image("scr/SDTLogoC.png",width=1200, use_column_width=True, output_format='auto')

with st.container():
    
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>write {color: white;}, font=</style>', unsafe_allow_html=True)
  
column_widths = [2, 1]

with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Callejon Futbol")        
        st.markdown("""
                #### Es una propuesta diferente de analizar el Futbol, tomando a los dos maximos referentes del siglo 21, Lionel messi y Cristiano Ronaldo, hacemos un repaso de sus estadisticas en sus años en La Liga y las comptencias continentales, por su paso por Barcelona y Real Madrid respectivamente 
                """) 
      
    
    with col2:
        imagen = "scr/callejon.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)  

def main():    

    st.title("Dashboard de analisis de insercion de mercado")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1300" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiN2VlOWM4ODUtMmQzOC00NDI5LWE1ZDAtOTU3MGZhMjdkZmNlIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
       </div>
        """,
        
        unsafe_allow_html=True
    )      
    
        
if __name__ == "__main__":
    main()

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    
    st.header("Contactanos!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/strategicdatatransform@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Tu consulta" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/StreamlitCallejon/blob/main/scr/fondoi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)