from flask import Flask, request, jsonify, render_template ,send_from_directory
import joblib
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

app = Flask(__name__,template_folder='templates')
model = joblib.load('model.pkl')
print("model loaded successfully")

def create_medical_report(pdf_filename, df, output_class, name):
    
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)
    content = []

    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='TitleStyle', fontSize=18, alignment=1)
    subtitle_style = ParagraphStyle(name='SubtitleStyle', fontSize=14, alignment=1)
    normal_style = styles['Normal']

    
    content.append(Paragraph('Medical Report', title_style))
    content.append(Spacer(1, 12)) 
    content.append(Paragraph('Patient Data and Results', subtitle_style))
    content.append(Spacer(1, 12)) 

   
    content.append(Paragraph(f'Patient Name: {name}', normal_style))
    content.append(Spacer(1, 12)) 

    
    data = [df.columns.tolist()] + df.values.tolist()

   
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.5, 0.5, 0.5)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0)),
    ]))
    
    content.append(table)
    content.append(Spacer(1, 12)) 

    
    result_message = 'Patient Results: Positive' if output_class == 1 else 'Patient Results: Negative'
    content.append(Paragraph(result_message, normal_style))


    document.build(content)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<path:filename>')

def serve_static(filename):
    return send_from_directory(app.template_folder, filename)

@app.route('/test')
def test_page():
    return render_template('test.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    patient_name = data.pop("name")
    df = pd.DataFrame([data.values()], columns=data.keys())
    # print(df)

    prediction = model.predict(df)[0]
    print(prediction)
    output_class = "Heart Diseased" if prediction == 1 else "No Heart Disease"
    print(output_class)

    create_medical_report('templates/medical_report.pdf', df, prediction, patient_name)
    print("report saved")

    return jsonify({
        "prediction": int(prediction),
        "output_class": output_class
    })

@app.route('/diseased')
def diseased():
    return render_template('diseased.html')

@app.route('/not_diseased')
def not_diseased():
    return render_template('not_diseased.html')

if __name__ == '__main__':
    app.run(debug=True)

