import streamlit as st
import PyPDF2

output_pdf = "documents/final_pdf.pdf" #save route


#Function to merge

def merge_pdf(output_patch, documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)

    pdf_final.write(output_patch)
    
#Front

st.image("assets/mergepdf.svg")
st.header("Unir Pdf")
st.subheader("Adjuntar pdfs para unir")

pdf_merged = st.file_uploader(label="", accept_multiple_files=True)

merge = st.button(label="Unir Pdfs")

try: 
    if merge:
        if len(pdf_merged) <- 1:
            st.warning("Debes adjuntar más de un pdf :)")
        else:
            merge_pdf(output_pdf, pdf_merged)
            st.success("Ya puedes descargar el pdf aquí :)")
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label="Descargar el pdf final", data=pdf_data, file_name="pdf_final.pdf")
except:
    st.warning("Ha ocurrido un error al querer unir los pdf's :(")
