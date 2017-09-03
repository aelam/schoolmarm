from django.contrib import admin

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


