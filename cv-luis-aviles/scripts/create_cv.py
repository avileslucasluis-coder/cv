from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist/assets/CV_Luis_Aviles.pdf'
FONT = ROOT / 'scripts/fonts'
pdfmetrics.registerFont(TTFont('CVSans', str(FONT / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('CVSansBold', str(FONT / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('CVSans', normal='CVSans', bold='CVSansBold', italic='CVSans', boldItalic='CVSansBold')
INK = colors.HexColor('#152b43')
BLUE = colors.HexColor('#315bda')
MUTED = colors.HexColor('#4a5a6b')
styles = {
    'name': ParagraphStyle('name', fontName='CVSansBold', fontSize=21, leading=26, textColor=INK, spaceAfter=4),
    'role': ParagraphStyle('role', fontName='CVSans', fontSize=11, leading=16, textColor=BLUE, spaceAfter=6),
    'contact': ParagraphStyle('contact', fontName='CVSans', fontSize=9, leading=13, textColor=MUTED, spaceAfter=10),
    'section': ParagraphStyle('section', fontName='CVSansBold', fontSize=9.7, leading=14, textColor=BLUE, spaceBefore=7, spaceAfter=4),
    'body': ParagraphStyle('body', fontName='CVSans', fontSize=9.5, leading=14, textColor=INK, spaceAfter=4),
    'job': ParagraphStyle('job', fontName='CVSansBold', fontSize=9.7, leading=14, textColor=INK, spaceBefore=5, spaceAfter=2),
    'meta': ParagraphStyle('meta', fontName='CVSans', fontSize=8.9, leading=13, textColor=MUTED, spaceAfter=4),
    'bullet': ParagraphStyle('bullet', fontName='CVSans', fontSize=9.3, leading=13.5, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=2),
}
story=[]
def p(text, style='body'):
    story.append(Paragraph(text, styles[style]))
def section(text): p(text, 'section')
def job(role, company, date, bullets):
    group=[Paragraph(role + ' | ' + company, styles['job']), Paragraph(date, styles['meta'])]
    group += [Paragraph('• ' + text, styles['bullet']) for text in bullets]
    story.append(KeepTogether(group))

p('LUIS ENRIQUE AVILES LUCAS', 'name')
p('ASISTENCIA CONTABLE Y ADMINISTRATIVA · TECNOLOGÍA', 'role')
p('Guayaquil, Ecuador &nbsp; | &nbsp; <link href="https://wa.me/593969951379" color="#152b43">096 995 1379</link><br/><link href="mailto:avileslucasluis@gmail.com" color="#152b43">avileslucasluis@gmail.com</link>', 'contact')
section('PERFIL PROFESIONAL')
p('Asistente contable y administrativo con experiencia en facturación, caja chica, retenciones, cuentas por pagar y cobrar e inventarios. Estudiante de Desarrollo de Software con un proyecto realizado en Python y SQL, conocimientos de diseño web, ofimática e inglés intermedio. Combino organización y atención al detalle con la capacidad de aplicar herramientas digitales a necesidades del negocio.')
section('EXPERIENCIA LABORAL')
job('Asistente contable / Apoyo en bodega', 'PALET CORP S.A.', 'Febrero 2025 – Diciembre 2025', [
    'Registro y control de facturas y retenciones de compras y ventas.',
    'Manejo de caja chica, control de chequeras y revisión de cuentas por pagar y por cobrar.',
    'Control de inventarios, entradas y salidas de equipos y suministros, revisión de herramientas y organización de materiales.'
])
job('Auxiliar de limpieza', 'Tu pintor Luis', 'Julio 2023 – Diciembre 2024', [
    'Preparación y limpieza de superficies, apoyo con materiales, lavado de herramientas y orden del área de trabajo.'
])
job('Pasante administrativo', 'PALET CORP S.A.', 'Agosto 2022', [
    'Digitalización, registro de facturas, organización y archivo de documentación administrativa y del personal.',
    'Elaboración de plantillas y formatos para procesos administrativos.'
])
section('PROYECTO TECNOLÓGICO')
p('<b>Sistema de registro de entradas y salidas | Python y SQL</b>')
p('Desarrollo de un sistema para registrar las horas de entrada y salida del personal en los distintos sitios de trabajo de una empresa. Programación en Python y manejo de datos con SQL, aplicados a una necesidad de control de asistencia.')
section('EDUCACIÓN')
p('<b>Tecnología en Desarrollo de Software — En curso</b><br/>Instituto Tecnológico Almirante Illingworth')
p('<b>Bachiller Técnico en Informática</b><br/>Escuela Particular La Consolata')
section('CAPACITACIÓN COMPLEMENTARIA')
p('<b>Python (Dominio Medio – Avanzado)</b> — Universidad Estatal de Milagro<br/><b>Contabilidad, Tributación y Laboral</b> — Visión Empresarial')
section('HABILIDADES E IDIOMAS')
p('<b>Ofimática:</b> Microsoft Excel, Word y PowerPoint; documentos, hojas de cálculo y presentaciones.<br/><b>Desarrollo:</b> Python, SQL, HTML, CSS, diseño web y JavaScript básico.<br/><b>Inglés:</b> nivel intermedio.<br/><b>Personales:</b> organización, responsabilidad, trabajo en equipo y aprendizaje rápido.')
story.append(Spacer(1, 5))
p('Referencias laborales disponibles a solicitud.', 'meta')

doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=43, rightMargin=43, topMargin=32, bottomMargin=30,
    title='CV | Luis Enrique Aviles Lucas', author='Luis Enrique Aviles Lucas', subject='Contabilidad, administración y tecnología')
def page_decoration(canvas, doc):
    canvas.setStrokeColor(colors.HexColor('#dfe5eb'))
    canvas.setLineWidth(0.5)
    canvas.line(43, 28, A4[0]-43, 28)
doc.build(story, onFirstPage=page_decoration, onLaterPages=page_decoration)
print(OUT)
