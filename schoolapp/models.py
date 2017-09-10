import uuid

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _


# 基础信息
CHANNEL_TYPE_CHOICES = (
    ("ONLINE", "线上"),
    ("OFFLINE", "线下"),
)

OPERATION_CHANNEL_TYPE_CHOICES = (
    ("转介绍", "转介绍"),
    ("流动收单", "流动收单"),
    ("定点收单", "定点收单"),
    ("中心市场活动", "中心市场活动"),
    ("异业合作活动", "异业合作活动"),
    ("社区公益活动", "社区公益活动"),
)


GENDER_CHOICES = (
    ("M", "男"),
    ("F", "女"),
)

TRACE_STATUS_CHOICES = (

)

CUSTOMER_CONTACT_SOURCE = (
    ("tmk-out", "tmk-out"),
    ("tmk-in", "tmk-in"),
    ("walk-in", "walk-in"),
)

## 基础信息表
class Center(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("中心管理")
        verbose_name_plural = _("中心管理")


class Note(models.Model):
    note = models.TextField(null=False, blank=False)


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', null=True, blank=True)
    student_id = models.AutoField(max_length=100, auto_created=True, verbose_name="学员编号", primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="学员姓名")
    english_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="英文名")
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER_CHOICES, verbose_name="性别", default=GENDER_CHOICES[0][0])
    parent_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="家长姓名")
    mobile_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="手机")
    other_mobile_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="其他手机")
    home_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="家庭电话")
    trace_status = models.CharField(max_length=100, null=True, blank=True, verbose_name="跟踪状态")
    trace_count = models.PositiveIntegerField(verbose_name="跟踪次数", default=0)
    promised_arrive_time = models.DateField(max_length=100, null=True, blank=True, verbose_name="诺到时间")
    birth = models.DateField(max_length=100, null=True, blank=True, verbose_name="生日")
    created_at = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name="登记日期")
    school = models.CharField(max_length=100, null=True, blank=True, verbose_name="就读学校")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="电子邮箱")
    refer_person = models.CharField(max_length=100, blank=True, null=True, verbose_name="推荐人")

    # 中心
    center = models.ForeignKey(Center, null=True, blank=True)

    # 方式, 
    contact_source = models.CharField(max_length=100, blank=True, null=True, verbose_name="方式", choices=CUSTOMER_CONTACT_SOURCE)

    id_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="证件号")
    refer_date = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name="登记日期")
    # notes = GenericRelation(Note)
    note1 = models.TextField(max_length=1000, null=True, blank=True, verbose_name="备注1")
    note2 = models.TextField(max_length=1000, null=True, blank=True, verbose_name="备注2")

    sale_person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="市场推广员")
    sale_person_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="市场推广员Id")

    record_person_name =  models.CharField(max_length=100, blank=True, null=True, verbose_name="录入员")
    record_person_id =  models.CharField(max_length=100, blank=True, null=True, verbose_name="录入Id")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("学生管理")
        verbose_name_plural = _("学生管理")


class CourseConsultant(models.Model):
    user = models.OneToOneField(User, related_name='consultant')
    mobile_phone = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("课程顾问")
        verbose_name_plural = _("课程顾问")


class Staff(models.Model):
    user = models.OneToOneField(User, related_name='staff')
    mobile_phone = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    center = models.ForeignKey(Center) # 中心

    def __str__(self):
        return self.name


# 业务管理
class OperationChannel(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False,
                             choices=OPERATION_CHANNEL_TYPE_CHOICES,
                             verbose_name="运营渠道")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("运营渠道管理")
        verbose_name_plural = _("运营渠道管理")


class MarketChannel(models.Model):
    #channel_id = models.AutoField(max_length=200, verbose_name="渠道ID", primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="渠道名称")
    channel_type = models.CharField(max_length=20, blank=False, null=False, choices=CHANNEL_TYPE_CHOICES,
                                     verbose_name="渠道类型", default=CHANNEL_TYPE_CHOICES[0][0])
    operation_channel_type = models.ForeignKey (OperationChannel, verbose_name="运营渠道")
    fee = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name="费用")
    isActive = models.BooleanField(default=bool, verbose_name="启用")
    place = models.CharField(max_length=200, null=False, blank=False, verbose_name="地点")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name="备注")
    center = models.ForeignKey(Center, verbose_name="中心")

    create_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("市场渠道管理")
        verbose_name_plural = _("市场渠道管理")


##################################################################################
# 教务管理
class ClassRoom(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("教室管理")
        verbose_name_plural = _("教室管理")


class ClassTimeSlot(models.Model):
    startTime = models.TimeField(max_length=100, null=False, blank=False)
    endTime = models.TimeField(max_length=100, null=False, blank=False)


class ClassRoomTimeSlotManagement(models.Model):
    time_slots = models.ManyToManyField(ClassTimeSlot)
    class_room = models.ForeignKey(ClassRoom)


# 开班计划
class StartNewClassPlan(models.Model):
    plan_id = models.AutoField (primary_key=True, verbose_name="开班计划ID")
    center = models.ForeignKey(Center)
    start_date = models.DateField(max_length=100, null=False, blank=False, verbose_name="开班日期")
    end_date = models.DateField(max_length=100, null=False, blank=False, verbose_name="结束日期")
    class_room = models.ForeignKey(ClassRoom, verbose_name="上课教室")
    class_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="班级名称")

    head = models.ForeignKey(Staff, null=True, blank=True, related_name="head", verbose_name="班主任")
    chinese_teacher = models.ForeignKey(Staff, related_name="chinese_teacher", verbose_name="中教老师")
    english_teacher = models.ForeignKey(Staff, related_name="english_teacher", verbose_name="外教老师")

    is_enabled = models.BooleanField(default=False, verbose_name="是否启用")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name="备注")
    course_duration = models.FloatField(null=False, blank=False, verbose_name="总课时")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("开班计划")
        verbose_name_plural = _("开班计划")


class CoursePlan(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="课程名称")
    level = models.IntegerField(blank=False, null=False, verbose_name="课程级别")
    tuition = models.FloatField(blank=False, null=False, verbose_name="学费")
    discount_fee = models.FloatField(blank=False, null=False, verbose_name="减免金额")



##################################################################################
# Finance Management
CONTRACT_STATUS = (
    ("NOT PAID", "未付款"),
    ("PAID", "已付款"),
)


class ContractManagement(models.Model):
    contract_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, verbose_name="学生")
    course_plan = models.ForeignKey(CoursePlan, verbose_name="课程")
    tuition = models.FloatField(blank=False, null=False, verbose_name="学费")
    contract_status = models.CharField(max_length=200, blank=False, null=False,
                                       choices=CONTRACT_STATUS, verbose_name="合同状态")
    reason = models.CharField(max_length=200, null=True, blank=True)
    is_resign = models.BooleanField(default=False, verbose_name="续约")

    class Meta:
        verbose_name = _("合同管理")
        verbose_name_plural = _("合同管理")



