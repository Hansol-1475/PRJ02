import streamlit as st
import time

st.title(':two: 번째 프로젝트 :smile:')
# st.header('')
st.subheader('대한민국 의사증원, 몇 명이 적절한가 :grey_question')

with st.spinner( text = '로딩중... '):
    time.sleep(3.0)

col01,col02,col03 = st.tabs([':large_yellow_square: 데이터 분석', ':large_orange_square: 데이터 시각화', ':large_green_square: 프로젝트 결과'])

image_url_0 = 'https://github.com/Hansol-1475/PRJ02/blob/main/OECD%20datas/images/OECD_2017_doctor_ratio.png?raw=true'
image_url_1 = 'https://github.com/Hansol-1475/PRJ02/blob/main/OECD%20datas/images/OECD_see_a_doc.png?raw=true'
image_url_2 = 'https://github.com/Hansol-1475/PRJ02/blob/main/other%20images/%EC%A0%84%EA%B3%B5%EC%9D%98%20%ED%8F%89%EA%B7%A0%20%EC%A3%BC%EB%8B%B9%20%EA%B7%BC%EB%AC%B4%EC%8B%9C%EA%B0%84.png?raw=true'
image_url_3 = 'https://github.com/Hansol-1475/PRJ02/blob/main/other%20images/%ED%95%9C%EA%B5%AD%20%EC%9D%98%EC%82%AC%20%ED%8F%89%EA%B7%A0%20%EC%A7%84%EB%A3%8C%EC%8B%9C%EA%B0%84.png?raw=true'

col01.write('대한민국 의사들은 어떻게 지내고 있는가')
col01.image(image_url_0, caption='인구 1000명당 활동 의사 수 (2017년)')
col01.image(image_url_1, caption='의사당 진찰건수 (2019년)')
col01.image(image_url_2, caption='전공의 평균 주당 근무시간')
col01.image(image_url_3, caption='1차의료 평균 진료시간')

image_url_4 = 'https://github.com/Hansol-1475/PRJ02/blob/main/visualize/doc_num_of_main4.png?raw=true'
image_url_5 = 'https://github.com/Hansol-1475/PRJ02/blob/main/visualize/kr_future_population.png?raw=true'

col02.image(image_url_4, caption='OECD 주요 고령화 국가 인구 1천명 대비 의사수')
col02.image(image_url_5, caption='2035년, 2045년 대한민국 연령별 예상 인구 분포도')


col03.write(' 대한민국은 OECD 38개국들과 비교하여 1천명당 의사수가 2021년 기준 3.07명으로 고령화 수치가 가장 높은 4개국(이탈리아, 스페인, 한국, 일본) 평균인 4.78명에 상당히 못 미쳤습니다')
col03.write(' 시장 경제 체제에서 수요와 공급이 가격을 결정하듯이 OECD 국가들 중 봉직의 연봉은 1인당 GDP 대비 5.06배로 칠레 5.12배 다음 2번째로 높았다')
col03.write(' 그럼에도 불구하고 고령화 증가 비율은 3.3%로 OECD 국가들 중 가장 높으며 앞선 4개국의 고령화 증가율 평균은 2.3%에 불과한것으로 나타났다')
col03.write(' 이에 첫 번째로 내릴 수 있는 결론은 의대생 증원은 OECD 국가들의 상황과 비교할 때, 필수적으로 보인다')

st.sidebar.title(':black[공공데이터를 이용한 AI 챗봇 과정]')
st.sidebar.write('조장 : 김한솔')
st.sidebar.write('조원 : 이혁빈, 황성현')
st.sidebar.write('')
st.sidebar.write('역할분담')
st.sidebar.write('김한솔 : 데이터수집·정리·시각화, 앱 개발 및 배포, 사전 및 중간 발표')
st.sidebar.write('이혁빈 : 데이터수집·정리·시각화')
st.sidebar.write('황성현 : 데이터 수집·정리, 최종 발표')
