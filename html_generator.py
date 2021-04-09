from django.template import Template, Context
from django.template.loader import get_template
from django.conf import settings
settings.configure() # We have to do this to use django templates standalone - see
# http://stackoverflow.com/questions/98135/how-do-i-use-django-templates-without-the-rest-of-django

# Our template. Could just as easily be stored in a separate file
template = """
<html>
<head>
<title>Template {{ title }}</title>
</head>
<body>
Body with {{ mystring }}.
</body>
</html>
"""

t = get_template(template)
c = Context({"title": "title from code",
             "mystring":"string from code"})
print (t.render(c))