import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 하찮은 운세", page_icon="🔮")

# 2. 스타일링 및 제목
st.title("🔮 오늘의 하찮은 운세 복채소")
st.write("거창한 미래는 모릅니다. 딱 오늘 하루의 '소소하고 하찮은' 행운과 컬러, 그리고 조심할 음식을 점쳐드립니다.")

# 3. 하찮은 운세 데이터베이스 (멘트를 많이 넣을수록 좋습니다!)
fortunes = [
    {"title": "🎁 편의점의 기적", "content": "오늘 편의점에 가면 당신이 찾는 2+1 상품의 마지막 하나를 겟하게 됩니다."},
    {"title": "☕ 완벽한 타이밍", "content": "오늘 탕비실에 갔을 때, 마침 새 커피가 내려져 있습니다. 첫 잔을 사수하세요."},
    {"title": "🎈 무선 이어폰의 가호", "content": "오늘 가방에서 무선 이어폰을 꺼냈을 때, 한 번에 연결됩니다. 소소한 평화."},
    {"title": "💧 물 한 모금의 여유", "content": "오늘 물을 마실 때, 마침 목구멍이 가장 원하던 온도의 물이 나옵니다. 크으-"},
    {"title": "🧦 양말의 배신", "content": "오늘 양말을 신고 나갔는데, 하루 종일 한 번도 양말이 발가락 사이로 말려 들어가지 않습니다."},
    {"title": "📩 스팸 메일의 진실", "content": "오늘 스팸 메일함을 확인해 보세요. 혹시... 당신을 기다리던 중요한 메일이 거기 있을지도?"},
    {"title": "🐱 길고양이의 간택", "content": "오늘 길가에서 고양이를 만난다면, 그 고양이가 당신을 향해 눈인사를 건넬 확률이 80%입니다."},
    {"title": "🚌 버스의 가호", "content": "오늘 정류장에 가자마자, 당신이 타야 할 버스가 바로 도착합니다. 뛰지 마세요."},
    {"title": "🍫 당 충전의 순간", "content": "오늘 가방 구석을 잘 찾아보세요. 잊고 있던 초콜릿이나 캔디가 발견됩니다."},
    {"title": "👍 무플 방지 위원회", "content": "오늘 어딘가에 댓글을 단다면, 누군가 즉시 '좋아요'를 눌러줍니다."},
    {"title": "🧹 완벽한 먼지 제거", "content": "오늘 스마트폰 화면을 닦았는데, 단 한 번의 움직임으로 모든 지문이 깨끗하게 사라집니다."},
    {"title": "🌞 창가의 축복", "content": "오늘 오후 3시경, 창가에서 쏟아지는 햇살이 당신의 지친 몸을 잠시나마 따뜻하게 감싸줍니다."},
    {"title": "🎁 택배의 기적", "content": "오늘 택배 상자를 뜯었을 때, 마침 딱 한 번에 뜯어지는 쾌감을 경험하게 됩니다."},
    {"title": "🎤 완벽한 선곡", "content": "오늘 셔플로 음악을 틀었는데, 첫 번째 곡이 마침 당신의 기분과 완벽하게 맞아떨어집니다."}
    # --- 전통적 감성 + 하찮은 반전 버전 ---
    {"title": "🧭 동방의 귀인", "content": "오늘 동쪽에서 귀인이 나타납니다. 아, 근데 그 귀인이 당신의 택배 기사님일 확률이 99%입니다. 벨소리에 집중하세요."},
    {"title": "🧭 서방의 희소식", "content": "서쪽에서 반가운 소식이 들려옵니다. 주로 당근마켓 거래 성사나 택배 배송 완료 문자일 가능성이 큽니다."},
    {"title": "🧭 남방의 재물운", "content": "남쪽으로 이동하면 재물이 따릅니다. 길가다 100원을 줍거나, 편의점 바닥에서 잃어버린 동전을 발견할 운세입니다."},
    {"title": "🧭 북방의 인연", "content": "북쪽에서 뜻밖의 인연을 마주합니다. 아는 척하기엔 조금 어색한 전 직장 동료일 수 있으니 스마트폰을 보는 척하세요."},
    {"title": "💎 횡재의 기운", "content": "오늘 횡재수가 있습니다. 바지 주머니를 잘 뒤져보세요. 작년 겨울에 넣어둔 1,000원짜리 지폐가 당신을 기다립니다."},
    
]
lucky_colors = [
    {"name": "갓 볶은 원두색", "desc": "커피가 매우 당기게 될 것입니다. 한 잔 마시고 시작하세요."},
    {"name": "어제 입은 양말색", "desc": "가장 익숙하고 편안한 행운이 찾아옵니다."},
    {"name": "잘 익은 귤색", "desc": "상큼한 비타민 같은 소소한 웃음이 생길 수 있습니다."},
    {"name": "지나가는 택시색", "desc": "집에 빨리 가고 싶은 마음이 운으로 작용해 칼퇴할 예감!"},
    {"name": "편의점 1+1 행사표 색", "desc": "지나가다 예상치 못한 덤을 얻게 될지도 모릅니다."},
    {"name": "먼지 없는 유리창색", "desc": "오늘 하루 시야가 맑고 막힘이 없을 것입니다."},
    {"name": "퇴근하고 싶은 하늘색", "desc": "하늘을 한 번 보세요. 퇴근 시간이 조금 더 빨리 다가올 것 같은 기분이 듭니다."}
]
# [추가] 오늘 피해야 할 음식 리스트
avoid_foods = [
    {"name": "남이 탐내는 마지막 치킨 한 조각", "desc": "평화가 치킨 한 조각보다 중요합니다. 오늘은 양보하세요. 그래야 더 큰 복이 옵니다."},
    {"name": "식어서 기름 뜬 제육볶음", "desc": "첫맛은 좋으나 끝맛은 설거지 걱정뿐입니다. 따뜻할 때 드시거나 다른 메뉴를 보세요."},
    {"name": "국물이 다 쫄아버린 라면", "desc": "면만 먹기엔 너무 짭니다. 당신의 혈압과 오후의 갈증을 위해 피하는 것이 좋습니다."},
    {"name": "눅눅해진 탕수육 찍먹파의 부먹", "desc": "취향 존중이 안 된 음식은 소화가 잘 안 될 수 있습니다. 오늘은 확실한 메뉴를 선택하세요."},
    {"name": "편의점 구석의 정체불명 샌드위치", "desc": "유통기한은 남았어도 왠지 모를 불안함이 엄습합니다. 신선한 것을 고르세요."},
    {"name": "얼음이 다 녹아 밍밍해진 아메리카노", "desc": "이 맛도 저 맛도 아닌 것은 기분을 축 처지게 합니다. 새로 한 잔 시원하게 마시는 게 낫습니다."}
]
# 4. 운세 뽑기 상태 관리
if 'lucky_fortune' not in st.session_state:
    st.session_state.lucky_fortune = None
