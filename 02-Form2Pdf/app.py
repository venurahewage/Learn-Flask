from flask import Flask, render_template, request, Response, send_file
from io import BytesIO
from reportlab.pdfgen import canvas
import time

app = Flask(__name__)

# Initialize an empty list to store user input data
user_data = []

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/generate-pdf', methods=['GET', 'POST'])
def generate_pdf():
	if request.method == 'POST':
		# Retrieve user input from the form
		name = request.form.get('name')
		city = request.form.get('city')
		birthyear = request.form.get('byear')

		user_data.append({
			'Name': name,
			'City': city,
			'BirthYear': birthyear
		})
			

	time_format = time.strftime("%Y%m%d-%H%M%S")
	pdf_file = generate_pdf_file()
	return send_file(pdf_file, as_attachment=False, download_name=time_format+'.pdf')
	#return send_file(pdf_file, as_attachment=True, download_name=time_format+'.pdf')

def generate_pdf_file():
	buffer = BytesIO()
	p = canvas.Canvas(buffer)

	# Create a PDF document
	p.drawString(100, 750, "User Details")

	y = 700
	for data in user_data:
		p.drawString(10, y, f"Name: {data['Name']}")
		p.drawString(10, y - 20, f"City: {data['City']}")
		p.drawString(10, y - 40, f"Birth Year: {data['BirthYear']}")
		#y -= 60

	p.showPage()
	p.save()

	buffer.seek(0)
	return buffer

if __name__ == '__main__':
	app.run(debug=True)
