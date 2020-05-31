from codele.admin import admin_site
from .models import Question, Answer
# Register your models here.
admin_site.register(Question)
admin_site.register(Answer)
