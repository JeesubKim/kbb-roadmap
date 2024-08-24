from django.http import HttpResponse
from django.template import loader
# Create your views here.
def main(request):
    base = "/media/internal/event"
    # 카드 스타일로 바꿀 것
    template = loader.get_template("event/event.html")
    context = {
        "events": [
            {
                "title":"초대 회원 모집 및 생존게임 in 난지 (지연 빨 초대)",
                "subtitle":"난지 캠핑장 극기훈련",
                "img":[{
                    "src":f"{base}/2014_3.jpg",
                    "alt":"난지캠핑장"
                }],
                "description":"KBB 회장 베프 동반, 모임의 기반을 다짐",
                
            },{
                "title":"2차 회원 모집 공고 및 오징어게임 in 둥지 (지연 빨 초대)",
                "subtitle":"둥지 베이스캠프 재점검 차 방문",
                "img":[{
                    "src":f"{base}/2014_12.jpg",
                    "alt":"둥지"
                }],
                "description":"KBB 회장 친동생 한동열이 베프 동반",
                
            },
            {
                "title":"둥지 모임 유니폼 정의",
                "subtitle":"뭘봐?",
                "img":[{
                    "src":f"{base}/kbb_uniform.jpg",
                    "alt":"뭘보노"
                }],
                "description":"은갈치 핸드폰 커버 씌운 폰으로 극기훈련 스케줄 기획중인 한회장",
                
            },{
                "title":"회장 부회장 임명식",
                "subtitle":"회장과 부회장만 기분좋음",
                "img":[{
                    "src":f"{base}/2015.jpg",
                    "alt":"보직을 가진자의 미소"
                }],
                "description":"보직을 가진자의 미소, 일반회원들은 표정으로 보아 철권통치로 다스려졌음이 여실히 드러난 역사의 증거",
                
            },{
                "title":"최초의 KBB 발대식",
                "subtitle":"KBB의 진정한 탄생",
                "img":[{
                    "src":f"{base}/2015_5_2.jpg",
                    "alt":"발대식"
                }],
                "description":"진정한 KBB의 탄생인것처럼 보이지만, 누구한명이 드레스코드 안지키고 떠날준비중이였던듯. (Hint 이전사진에서 표정 젤 안좋고 옷안입은사람)",
                
            },
            {
                "title": "가끔은 철권통치를 벗어나 음식 배급을 통한 사육 통치",
                "subtitle":"사육",
                "img":[{
                    "src":f"{base}/2015_5.jpg",
                    "alt":"사육"
                }],
                "description":"KBB 내부 불만은 1차적으로는 음식으로 보상",
                
            },{
                "title":"음식으로는 성에 안차는 행동대장의 속내",
                "subtitle":"여전히 회장과 부회장만 기분좋음",
                "img":[{
                    "src":f"{base}/2015_5_3.jpg",
                    "alt":"보직을 가진자의 미소"
                }],
                "description":"손은 V를 그리고 있으나 표정으로 보아 아직 노조가입 가능성 220%",
                
            },{
                "title":"스포스 근본 클럽을 피할 수 없음",
                "subtitle":"회장/부회장급만 즐길 수 있는 부자 스포스. 배트민턴",
                "img":[{
                    "src":f"{base}/2015_b.jpg",
                    "alt":"배드민턴"
                }],
                "description":"이날 배드민턴 채는 박살나고 찔러서 피한방울 안나올것같은 강인한 바디의 소유자인 누군가는 다쳤으나 스포스 기업으로써의 발돋움을 함 (참고사항: 배드민턴 치려고 요넥스 티샤스 입고왔는데 다침, 신발은 쪼리신고옴)",
                
            },
             {
                "title":"둥지에서 기강을 잡다",
                "subtitle":"헤이해진 기강을 바로잡고자 둥지 소집",
                "img":[{
                    "src":f"{base}/2015_11.jpg",
                    "alt":""
                }],
                "description":"2016년을 맞아 15년 말에 헤이해진 기강을 바로잡고자 하였으나 불주먹 사용시 논란이 될수 있어 술로써 다스림"
            },
            
            {
                "title":"2017년",
                "subtitle":"사진없음",
                "img":[{
                    "src":f"{base}/handongyeol.jpg",
                    "alt":""
                }],
                "description":"사진 구함, 사례는 한동렬 컨택 요망"
            },{
                "title":"2018년",
                "subtitle":"둥지에서 손수 고기를 굽는 한회장",
                "img":[{
                    "src":f"{base}/2018_1.jpg",
                    "alt":""
                },{
                    "src":f"{base}/2018_2.jpg",
                    "alt":""
                },{
                    "src":f"{base}/2018_3.jpg",
                    "alt":""
                }],
                "description":"대학원 진학으로 주먹만으로 통치하는것은 트렌드에 맞지않다고 생각, 손수 고기도 구워 줌"
            },{
                "title":"가방끈 +1",
                "subtitle":"회원들과 동일한 끈길이는 참을수 없음에",
                "img":[{
                    "src":f"{base}/2019_0.jpg",
                    "alt":""
                }],
                "description":"지 까지 겸비한 완벽한 통치자로 거듭나는 순간"
            },{
                "title":"두 해병의 옷이 붉게 물들다",
                "subtitle":"뭔가 노여운 일이있었던건지 핵불주먹 인계똥 소집",
                "img":[{
                    "src":f"{base}/2019_1.jpg",
                    "alt":""
                }],
                "description":"준비한 '고맙습니다, 사랑합니다' 화분은 성에 차지 않았고, 더해서 변치 않고 투쟁의 눈빛을 담아낸 일반회원 견동열의 표정으로 회장은 가짜웃음으로 사진을 찍을 수 밖에 없었다"
            },{
                "title":"하우스",
                "subtitle":"하우스를 달구다",
                "img":[{
                    "src":f"{base}/2019_2.jpg",
                    "alt":""
                },{
                    "src":f"{base}/2019_3.jpg",
                    "alt":""
                }],
                "description":"KBB 모임에 사건사고는 기본옵션중의 하나인데, 찌라시에 의하면 역시나 스파클링와인 분수쇼로 하우스판을 후끈하게 달궜다는 후문"
            },{
                "title":"제보",
                "subtitle":"KBB 제보를 받습니다",
                "img":[{
                    "src":"#",
                    "alt":""
                }],
                "description":"KBB 2016~2018년 KBB 의 행방을 추적하고 있습니다. 사진이 있거나 목격하신분을 찾습니다. 연락부탁드립니다. jays.kim@hotmail.com. 비밀보장"
            },{
                "title":"참고",
                "subtitle":"참고사항",
                "img":[{
                    "src":f"{base}/wanted.jpg",
                    "alt":""
                }],
                "description":"희미한 사진속 인물 주인공을 찾습니다. 찾게되면 그뒤는 어떻게 될지 상상에 맡기겠습니다."
            },
        ]
    }


    
    return HttpResponse(template.render(context, request))