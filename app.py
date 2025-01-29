import streamlit as st
import time
from fpdf import FPDF
from datetime import datetime
import pytz
from PIL import Image

# Function to generate the PDF with table and image
def generate_pdf(aadhar_number, full_name, mobile_number, gender, address, customer_id, image_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="eKYC Verification - Verified", ln=True, align='C')

    # Add space
    pdf.ln(10)

    # Image (assuming the image is in the same folder as the script)
    try:
        img = Image.open(image_path)
        img_path = image_path
        pdf.image(img_path, x=10, y=30, w=30)  # Resize as per your preference
    except Exception as e:
        st.error(f"Error loading image: {e}")

    # Set table header
    pdf.ln(40)  # Moving below the image

    # Table: Define the column headers and width
    pdf.set_font("Arial", size=12, style='B')
    headers = ['Field', 'Details']
    col_widths = [50, 120]  # Width of each column
    
    # Loop to print the table headers
    for i in range(2):
        pdf.cell(col_widths[i], 10, headers[i], border=1, align='C')
    pdf.ln()

    # Get the current date and time in IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    created_on = datetime.now(ist_timezone).strftime('%d %b %Y: %I:%M %p')
    verified_on = created_on  # Assuming verified time is same as created time for now

    # Data rows (Details)
    pdf.set_font("Arial", size=12)

    data = [
        ("Full Name", full_name),
        ("Mobile Number", mobile_number),
        ("Reference ID", "eujfiytghjyb12"),
        ("Gender", gender),
        ("Address", address),
        ("Aadhaar ID", f"XXXX-XXXX-{aadhar_number[-4:]}"),
        ("Customer ID", customer_id),
        ("Created On", created_on),
        ("Verified On", verified_on),
        ("Document", "Aadhar XML"),
        ("Uploaded Photo", "Placeholder (Image included)"),
    ]
    
    # Loop to print data
    for row in data:
        pdf.cell(col_widths[0], 10, row[0], border=1, align='C')
        pdf.cell(col_widths[1], 10, row[1], border=1, align='L')
        pdf.ln()

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
            st.write(f"Created On: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d %b %Y: %I:%M %p')}")
            st.write(f"Verified On: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d %b %Y: %I:%M %p')}")

            # Path to the image
            image_path = "myPicHD.png"  # Make sure this file exists in the directory

            # Generating the PDF
            pdf_file = generate_pdf(aadhar_number, full_name, mobile_number, gender, address, customer_id, image_path)

            # Providing the PDF download link
            with open(pdf_file, "rb") as file:
                st.download_button("Download Verified eKYC PDF", file, file_name=pdf_file)

        else:
            st.error("Invalid OTP. Please try again.")
    else:
        st.warning("Please enter a valid 12-digit Aadhaar number.")

if __name__ == "__main__":
    ekyc_verification()
