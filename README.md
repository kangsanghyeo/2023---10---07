# 2023---10---07
문제 : alien이 두개가 나와야 하지만 alien_group에 더 이후에 넣은 alien만이 화면에 나오는 문제가 있었다
해결 방안 : alien_group을 alien_group1과 alien_group2로 나누어 alien1은 alien_group1로 가게 하고 alien2는 alien_group2로 가게 하여 문제를 해결하였다
문제 : 사각형을 만들때 스페이스 바를 누르기 전에 그려지는 문제
해결 방안 : 사각형을 그리는 코드에 game_state == GAME_PLAY를 추가

알아낸 것 : alien.rect.left
                  alien.rect.top 은 외계인 왼쪽 꼭지점  그 반대는 bottom이라 한다 

또 다른 기능 추가 
1.화면에서 움직일수있는것이 투석기 하나 뿐이니 wasd나 다른 키를 이용해 alien을 움직일수있는 기능 추가
2. 게임을 2인 게임으로 만든후 외계인이 점수를 얻을수있는 방식인 파란색 사각형 을 먹어 외계인 점수를 올려 시간이 다 지난후 누가 더 점수가 높은지로 승패를 가르는 게임을 만들려한 (시간 부족)
