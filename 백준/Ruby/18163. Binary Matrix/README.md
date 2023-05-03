# [Ruby II] Binary Matrix - 18163 

[문제 링크](https://www.acmicpc.net/problem/18163) 

### 성능 요약

메모리: 31256 KB, 시간: 56 ms

### 분류

비트 집합, 선형대수학, 수학, 정수론

### 문제 설명

<p>키파는 율이로부터 <code>0</code>과 <code>1</code>이 가득한 <span style="font-style: italic;">n</span> by <span style="font-style: italic;">n</span> 표를 하나 선물로 받았습니다. 이 선물이 고마운 키파는 이 표를 커다란 행렬로 보고 <span style="font-style: italic;">K</span>라는 이름을 붙여 주었습니다. 키파는 이 행렬을 가지고 놀아보기로 했습니다. 키파는 <span style="font-style: italic;">K</span>의 각 성분이 0 혹은 1이라는 게 너무 마음에 든 나머지, 어떤 연산을 했을 때 계산 결과도 각 성분별로 짝수이면 0, 홀수이면 1을 채우기로 했습니다.</p>

<p>먼저 덧셈을 이용해서 <span style="font-style: italic;">K</span>, <span style="font-style: italic;">K</span>+<span style="font-style: italic;">K</span>, <span style="font-style: italic;">K</span>+<span style="font-style: italic;">K</span>+<span style="font-style: italic;">K</span>를 계산해 보다가 금방 싫증이 났습니다. <span style="font-style: italic;">K</span>+<span style="font-style: italic;">K</span>가 모든 성분이 0이어서 재미가 없었기 때문입니다. 그래서 곱셈을 하기로 했습니다. <span style="font-style: italic;">K</span>, <span style="font-style: italic;">K</span><sup>2</sup>, <span style="font-style: italic;">K</span><sup>3</sup>, ...을 계산하다가 어느 순간 똑같은 계산을 반복하고 있는 것 같았습니다!</p>

<p>같은 것을 반복하는 건 컴퓨터가 해야지 내가 하면 재미없다는 생각이 들었던 키파는, <span style="font-style: italic;">K</span>를 가지고 곱셈을 하다가 언제 싫증이 날지가 궁금해졌습니다. 키파가 예전 계산 결과를 다시 보게 될 때 이 곱셈 식에 <span style="font-style: italic;">K</span>가 몇 번 곱해져 있는지를 출력하는 프로그램을 작성해서 키파를 도와 줍시다.</p>

### 입력 

 <p>첫째 줄에 행렬의 크기 <span style="font-style: italic;">n</span>이 주어집니다.</p>

<p>둘째 줄부터 <span style="font-style: italic;">n</span>개의 줄에 총 <span style="font-style: italic;">n</span>개의 수가 공백을 사이에 두고 주어집니다. 이 수들은 모두 0 혹은 1입니다.</p>

### 출력 

 <p>키파가 예전 계산 결과를 다시 보게 될 때 그 곱셈 식에 곱해진 <em>K</em>의 개수를 출력합니다.</p>

