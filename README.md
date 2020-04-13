# itemFinder

一个方便服务器玩家在全物品中查找特定物品位置的插件

仅支持 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

支持精确搜索与模糊搜索

支持中英文


# 格式说明

`!!find` 显示帮助信息

`!!find 物品名` 查找对应物品位置[未查询到自动模糊查询]

`!!find 物品名 -d` 模糊查询

# 配置文件

官方名 常用名1|常用名2|...|常用名n x y z

例如：

`金合欢木告示牌 合金欢木告示牌|金合欢告示牌|合金欢告示牌 -1556 41 -62`

`轻质测重压力板 light_weighted_pressure_plate|金压力板|金测重压力板 -1595 41 -85`

配置文件目录 `MCDR/config/itemFinder.json`

# 使用示例

`!!find 金压力板`

`!!find 压力板 -d`

# 输出示例

`轻质测重压力板在[x:-1595,y:40,z:-85,dim:0]`

点击坐标可在小地图内显示
