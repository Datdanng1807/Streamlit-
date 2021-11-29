import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import seaborn as sns
import os # accessing directory structure
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title="NHÓM DATA VISUALIZATION [NGHỊ]",
                  page_icon=":satisfied:",
                  layout="wide")

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif" 
                          
st.write("""
# Phân tích tác động của tai nạn đường bộ ở Mandalay (Myanmar)
""")
st.title("""
I. Mở đầu: 
""")
st.header("""
Phần 1: Lý do chọn đề tài, đối tượng và phạm vi nghiên cứu
 """)
st.write("""
Lý do chọn đề tài: 

An toàn giao thông đã trở thành vấn đề nan giải của mỗi quốc gia. Bởi
nhu cầu sinh hoạt, đi lại là thiết yếu đối với mỗi người dân và nhu cầu đó đang ngày càng tăng lên, đặc biệt là lưu thông trên đường bộ. Dẫn tới các vấn nạn liên quan đến an toàn giao thông xảy ra ngày càng nhiều, khiến vấn đề tai nạn giao thông trở nên khó khắc phục và ngày càng phức tạp. Ngoài ra, chính sự phát triển của khoa học - kỹ thuật như ngày nay, vấn nạn này còn trở nên xấu hơn và khiến cho sự an toàn trong giao thông suy giảm trầm trọng. 

Thành phố Mandalay là thành phố lớn thứ hai ở Myanmar, đã từng là thủ đô của Myanmar dưới triều đại Midon (1857). Do đó, có rất nhiều di tích lịch sử lâu đời thu hút khách du lịch trong và ngoài nước. Cùng với hệ thống giao thông, cơ sở vật chất - kỹ thuật, cơ sở hạ tầng hiện đại và phát triển. Cũng vì sự nhộn nhịp đó đã khiến vấn đề an toàn giao thông ở đây trở nên khó khăn và phức tạp hơn dẫn tới số lượng vụ tai nạn giao thông đường bộ trong khu vực ngày càng nhiều và khó giải quyết. Vì vậy người dân cần có những hành động thiết thực để giảm thiểu vấn đề tai nạn giao thông đường bộ bằng những hoạt động, cách thức phù hợp. Để phân tích sự tác động của tai nạn giao thông thì nhóm của chúng tôi xin được điểm lại và phân tích những số liệu về tai nạn giao thông đường bộ của Mandalay (Myanmar) trong từng Quý của năm 2017 và 2018. 

""")
#Phần 2: Nhập dữ liệu 
st.title("""
II. Nội dung: 
""")
st.header("""
Phần 2: Cài đặt và nhập số liệu 
 """)
st.code("""
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import seaborn as sns
import os # accessing directory structure
import pandas as pd
df = pd.read_excel("AccidentDataSet_excel.xlsx")
df.head()""", language='python')
st.write("""Dữ liệu số vụ tai nạn ở Mandalay""")

df = pd.read_excel("AccidentDataSet_excel.xlsx")
#tạo khung điều kiện:
st.sidebar.header("Bảng xem dữ liệu số vụ tai nạn ở Mandalay theo quý") 
quarter=st.sidebar.multiselect(
    "Chọn theo quý:",
    options = df["Quarter"].unique(),
    default = df["Quarter"].unique())     
df_select=df.query( "Quarter == @quarter")
st.dataframe(df_select)


#phần 3: Phân tích
#2.1. Phân tích số vụ tai nạn giao thông vào các thời điểm chính và trên các vùng trong từng quý của năm 2017 và 2018 
st.header("""
Phần 3. Phân tích tác động của tai nạn đường bộ ở Mandalay (Myanmar) nhóm em chia làm 4 nội dung phân tích: 
 """)
