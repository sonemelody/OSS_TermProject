# Term Project


#### 20101200 컴퓨터공학과 김도연


* * *



### 지하철 시간대별 이용 현황 분석

1. 프로젝트 소개

+ 티머니에서 제공하는 교통카드 통계 자료를 이용해 각 시간마다 지하철의 이용 현황을 분석한다.
> + 사용자가 알고 싶은 시간의 지하철 이용량을 보여준다.
> + 오픈소스 라이브러리를 이용하여 csv 파일을 시각화한다.
+ 2021년 11월 통계 자료를 사용한다.
계획서에 썼던 주제는 오픈소스 라이브러리를 활용할 수 없다는 점과, 데이터 분석 측면에서 유용하지 않다고 생각하여 조금 더 활용성이 높은 지하철의 통계를 이용해 분석하기로 했다.  

#

2. 사용 라이브러리
+ matplotlib.pyplot (라이선스: <https://matplotlib.org/stable/users/project/license.html>)

#

3. 프로그램 동작
+ 이용량을 알고 싶은 시간을 입력하면, 그 시간에 승하차 인원이 가장 많은 역과 가장 적은 역을 알려준다.
+ 지하철의 시간대별 승하차 인원 추이를 꺾은선 그래프로 표현하여 전반적인 승객의 이용량을 알 수 있다.
+ 지하철의 24시간 이용량을 전부 막대 그래프로 표현하여 사용자가 입력한 시간이 아닌 다른 시간의 이용량도 알 수 있다.

* ![img1](https://user-images.githubusercontent.com/49124725/146889982-03028580-d01b-4ee0-99da-f67d8c5e0fd2.jpg)
* ![plot1](https://user-images.githubusercontent.com/49124725/146889984-077c1227-89ad-41f2-820c-aa75c96c85d5.png)
* ![plot2](https://user-images.githubusercontent.com/49124725/146889987-0882ccd1-1f21-4762-afdc-918df8b997dc.png)
* ![plot3](https://user-images.githubusercontent.com/49124725/146889989-abb44c4e-75fb-42c6-be7d-f935129037f9.png)
* ![plot4](https://user-images.githubusercontent.com/49124725/146889991-6d161814-d5c9-4ea3-af3a-ba4956ac1f33.png)
* ![plot5](https://user-images.githubusercontent.com/49124725/146889980-0ef85feb-0fee-4d04-9539-08753b44d9ea.png)

#

4. 아쉬운 점 및 보완 가능성
+ 단순히 지하철의 이용량을 분석한 프로그램이라 데이터의 활용 능력이 떨어진다.
+ 원하는 지하철역 혹은 노선을 입력하면 그에 맞는 지하철 이용량을 제공하는 프로그램으로 확장할 수 있을 것 같다.

#

5. 참고 자료
+ 모두의 데이터 분석 with 파이썬 (저자: 송석리, 이현아)