if 'lucky_color' not in st.session_state:
    st.session_state.lucky_color = None
if 'avoid_food' not in st.session_state:
    st.session_state.avoid_food = None

if st.button("🔮 나의 하찮은 행운 확인하기", use_container_width=True):
    # 로딩 효과
    progress_text = "우주적 기운과 색채, 음식의 조화를 맞추는 중..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    # 랜덤 선택
    st.session_state.lucky_fortune = random.choice(fortunes)
    st.session_state.lucky_color = random.choice(lucky_colors)
    st.session_state.avoid_food = random.choice(avoid_foods)
    st.snow()
    
if st.session_state.lucky_fortune:
    f = st.session_state.lucky_fortune
    c = st.session_state.lucky_color
    a = st.session_state.avoid_food
    
    st.divider()
    # 1. 운세 출력
    st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>🎊 {f['title']} 🎊</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px;'>{f['content']}</p>", unsafe_allow_html=True)
    
    st.divider()
    # 2. 행운 컬러 & 피해야 할 음식 (2단 레이아웃)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"<h3 style='text-align: center;'>🎨 행운의 컬러</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; color: #FF4B4B;'>{c['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 14px;'>{c['desc']}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<h3 style='text-align: center;'>🚫 피해야 할 음식</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; color: #555555;'>{a['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 14px;'>{a['desc']}</p>", unsafe_allow_html=True)

# 5. 푸터
st.divider()
st.caption("주의: 결과에 불만이 있어도 개발자는 책임지지 않습니다. 마음에 안 들면 '될 때까지' 누르는 게 국룰입니다. 😉")