st.subheader("""
2. Nội dung phân tích 
""")
st.subheader("""
*       2.1. Phân tích số vụ tai nạn giao thông vào các thời điểm chính và trên các vùng trong từng quý của năm 2017 và 2018 *
""")
st.dataframe(df_select[["Quarter", "Day", "Night"]])
st.write("""Nhìn chung tổng số vụ tai nạn giao thông giữa ngày và đêm qua các quý của 2 năm 2017, 2018 không có sự chênh lệch đáng kể, trừ 2 quý đầu năm 2017. Vào 2 quý đầu năm 2017, tai nạn giao thông đường bộ xảy ra vào ban ngày nhiều hơn so với ban đêm. Cụ thể, số vụ tai nạn xảy ra vào ban ngày gấp 2 lần vào ban đêm (nhiều hơn 186 vụ) tại quý 1 năm 2017 và gấp 1,68 lần (nhiều hơn 150 vụ) tại quý 2 năm 2017. """)
st.code("""x = df["Quarter"]
Day = df["Day"]
Night = df["Night"]
labels = ["Day", "Night"]
fig, ax = plt.subplots()
ax.stackplot(x, Day, Night,labels=labels, colors = ['#1D2F6F','#8390FA'])
plt.xlabel('Quarter')
plt.ylabel('Frequency')
plt.title('The number of accident between Day and Night')
plt.xticks(rotation=30)
plt.show())""",language='python')
x = df_select["Quarter"]
Day = df_select["Day"]
Night = df_select["Night"]
labels = ["Day", "Night"]
fig, ax = plt.subplots()
ax.stackplot(x, Day, Night,labels=labels, colors = ['#1D2F6F','#8390FA'])
plt.xlabel('Quarter')
plt.ylabel('Frequency')
plt.title('The number of accident between Day and Night')
plt.xticks(rotation=30)
st.pyplot(fig)
st.write("""Trong giai đoạn 2017 - 2018, tổng số vụ tai nạn giao thông ở thành thị nhiều hơn nông thôn là 332 vụ. Vào các quý 3, 4 năm 2017 và quý 1, 3 năm 2018, tai nạn ở thành thị xảy ra nhiều hơn nông thôn và ngược lại vào các quý 1, 2 năm 2017, quý 2, 4 năm 2018. Chênh lệch nhiều nhất là vào quý 1 năm 2018 với số vụ tai nạn xảy ra ở thành thị nhiều gấp đôi nông thôn. """)
# 2.2. Phân tích số vụ tai nạn theo loại phương tiện giao thông trong từng quý của năm 2017 và 2018 
st.subheader("""
* 2.2 Phân tích số vụ tai nạn theo loại phương tiện giao thông trong từng quý của năm 2017 và 2018 *
""")
st.write(""" Nhìn tổng quan số liệu từ quý 1 năm 2017 đến quý 4 năm 2018 số vụ tai nạn giao thông do các phương tiện lớn luôn chiếm đa số. Cụ thể số liệu qua các quý cho thấy số vụ tai nạn do các phương tiện lớn luôn chiếm hơn 80%.
 """)
st.code("""df.plot(x="Quarter", y=["Town", "Village"], kind="bar",figsize=(9,5), title='The number of accident between Town and Village')
plt.xticks(rotation=30)
#ax.set_ylabel('Frequency')
plt.show() """)
x = df_select["Quarter"]
Town = df_select["Town"]
Village = df_select["Village"]
labels =["Town","Village"]
fig, ax = plt.subplots()
ax.plot(x, Town)
ax.plot(x, Village)
plt.xlabel('Quarter')
plt.ylabel('Place')
plt.title('The number of accident between Town and Village')
plt.xticks(rotation=30)
st.write(fig)
# 2.3. Phân tích số vụ tai nạn theo loại phương tiện giao thông trong từng quý của năm 2017 và 2018
st.subheader("""
*2.3. Phân tích số vụ tai nạn theo loại phương tiện giao thông trong từng quý của năm 2017 và 2018*
""")
st.write("""Nhìn tổng quan số liệu từ quý 1 năm 2017 đến quý 4 năm 2018 số vụ tai nạn giao thông do các phương tiện lớn luôn chiếm đa số. Cụ thể số liệu qua các quý cho thấy số vụ tai nạn do các phương tiện lớn luôn chiếm hơn 80% """)
st.write(""" Số vụ tai nạn giao thông đường bộ do các phương tiện lớn gây ra có sự chênh lệch đáng kể so với phương tiện nhỏ. Cụ thể, khi vào quý 1, 2, 3, 4 năm 2017 số vụ tai nạn do phương tiện lớn gấp lần lượt là 7.26, 6.30, 6.24, 5.11.""")
st.code("""
barWidth = 0.25
bars1 = df['Small Vehicle']
bars2 = df['Large Vehicle']
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
fig =plt.figure(figsize=(15,7))
plt.bar(r1, bars1, color='aquamarine', width=barWidth, edgecolor='white', label='Small Vehicle')
plt.bar(r2, bars2, color='darkslategrey', width=barWidth, edgecolor='white', label='Large Vehicle')
plt.xlabel('number of accidents by type of transport', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Q1/2017', 'Q2/2017', 'Q3/2017', 'Q4/2017',
                                                       'Q1/2018', 'Q2/2018', 'Q3/2018', 'Q4/2018'])
plt.legend()
plt.show();
""",language='python')
barWidth = 0.25
bars1 = df_select['Small Vehicle']
bars2 = df_select['Large Vehicle']
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
fig = plt.figure(figsize=(15,7))
plt.bar(x, bars1, color='aquamarine', width=barWidth, edgecolor='white', label='Small Vehicle')
plt.bar(r2, bars2, color='darkslategrey', width=barWidth, edgecolor='white', label='Large Vehicle')
plt.xlabel("Quarter")
plt.title('number of accidents by type of transport', fontweight='bold')
plt.legend(loc='right', framealpha=0, borderpad=-15, title='Note')
st.pyplot(fig)
# 2.3. Phân tích nguyên nhân gây tai nạn giao thông trong từng quý của năm 2017 và 2018
st.subheader("""
*2.3. Phân tích nguyên nhân gây tai nạn giao thông trong từng quý của năm 2017 và 2018*
""")
st.write("""
Nguyên nhân dẫn đến tai nạn giao thông thì tồn tại rất nhiều, có thể đến từ ý thức tham gia giao thông của người điều khiển hay hành khách, nhưng theo thống kê tại thành phố Mandalay thì đa phần các vụ tai nạn xảy ra đều do sự bất cẩn của người điều khiển phương tiện chiếm tới trên 85% trên các quý. Các nguyên nhân còn lại chiếm tỉ lệ rất ít so với số lượng vụ tai nạn xảy ra.
""")
st.dataframe(df_select[['Quarter', 'Drug', 'Careless Driving','Skilless Driver',
         'Racing', 'Careless Passenger','Machine Error']])
