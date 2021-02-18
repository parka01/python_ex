"""지난 해 남부 대리점의 TV판매 금액은 3,500,000원이다.
판매에서 25%의 이익률이 발생했다면 총 판매 이익금을 구하는 
프로그램을 작성 하시오."""
income=int(3500000)
benefit=int(income*0.25)
print(benefit)
#----------------모범답안---------------------
tv_sale_amount=3500000
profit_ratio=0.25
total_sales_profit=tv_sale_amount*profit_ratio
print("총 판매 이익금은",'%.1f'%total_sales_profit,"입니다.")