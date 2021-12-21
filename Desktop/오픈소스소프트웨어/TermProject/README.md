# Term Project


#### 20101200 컴퓨터공학과 김도연


* * *



### 지하철 시간대별 이용 현황 분석

1. 프로젝트 소개

+ 티머니에서 제공하는 교통카드 통계자료를 이용해 각 시간마다 지하철의 이용 현황을 분석한다.
> + 사용자가 알고 싶은 시간의 지하철 이용량을 보여준다.
> + 오픈소스 라이브러리를 이용하여 csv 파일을 시각화한다.
계획서에 썼던 주제는 오픈소스 라이브러리를 활용할 수 없다는 점과, 데이터 분석 측면에서 유용하지 않다고 생각하여 조금 더 활용성이 높은 지하철의 통계를 이용해 분석하기로 했다.  

#

2. 사용 라이브러리
+ matplotlib.pyplot (라이선스: <https://matplotlib.org/stable/users/project/license.html>)

#

3. 프로그램 동작
+ 이용량을 알고 싶은 시간을 입력하면, 그 시간에 승하차 인원이 가장 많은 역과 가장 적은 역을 알려준다.
+ 지하철의 시간대별 승하차 인원 추이를 꺾은선 그래프로 표현하여 전반적인 승객의 이용량을 알 수 있다.
+ 지하철의 24시간 이용량을 전부 막대 그래프로 표현하여 사용자가 입력한 시간이 아닌 다른 시간의 이용량도 알 수 있다.

* <img src="/path/to/img1.jpg" width="100%" height="100%" alt="실행화면"></img>  
* <img src="/path/to/plot1.png" width="100%" height="100%" alt="지하철 시간대별 승하차 인원 추이"></img>
* <img src="/path/to/plot2.png" width="100%" height="100%" alt="시간대별 승차 인원이 많은 역"></img>
* <img src="/path/to/plot3.png" width="100%" height="100%" alt="시간대별 승차 인원이 적은 역"></img>
* <img src="/path/to/plot4.png" width="100%" height="100%" alt="시간대별 하차 인원이 많은 역"></img>
* <img src="/path/to/plot4.png" width="100%" height="100%" alt="시간대별 하차 인원이 적은 역"></img>

#

4. 참고 자료
+ 모두의 데이터 분석 with 파이썬 (저자: 송석리, 이현아)
