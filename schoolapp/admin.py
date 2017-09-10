from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from schoolapp import models


# 人员
# 业务管理

admin.site.register(models.Center)
admin.site.register(models.Student)
admin.site.register(models.Staff)
admin.site.register(models.CourseConsultant)

admin.site.register(models.OperationChannel)
admin.site.register(models.MarketChannel)
admin.site.register(models.Note)

TokenAdmin.raw_id_fields = ('user',)

