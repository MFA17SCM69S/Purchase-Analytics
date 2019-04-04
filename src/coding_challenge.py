import numpy as np
import pandas as pd
data_set = pd.read_csv("/Users/malavikasujir/Desktop/School/Insight_code/instacart_2017_05_01/order_products__prior.csv")
data_set_1 = pd.read_csv("/Users/malavikasujir/Desktop/School/Insight_code/instacart_2017_05_01/products.csv")
data_set
data_set_1
pid = data_set['product_id']
pid
full_data_set = pd.merge(data_set,data_set_1,on='product_id')
full_data_set
answer =full_data_set['department_id'].value_counts()
answer
department_numbers = [0,4,16,19,7,1,13,3,15,20,9,17,14,12,11,18,6,5,8,21,2,10]
type(department_numbers)
answer = pd.DataFrame(answer)
department_numbers = pd.DataFrame(department_numbers)
output_part=pd.concat([answer,department_numbers],axis=1)
output_part=output_part[1:]
output_part
output_part.columns = ['Number of times requested from each department','Department number']
output_part
#sum(answer['department_id'])
two = full_data_set[full_data_set['reordered']==0]
two
ans_1 =two['department_id'].value_counts()
ans_1
department_numbers_1 = [0,4,16,19,13,1,7,15,9,17,3,20,14,12,11,18,6,5,21,8,2,10]
type(department_numbers_1)
department_numbers_1=pd.DataFrame(department_numbers_1)
ans_1 = pd.DataFrame(ans_1)
ans_1
output_2 = pd.concat([ans_1,department_numbers_1],axis=1)
output_2=output_2[1:]
output_2
output_2.columns = ['Number of times requested from each department for first order ','Department number']
output_2
output_part
solved = pd.merge(output_part,output_2,on='Department number')
solved
percentage = solved['Number of times requested from each department for first order ']/solved['Number of times requested from each department']
type(percentage)
percentage = pd.DataFrame(percentage)
type(percentage)
percentage
percentage=percentage.round(2)
solved =pd.concat([solved,percentage],axis=1)
solved
solved = solved.sort_values(by=['Department number'])
solved
solved.columns
solved.columns= [                 'Number of times requested from each department',
                                                     'Department number',
       'Number of times requested from each department for first order ',
                                                                       'Percentage']
solved
