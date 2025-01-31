# import pizza_order as po           #이처럼 쓸때는 po.함수
from pizza_order import *           #함수 이름 그대로 쓰는거

pizza_menu={'페페로니 피자': 3000,'치즈 피자': 3200,
            '콤비네이션 피자': 3500,'불고기 피자': 3600,'해산물 피자': 3800}
drink_menu={'콜라': 1500,'사이다': 1500,'생수':1000}


#피자 주문
order_pizza=menu_select(pizza_menu,'피자')
# print(order_pizza)
#음료 주문
order_drink=menu_select(drink_menu,'음료')
# print(order_drink)

#돈계산
pizza_money=money_calc(order_pizza,pizza_menu)
drink_money=money_calc(order_drink,drink_menu)

print(f'전체금액: {pizza_money+drink_money:,}원')