st.write("""
 Ở 4 quý năm 2017 đa phần số lượng vụ tai nạn do người điều khiển bất cẩn xảy ra nhiều nhưng vẫn có những nguyên nhân khác như sử dụng chất kích thích, sự bất cẩn của hành khách và sự cố phương tiện. Nguyên nhân sử dụng chất kích thích và sự cố phương tiện tuy chiếm tỉ lệ nhỏ nhưng đây là những vấn đề lớn và ảnh hưởng rất nhiều đến người điều khiển phương tiện cũng như tất cả những người cùng tham gia giao thông.
""")
st.code(""" 
fig = plt.figure(figsize=(5,5))
a = df['Drug']
b = df['Careless Driving']
c = df['Skilless Driver']
d = df['Racing']
e = df['Careless Passenger']
f = df['Machine Error']
g = df['Quarter']

plt.xticks(rotation=30)
plt.bar(g, a, color='#b00b0b', label='Drug', bottom=b+e+f)
plt.bar(g, b, color='#edb03e', label='Careless Driving')
plt.bar(g, c, color='#1c3c94', label='Skilless Driver', bottom=b+d)
plt.bar(g, d, color='#a38b8b', label='Racing', bottom=b)
plt.bar(g, e, color='darkslateblue', label='Careless Passenger', bottom=b)
plt.bar(g, f, color='#46d61a', label='Machine Error', bottom=b+e)
plt.xlabel("Quarter")
plt.ylabel("Main Reason")
plt.title("Main causes of accidents in 2017 and 2018")
plt.legend(loc='right', framealpha=0, borderpad=-15, title='Note')
plt.show()
""", language='python')

st.write(""" 
Vào năm 2018, trường hợp tai nạn giao thông xảy ra do sự bất cẩn của người điều khiển phương tiện vẫn không có hiện tượng giảm đi, trong khi đó các vụ tai nạn do sử dụng chất kích thích, sự cố phương tiện đã giảm đi rất nhiều và có dấu hiệu không còn, song với đó bắt đầu xuất hiện những vụ tai nạn liên quan đến đua xe trái phép. Trong một năm có đến 174 vụ tai nạn liên quan đến đua xe. Điều đó thể hiện sự suy giảm đáng kể về nhận thức của người dân khi tham gia giao thông.
""")
fig = plt.figure(figsize=(15,7))
a = df_select['Drug']
b = df_select['Careless Driving']
c = df_select['Skilless Driver']
d = df_select['Racing']
e = df_select['Careless Passenger']
f = df_select['Machine Error']
g = df_select['Quarter']

