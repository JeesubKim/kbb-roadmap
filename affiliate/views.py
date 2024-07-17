from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def main(request):

    template = loader.get_template("affiliate/affiliate.html")
    context = {
        "cards": [
            {
                "title":"(주)곡반 보더스 / KBB",
                "content":"설산에서 꿈 꾼 모기업",
                "img":{
                    "src":"#",
                    "alt":"철권통치로 단합 된 KBB"
                }
            },
            {
                "title":"(주)곡반 산악 / KBS",
                "content":"회장/부회장 등산복 품위유지 구매 담당 업체",
                "img":{
                    "src":"#",
                    "alt":""
                }
            },
            {
                "title":"(주)곡반 싸이클 / KBC",
                "content":"수원시 주관 싸이클 본선 진출",
                "img":{
                    "src":"#",
                    "alt":""
                }
            },
            {
                "title":"(주)곡반 웨이크 보더스 / KBW",
                "content":"전설의 시작, 글로벌 진출을 목표로 브리티쉬의 Lady first 정신을 승계하는 주식회사 설립",
                "img":{
                    "src":"#",
                    "alt":""
                }
            },
            {
                "title":"(주)곡반 드라이빙 / KBD",
                "content":"(s)M3 / Mini / 520d - 로O갤러리 공식 후원 업체",
                "img":{
                    "src":"#",
                    "alt":""
                }
            },
            {
                "title":"(주)동탄 골프 클럽 / DTG",
                "content":"부회장 경기도 금강아파트 연합 동대표 출마 후원기업, 부회장으로 인해 처음으로 KB 이니셜을 버리고 설립한 기업",
                "img":{
                    "src":"#",
                    "alt":""
                }
            },
            {
                "title":"(주)인계 드라이빙 센터 / IGD",
                "content":"인계 불주먹 사비로 드라이빙 센터 및 지역주민 수퍼카 체험 라운지 설립, 최고급 레이싱 핸들을 입수했다는 후문",
                "img":{
                    "src":"#",
                    "alt":""
                }
            }
        ]
    }
    return HttpResponse(template.render(context, request))