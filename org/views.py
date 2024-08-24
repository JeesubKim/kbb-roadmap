from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def main(request):
    base = "/media/internal/org"
    template = loader.get_template("org/org.html")
    context = {
        "nodes": [
            {
                "position":"회장",
                "name":"한지훈",
                "img":[{
                    "src":f"{base}/han.jpg",
                    "alt":"한지"
                }],
                "description":"KBB 초대 회장, 인계불주먹, 살.리.도.라 챔피온 타이틀 보유자, 조만간 장충동 곰장파와 1:1대결 예정",
                "children":[
                    {
                        "position":"부회장",
                        "name":"위태윤",
                        "img":[{
                            "src":f"{base}/wi.jpg",
                            "alt":"위태"
                        }],
                        "description":"KBB 초대 부회장, 눈빛으로 민준,곰장충동을 제압하였으나 불주먹앞에서 눈빛 변함",
                        "children":[
                            {
                                "position":"명예회원",
                                "name":"박사장",
                                "img":[{
                                    "src":f"{base}/park.jpg",
                                    "alt":"박사"
                                }],
                                "description":"(주) KBW 설립 발대식에 참석하여 Lady first 목격으로 명예 자문위원 자격 획득, 부회장의 Better-half로 시민권 획득",
                                "children":[
                                    {
                                        "position":"명예 KBW 회원",
                                        "name":"웨이크 보드 사장님",
                                        "img":[{
                                            "src":f"{base}/wake.jpg",
                                            "alt":"웨보사"
                                        }],
                                        "description":"몇십년 케이블 웨이크 보드 운영 중에 처음으로 Lady first 목격한 사장님, 목격만으로 영주권 획득",
                                        "children":[
                                            
                                        ]
                                    },   
                                ]
                            },            
                        ]
                    },
                    {
                        "position":"행동대장 (현 신임 교육부장 겸임)",
                        "name":"견동열",
                        "img":[{
                            "src":f"{base}/yeol.jpg",
                            "alt":"견동"
                        }],
                        "description":"외부에서 KIM_CEO로 활동하다가 인계핵불주먹으로 단합 완료됨",
                        "children":[
                            {
                                "position":"개(犬)들의 제왕",
                                "name":"견동열",
                                "img":[{
                                    "src":f"{base}/kyun.jpg",
                                    "alt":"견동"
                                }],
                                "description":"개(犬)들의 제왕 평소에 개를 타고다닌다는 설만 신화처럼 돌다가 파파라치들에게 포착됨, 외부에서 KIM_CEO로 활동하다가 인계핵불주먹으로 단합 완료됨",
                                "children":[
                                    
                                ]
                            }
                        ]
                    },
                    {
                        "position":"일반 회원 (구 교육부장)",
                        "name":"김지섭",
                        "img":[{
                            "src":f"{base}/sub.jpg",
                            "alt":"지쇼핑"
                        }],
                        "description":"일반 회원",
                        "children":[
                                        
                        ]
                    },
                ]
            },
        ]
    }


    print(context)
    return HttpResponse(template.render(context, request))