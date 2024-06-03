import json

from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Service
from .integrated_forward_backward_search_with_updated_backward_search import create_sample_data, forward_expand, backward_search
import random
from django.core import serializers
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

        if not Service.objects.exists():
            services_info = {
                "userA": {"input": "userN,userFV", "output": "userID"},
                "vehicleCC": {"input": "vehicleCV", "output": "vehicleID"},
                "deliveryO": {"input": "userID,vehicleID", "output": "pName,pPhone,origin,des"},
                "routeP": {"input": "origin,des", "output": "route,time"},
                "billing": {"input": "origin,des", "output": "cost"},
                "exchangeR": {"input": "cost,USD,EUR", "output": "newCost"},
            }

            for i in range(1):
                for service_type, concepts in services_info.items():
                    service = Service(
                        name=f"{service_type}_{i}",
                        cost=random.randint(1, 100),
                        input_concepts=concepts["input"],
                        output_concepts=concepts["output"],
                        type=service_type,
                    )
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


def initial(request):
    if not Service.objects.exists():
        services_info = {
            "userA": {"input": "userN,userFV", "output": "userID"},
            "vehicleCC": {"input": "vehicleCV", "output": "vehicleID"},
            "deliveryO": {"input": "userID,vehicleID", "output": "pName,pPhone,origin,des"},
            "routeP": {"input": "origin,des", "output": "route,time"},
            "billing": {"input": "origin,des", "output": "cost"},
            "exchangeR": {"input": "cost,USD,EUR", "output": "newCost"},
        }

        for i in range(1):
            for service_type, concepts in services_info.items():
                service = Service(
                    name=f"{service_type}_{i}",
                    cost=random.randint(1, 100),
                    input_concepts=concepts["input"],
                    output_concepts=concepts["output"],
                    type=service_type,
                )
                service.save()
    return HttpResponse("finish")


def composition(request):
    # print(request.body)
    print(request.body)
    json_param = json.loads(request.body.decode())

    initial_str = json_param['initial'].split(",")
    goal_str = json_param['goal'].split(",")

    concept_dict,services,service_map = create_sample_data()

    initial_concepts = [concept_dict[name] for name in initial_str]
    goal_concepts = [concept_dict[name] for name in goal_str]


    # 执行前向扩展以构建规划图
    print("start fe")
    # print(service_map)
    pg = forward_expand(service_map, initial_concepts, goal_concepts)

    print("start bs")
    # 执行后向搜索以找到计划
    results = backward_search(pg, initial_concepts, goal_concepts)

    # 返回结果
    return JsonResponse(results)


def add_new_service(request):
    json_param = json.loads(request.body.decode())
    service_name = json_param['name']
    service_input = json_param['input']
    service_output = json_param['output']
    service_type = json_param['type']
    service_label = json_param['label']

    service = Service(
        name=service_name,
        cost=random.randint(1, 100),
        input_concepts=service_input,
        output_concepts=service_output,
        type=service_type,
        label=service_label
    )
    service.save()
    return HttpResponse("finish")


def get_all_service(request):
    service_info = Service.objects.all()

    service_info_json = serializers.serialize('json', service_info)
    return JsonResponse(service_info_json, safe=False)