plt.xticks(rotation=30)
plt.bar(g, a, color='#b00b0b', label='Drug', bottom=b+e+f)
plt.bar(g, b, color='#edb03e', label='Careless Driving')
plt.bar(g, c, color='#1c3c94', label='Skilless Driver', bottom=b+d)
plt.bar(g, d, color='#a38b8b', label='Racing', bottom=b)
plt.bar(g, e, color='darkslateblue', label='Careless Passenger', bottom=b)
plt.bar(g, f, color='#46d61a', label='Machine Error', bottom=b+e)
plt.xlabel("Quarter")
plt.ylabel("Main Reason")
plt.title("Main causes of accidents in 2017 and 2018")
plt.legend(loc='right', framealpha=0, borderpad=-15, title='Note')
st.pyplot(fig)
st.write("""
Để giảm thiểu tối đa các nguyên nhân dẫn đến tai nạn giao thông như trên, có các giải pháp thiết thực như sau: 
- Nâng cao ý thức, hiểu biết người dân phải có trách nhiệm thực hiện nghiêm luật giao thông đường bộ, bên cạnh đó có các hình thức tuyên truyền hoặc thông tin đại chúng như: làm các bảng khẩu hiệu giao thông, các chương trình an toàn giao thông… 
- Vận động người dân tham gia giao thông bằng phương tiện giao thông công cộng để giảm thiểu mật độ tham gia giao thông.
- Tăng cường quản lý trật tự an toàn giao thông đường bộ, tiến hành xử phạt nghiêm đối với các trường hợp vi phạm.
- 
Đặt các cột đèn xanh đèn đỏ, biển cảnh báo lớn tại các tuyến đường ngã ba ngã tư nguy hiểm để người điều khiển có thể chú ý khi tham gia giao thông.
""")
# 2.4. Phân tích mức độ thương vong của tai nạn giao thông theo nhóm người trong từng quý của năm 2017 và 2018 (va chạm, bị thương, tử vong)
st.subheader("""
*2.4. Phân tích mức độ thương vong của tai nạn giao thông theo nhóm người trong từng quý của năm 2017 và 2018 (va chạm, bị thương, tử vong)*
""")
st.write("""
Nhìn chung số vụ tai nạn của cả hai nhóm thanh niên và người trưởng thành ở mức độ va chạm chiếm số lượng ít, còn mức độ bị thương và tử vong do tai nạn chiếm số lượng lớn. Và đa phần có xu hướng giảm theo từng quý trong 2 năm 2017 và 2018.
""")
st.dataframe(df_select[['Quarter', 'Youth Collision', 'Youth Death','Youth Injury',
         'Adult Collision', 'Adult Death','Adult Injury']])
st.write("""
Đối với mức độ va chạm, từ quý 1 năm 2017 đến quý 2 năm 2018, nhóm người trưởng thành có số lượng vụ tai nạn chiếm phần lớn và tăng theo từng quý (cụ thể từ 347 vụ đến 444 vụ). Tuy nhiên, từ quý 3 năm 2018 cho đến hết năm 2018 số vụ tai nạn của nhóm thanh niên chiếm số lượng lớn hơn và tăng nhanh (trên 300 vụ), còn nhóm người trưởng thành giảm đáng kể (dưới 300 vụ).
""")
st.code("""
fig = plt.figure(figsize=(14,3.5))

a1 = df['Youth Collision']
a2 = df['Youth Injury']
a3 = df['Youth Death']
b1 = df['Adult Collision']
b2 = df['Adult Injury']
b3 = df['Adult Death']
d = df['Quarter']

plt.subplot(1, 2, 1)
plt.plot(d, a1, color='#30cadb', marker='s', markersize=5, label="Youth Collision") #paper, notebook, talk, poster
plt.plot(d, a2, color='#f2f200', marker='*', markersize=10, label="Youth Injury")
plt.plot(d, a3, color='#f0764a', marker='.', markersize=10, label="Youth Death")
plt.xlabel("Quarter")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.legend(["Youth Collision", "Youth Injury", "Youth Death"], loc='upper center', framealpha=0, borderpad=-8.5, title='Note')
plt.title("Casualty levels among youth by quarters of 2017 and 2018")

plt.subplot(1, 2, 2)
plt.plot(d, b1, color='#30cadb', marker='s', markersize=5, label="Adult Collision")
plt.plot(d, b2, color='#f2f200', marker='*', markersize=10, label="Adult Injury")
plt.plot(d, b3, color='#f0764a', marker='.', markersize=10, label="Adult Death")
plt.xlabel("Quarter")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.legend(["Adult Collision", "Adult Injury", "Adult Death"], loc='upper center', framealpha=0, borderpad=-8.5, title='Note')
plt.title("Casualty levels among adults by quarters of 2017 and 2018")

plt.show()
""",language='python')
st.write("""
Đối với mức độ tai nạn bị thương, đa phần số vụ tai nạn ở nhóm người trưởng thành chiếm số lượng lớn hơn, tuy nhiên có xu hướng giảm theo từng quý. Duy chỉ quý 1 năm 2018, số vụ tai nạn ở nhóm thanh niên tăng đáng kể (cụ thể 105 vụ) lớn hơn số vụ tai nạn bên nhóm người trưởng thành. 
""")
fig = plt.figure(figsize=(14,3.5))

