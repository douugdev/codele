from django.contrib.admin import AdminSite

class CustomAdmin(AdminSite):
    site_header = 'Codele Admin'
    site_title = 'Admin'
    index_title = 'Codele'
    login_template = 'admin/login.html'


admin_site = CustomAdmin(name='myadmin')
