from django.views import View
from django.http import JsonResponse
from .models import Service
from .form import ServiceForm
from .integrated_forward_backward_search_with_updated_backward_search import create_sample_data, forward_expand, backward_search

class ServiceAPI(View):
    def get(self, request):
        name = request.GET.get('name')
        cost = request.GET.get('cost')
        input_concepts = request.GET.get('input_concepts')
        output_concepts = request.GET.get('output_concepts')
        type = request.GET.get('type')

        # 创建一个新的Service实例
        service = Service(name=name, cost=cost, input_concepts=input_concepts, output_concepts=output_concepts,
                          type=type)

        # 将实例保存到数据库
        service.save()

    def post(self, request):
        # 创建样本数据
        initial_concepts, goal_concepts, service_map = create_sample_data()

        # 执行前向扩展以构建规划图
        pg = forward_expand(service_map, initial_concepts, goal_concepts)

        # 执行后向搜索以找到计划
        results = backward_search(pg, initial_concepts, goal_concepts)

        # 返回结果
        return JsonResponse(results, safe=False)