a1 = df_select['Youth Collision']
a2 = df_select['Youth Injury']
a3 = df_select['Youth Death']
b1 = df_select['Adult Collision']
b2 = df_select['Adult Injury']
b3 = df_select['Adult Death']
d = df_select['Quarter']

plt.subplot(1, 2, 1)
plt.plot(d, a1, color='#30cadb', marker='s', markersize=5, label="Youth Collision") #paper, notebook, talk, poster
plt.plot(d, a2, color='#f2f200', marker='*', markersize=10, label="Youth Injury")
plt.plot(d, a3, color='#f0764a', marker='.', markersize=10, label="Youth Death")
plt.xlabel("Quarter")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.legend(["Youth Collision", "Youth Injury", "Youth Death"], loc='upper center', framealpha=0, borderpad=-8.5, title='Note')
plt.title("Casualty levels among youth by quarters of 2017 and 2018")

plt.subplot(1, 2, 2)
plt.plot(d, b1, color='#30cadb', marker='s', markersize=5, label="Adult Collision")
plt.plot(d, b2, color='#f2f200', marker='*', markersize=10, label="Adult Injury")
plt.plot(d, b3, color='#f0764a', marker='.', markersize=10, label="Adult Death")
plt.xlabel("Quarter")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.legend(["Adult Collision", "Adult Injury", "Adult Death"], loc='upper center', framealpha=0, borderpad=-8.5, title='Note')
plt.title("Casualty levels among adults by quarters of 2017 and 2018")

st.pyplot(fig)

st.write("""
Đối với mức độ gây tử vong, nhìn chung số lượng vụ tai nạn của nhóm người trưởng thành chiếm số lượng lớn và tăng giảm thất thường theo từng quý, trong quý 2 năm 2018 đạt số vụ tai nạn cao nhất trong 2 năm 2017 và 2018 (711 vụ tai nạn). Còn đối với nhóm thanh niên số lượng vụ tai nạn ít hơn và giảm theo từng quý trong năm (từ quý 3 năm 2017 trở về sau). 
""")

#III.Kết luận
st.title("""
III.Kết luận
""")
st.header("""
Phần 4: Hệ quả của tai nạn giao thông đường bộ ở Mandalay (Myanmar)
""")
st.subheader("""
Hệ quả 
""")
st.write("""
Số vụ tai nạn giao thông đường bộ ngày càng tăng: 
- Đối với bản thân người bị tai nạn giao thông: 
+ Bị cướp đi mạng sống nếu nghiêm trọng, hoặc có thể gây ảnh hưởng xấu đến sức khỏe rất nhiều.
+ Ảnh hưởng trầm trọng đến tâm lý của người bị tai nạn (sợ sệt, lo lắng mỗi khi tham gia giao thông).
+ Chịu trách nhiệm bồi thường nạn nhân nếu bản thân vi phạm luật giao thông và là người gây ra tai nạn nghiêm trọng. 
- Đối với gia đình người bị tai nạn:
+ Nếu gia đình có người mất vì tai nạn giao thông thì sẽ đau đớn rất nhiều về tinh thần, mất mát của gia đình rất lớn.
+ Nếu người bị tai nạn còn sống thì gia đình tốn nhiều viện phí, thời gian chăm sóc và điều trị. 
+ Tạo tâm lý lo sợ đối với người thân trong gia đình mỗi khi tham gia giao thông đường bộ. 
- Đối với xã hội và quốc gia 
+ An toàn giao thông trong quốc gia xuống cấp.
+ Ảnh hưởng đến sự phát triển kinh tế của một quốc gia.
+ Đe dọa đến tính mạng và sức khỏe của người dân.
+ Nhiễu loạn tâm lý người dân về sự an toàn trong giao thông.
+ Gây mất trật tự xã hội và an ninh quốc gia.

""")
