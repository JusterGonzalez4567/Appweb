import streamlit as st
from form.contacto import contact_form

def ver_form_contacto():
    # Ventana modal para el formulario de contacto
    contact_form()

def mostrar():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("img/Procesos.jpg", width=230)
    with col2:
        st.title("Juster Eduardo", anchor=False)
        st.write(
            "Analista de datos junior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. "
            "Especializado en Ciencia de Datos."
        )
  # Botón para mostrar el formulario de contacto en la ventana modal
    if st.button("Contacto"):  
        ver_form_contacto()

    # --- Experiencia y calificaciones ---
st.write("\n")
st.subheader("Experiencia y calificaciones", anchor=False)
st.write("""
- Fuerte experiencia en soporte Tecnico 
- Buen conocimiento de creacion de Front end
- Experiencia en reparaciones de computadoras y telefonos 
- conocimentos en administracion de Redes
""")

    # --- HABILIDADES ---
st.write("\n")
st.subheader("Habilidades", anchor=False)
st.write("""
- Programación: Recat.js , Typescript, javascript
- Repaciones: microsoldadura, remanufacturacion de pantallas de telefonos
    """)

# Llama a la función principal
mostrar()