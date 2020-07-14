from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

'''
Custom admin homepage so it doesn't look so ugly to anyone that tries to access codele.digital:8080/admin
'''

class CustomAdmin(AdminSite):
    site_header = 'Codele Admin'
    site_title = 'Admin'
    index_title = 'Codele'
    login_template = 'admin/login.html'

admin_site = CustomAdmin(name='myadmin')

admin_site.register(User)
