"""상반기 자동차 세금으로 173000원이 부과 됐다. 그런데 납부 기간
내에 세금을 내지 않아 가산금이 3%부과 됐다. 가산금을 포함하여
내야하는 총 자동차 세금이 얼마인지를 구하는 프로그램을 작성 하시오."""
tax=173000
fine=tax*0.03
finalTax=int(tax+fine)
print(finalTax)