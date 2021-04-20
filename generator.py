import pdfkit
from uuid import uuid4
import os

def html_to_pdf(text):

    temp_id = uuid4()
    temp_file = f'{temp_id}.html'
    my_pdf = open(temp_file,'w')
    my_pdf.write(text)
    my_pdf.close()
    
    pdfkit.from_file(temp_file, f'pdfs/{temp_id}.pdf')
    os.remove(temp_file)
    return temp_id

def data_to_html(program):

    html_string = open('templates/base.html', 'r').read()

    html_string += f'''
    <div class="row">
        <div class="header-logo-column">
            <img src="{program.header.logo}" />
        </div>
        <div class="header-title-column">
            {program.header.title}
        </div>
    </div>'''

    for exercise in program.exercises:
        html_string += '<div class="row">'
        for image in exercise.images:
            html_string += f'<div class="column"><img src="{image}"/></div>'
        html_string += '</div>'
        html_string += f'<p> {exercise.description} </p><hr>'

    html_string += '</body></html>'
    return html_to_pdf(html_string)


if __name__ == '__main__':
    test = open('templates/test.html', 'r')
    html_to_pdf(test.read())
    test.close()