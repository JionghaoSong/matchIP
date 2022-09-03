一个离线IP地址定位库和IP定位数据管理框架<br>
根据 https://github.com/lionsoul2014/ip2region/tree/master/binding/python 经行了简化操作，需要去main里面指定CSV的路径
TODO：直接写入到Excel，现在只是打印输出

每个 ip 数据段的 region 信息都固定了格式：`国家|区域|省份|城市|ISP`<br>
只有中国的数据绝大部分精确到了城市，其他国家部分数据只能定位到国家，后前的选项全部是。<br><br>
![1](https://user-images.githubusercontent.com/64049788/187949842-7d837c34-0079-42d4-832c-2fb5d3f86c50.png)<br><br>
![2](https://user-images.githubusercontent.com/64049788/187949851-b050f69d-21ee-43b1-8361-7e20392639de.png)
