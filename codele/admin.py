from django.contrib.admin import AdminSite, site
from django.contrib.auth.models import User

'''
TODO Custom admin homepage so it doesn't look so ugly to anyone that tries to access codele.digital:8080/admin

CURRENTLY NOT WORKING AS INTENDED
'''

# class CustomAdmin(AdminSite):
#     site_header = 'Codele Admin'
#     site_title = 'Admin'
#     index_title = 'Codele'
#     login_template = 'admin/login.html'

# admin_site = CustomAdmin(name='myadmin')

admin_site = site