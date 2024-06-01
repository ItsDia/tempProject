# from django.contrib import admin
# from Service.models import Parameter_Concept,ServiceType
#
# @admin.register(Parameter_Concept)
# class ParameterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_input')
#     pass
#
# @admin.register(ServiceType)
# class ServiceTypeAdmin(admin.ModelAdmin):
#     list_display = ('name','display_concepts')
#     filter_horizontal = ('concepts',)  # 改善多对多字段的选择界面
#
#     def display_concepts(self, obj):
#         # 通过多对多字段 concepts 获取所有关联的 Parameter_Concept 实例
#         # 并返回它们的名称列表，以字符串形式显示
#         return ", ".join([concept.name for concept in obj.concepts.all()])
#
#     display_concepts.short_description = 'Concepts'
