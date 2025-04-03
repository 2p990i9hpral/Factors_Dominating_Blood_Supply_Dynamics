# Documents

[Paper](<How is Korea’s Blood Supply Maintained.pdf>)  

![](<images/ppt_thumbnail.png>)  
[Presentation](<Presentation.pdf>)

# Summary

COVID-19, 혈액 부족 사태, 프로모션이 혈액 수요/공급 역학 관계에 미치는 영향을 정량적으로 측정
- “혈액관리기본계획”에 의한 “혈액 수급 위기단계별 대응” (위기상황시 공급량 증가, 사용량 감소)의 동작 여부 확인
- “헌혈”에 있어서 지역, 성별 그룹간 차이 분석
- 프로모션의 효과 분석

# Source Codes
- [Yearly data EDA](analysis_main.ipynb)
- [Data Analysis (EDA/Modeling/Visualization)](analysis_main.ipynb)
# Project

## 데이터 수집, 정제

### 일반 프로모션 데이터

> ![](<images/Pasted image 20250401223136.png>)  
> 전처리 전 원본 데이터

> ![](<images/Pasted image 20250401223201.png>)  
> Python, Pandas를 사용해 전처리 한 데이터

보고서 형태의 원본 데이터를 python을 사용해 테이블 형태의 데이터로 전처리

### 특수 프로모션 데이터

> ![](<images/Pasted image 20250401223307.png>)  
> 웹 상의 특수 프로모션 데이터

> ![](<images/Pasted image 20250401223333.png>)  
> Python, Selenium을 사용해 수집, 정제한 데이터

웹상의 특수 프로모션 데이터를 Python, Selenium을 사용해 스크래핑, 테이블 형태로 가공

### 헌혈자 수 데이터

> ![](<images/Pasted image 20250401231516.png>)  
> 원본 엑셀 데이터를 Pandas Dataframe으로 변형, 누락일 처리

## EDA

> ![](<images/Pasted image 20250401223452.png>)  
> 요일, 휴일에 따른 헌혈자 수 데이터 분포 차이 확인

> ![](<images/Pasted image 20250401223837.png>)  
> 요일이 전체 헌혈자 수 데이터 분포에 미치는 영향 확인

> ![](<images/Pasted image 20250401223926.png>)  
> 휴일이 전체 헌혈자 수 데이터 분포에 미치는 영향 확인

> ![](<images/Pasted image 20250401224145.png>)  
> 월별 헌혈자 수 데이터 분포 차이 확인

> ![](<images/Pasted image 20250401224252.png>)  
> 강수량 변수의 유의성 확인

> ![](<images/Pasted image 20250401224750.png>)  
> COVID-19 기간동안의 혈액 보유상태 확인 (COVID 기간, 혈액 부족기간 변수의 유의성 확인)
## 모델링

> ![](<images/Pasted image 20250401225310.png>)  
> ![](<images/Pasted image 20250401225322.png>)  
> 데이터의 연간 계절성을 Fourier terms를 사용해 통제

> ![](<images/Pasted image 20250401224942.png>)  
> ![](<images/Pasted image 20250401225408.png>)  
> EDA를 통해 유의성을 확인한 변수들\*을 사용해 회귀모형 설정  
> (\* 요일, 휴일, 혈액 부족기간, COVID-19 기간, 연간 계절성 통제용 Fourier terms, 강수량, 프로모션 기간)

## 결론

> ![](<images/Pasted image 20250401221914.png>)  
> 혈액 공급량 모델의 회귀계수 추정치

> ![](<images/Pasted image 20250401225739.png>)  
> 혈액 사용량 모델의 회귀계수 추정치

요일, 휴일 변수가 사용/공급 모두에 있어 큰 영향을 주고 있음을 확인.  
COVID-19가 혈액 사용/공급량 모두를 감소시켰으며 그 중 공급 감소량이 더 큰 것을 확인.  
혈액 부족기간에는 혈액 사용량이 감소하고 공급량이 증가함을 확인.

> ![](<images/Pasted image 20250401221531.png>)  
> ![](<images/Pasted image 20250401230429.png>)  
> 지역/성별에 따른 프로모션 효과

모든 지역/성별 그룹에 있어 프로모션이 헌혈자 수를 증가시킴을 정량적으로 확인

> ![](<images/Pasted image 20250403210100.png>) 
> ![](<images/Pasted image 20250401230528.png>)  
> 스포츠 관람티켓 증정 프로모션의 효과  
> (지역내 특수 프로모션 중 스포츠 관람티켓 증정 프로모션이 가장 높은 헌혈자 수 증가 비율을 가짐)

특수 프로모션 중 스포츠 관람 티켓 증정 프로모션의 효과가 다른 방법에 비해 효과적임을 확인
