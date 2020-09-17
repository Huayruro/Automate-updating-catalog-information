#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Generates a PDF report using Reportlab
def generate_report(attachment, title, paragraph):
 
  # Pdf file created
  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()
  #Title
  report_title = Paragraph(title, styles["h1"])
  # Body
  report_body=Paragraph(paragraph)

  #Build the PDF
  report.build([report_title, report_body])