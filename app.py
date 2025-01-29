import streamlit as st
import time
from fpdf import FPDF
from datetime import datetime

# Function to generate the PDF
def generate_pdf(aadhar_number, full_name, mobile_number, gender, address, customer_id):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="eKYC Verification - Verified", ln=True, align='C')

    # Adding data to the PDF
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    
    pdf.cell(200, 10, txt=f"Full Name: {full_name}", ln=True)
    pdf.cell(200, 10, txt=f"Mobile Number: {mobile_number}", ln=True)
    pdf.cell(200, 10, txt=f"Reference ID: eujfiytghjyb12", ln=True)
    pdf.cell(200, 10, txt=f"Gender: {gender}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True)
    pdf.cell(200, 10, txt=f"Aadhaar ID: XXXX-XXXX-{aadhar_number[-4:]}", ln=True)
    pdf.cell(200, 10, txt=f"Customer ID: {customer_id}", ln=True)
    pdf.cell(200, 10, txt=f"Created On: 29 Jan 2025", ln=True)
    pdf.cell(200, 10, txt=f"Verified On: {datetime.now().strftime('%d %b %Y: %I:%M %p')}", ln=True)

    # Adding placeholders for uploaded photo and aadhar xml document
    pdf.ln(10)
    pdf.cell(200, 10, txt="Document: Aadhar XML", ln=True)
    pdf.cell(200, 10, txt="Uploaded Photo: Placeholder", ln=True)

    # Validated data
    pdf.ln(10)
    pdf.cell(200, 10, txt="Validated Data:", ln=True)
    pdf.cell(200, 10, txt=f"Aadhaar Number: {aadhar_number}", ln=True)

    # Saving the file
    pdf_output = f"ekyc_verified_{aadhar_number}.pdf"
    pdf.output(pdf_output)

    return pdf_output

# Streamlit Interface
def ekyc_verification():
    st.title("eKYC Verification")

    # Input Aadhaar Number
    aadhar_number = st.text_input("Enter Aadhaar Number (12 digits)", max_chars=12)

    if len(aadhar_number) == 12:
        st.write(f"Aadhaar Number: {aadhar_number}")
        
        # Input OTP
        otp = st.text_input("Enter OTP", max_chars=4)
        
        if otp == "1100":
            st.success("eKYC Verified Successfully!")
            
            # Displaying the verified details
            full_name = "Subir Singh"
            mobile_number = "9873387612"
            gender = "Male"
            address = "B1/639 A, Janakpuri, New Delhi, Delhi 110058, India"
            customer_id = "lkjeytrevdmnndggd14528"

            st.write(f"Full Name: {full_name}")
            st.write(f"Mobile Number: {mobile_number}")
            st.write(f"Reference ID: eujfiytghjyb12")
            st.write(f"Gender: {gender}")
            st.write(f"Address: {address}")
            st.write(f"Aadhaar ID: XXXX-XXXX-{aadhar_number[-4:]}")
            st.write(f"Customer ID: {customer_id}")
            st.write(f"Created On: 29 Jan 2025")
            st.write(f"Verified On: {datetime.now().strftime('%d %b %Y: %I:%M %p')}")

            # Generating the PDF
            pdf_file = generate_pdf(aadhar_number, full_name, mobile_number, gender, address, customer_id)

            # Providing the PDF download link
            with open(pdf_file, "rb") as file:
                st.download_button("Download Verified eKYC PDF", file, file_name=pdf_file)

        else:
            st.error("Invalid OTP. Please try again.")
    else:
        st.warning("Please enter a valid 12-digit Aadhaar number.")

if __name__ == "__main__":
    ekyc_verification()
