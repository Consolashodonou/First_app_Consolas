#Application on streamlit
#On a la possibilité de le faire avec d'autres outils comme urako?? mais streamlit est gratuit.

import streamlit as st

def main():
    st.title('Application WIADA 2023')
    user = st.text_input("Entrer votre nom: ")
    if st.button("Dis bonjour"):
        if user:
            st.write(f'Bonjour {user}')
        else:
            st.write('Bonjour à toutes et à tous')
if __name__ == "_main_":
    main()
