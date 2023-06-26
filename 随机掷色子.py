import numpy as np
import pandas as pd
import easygui
import matplotlib.pyplot as plt

ip = int(easygui.enterbox("你想掷几次色子:", title="随机掷色子"))
df = np.random.randint(1, 7, ip)
fg = pd.Series(df)
a = fg.value_counts()
b = fg.mean()
a.plot(kind='pie', figsize=(6, 6), fontsize=14, autopct='%1.1f%%', ylabel='')
plt.title(f"The average is(平均值是){b}", fontproperties='SimHei')
plt.savefig('F:\\jie\\程序输出结果\\掷色子图像.jpg', bbox_inches='tight')
easygui.msgbox(f"平均值是{b}", title="随机掷色子")
plt.show()
# 一共14行代码
