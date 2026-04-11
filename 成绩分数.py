import time
yv_wen=12
shu_xue=35
ying_yv=26
print(f"姓名\t语文\t数学\t英语\n张\t{yv_wen}\t{shu_xue}\t{ying_yv}")
qw=yv_wen+shu_xue+ying_yv
time.sleep(1)
print(f"总分"+f"\t{qw}")
print(f"平均分{qw/3:.2f}")