# -*- coding: utf-8 -*-

file_path = 'config/'
file_name = 'itemFinder.json'
Prefix = '!!find'
helpmsg = '''§b----ItemFinder----§r
''' + Prefix + ''' | 显示帮助信息
''' + Prefix + ''' 物品名 | 查看位置
''' + Prefix + ''' 物品名 -d | 全局模糊查询
【点击坐标可高亮显示】
'''


def search_item(search_name):
    with open(file_path + file_name, 'r', encoding='utf-8') as f:
        for line in f:
            (name, usual_name, x, y, z) = line.strip().split()
            if (search_name in usual_name.split('|')) or (search_name == name):
                return [x, y, z, name]
        return None


def search_item_d(search_name):
    list = []
    with open(file_path + file_name, 'r', encoding='utf-8') as f:
        for line in f:
            (name, usual_name, x, y, z) = line.strip().split()
            if search_name in name:
                list.append([x, y, z, name])
            else:
                for each in usual_name.split('|'):
                    if search_name in each:
                        list.append([x, y, z, name])
                        break
        if not list:
            return None
        else:
            return list


def deal_msg(server, info, result, search_name):
    if result is None:
        server.tell(info.player, '未找到' + info.content.split()[1])
        server.tell(info.player, '尝试模糊搜索')
        result_d = search_item_d(search_name)
        deal_msg_d(server, info, result_d)
    else:
        server.tell(info.player, result[3] + '在[x:' + result[0] + ',y:' + str(int(result[1])-1) + ',z:' + result[2] + ',dim:0]')


def deal_msg_d(server, info, result):
    if result is None:
        server.tell(info.player, '未找到' + info.content.split()[1])
    else:
        for each in result:
            server.tell(info.player, each[3] + '在[x:' + each[0] + ',y:' + str(int(each[1]) - 1) + ',z:' + each[
                2] + ',dim:0]')


def on_info(server, info):
    if info.is_player:
        if info.content.startswith(Prefix):
            if len(info.content.split(' ')) == 2:
                if info.content == '!!find ten_miles_away':
                    server.say('在你心里鸭 (›´ω`‹ )')
                else:
                    search_name = info.content.split()[1]
                    result = search_item(search_name)
                    deal_msg(server, info, result, search_name)
            elif info.content == Prefix:
                for line in helpmsg.splitlines():
                    server.tell(info.player, line)
            elif len(info.content.split(' ')) == 3 and info.content.split()[2] == '-d':
                search_name = info.content.split()[1]
                result = search_item_d(search_name)
                deal_msg_d(server, info, result)
            else:
                server.tell(info.player, '输入错误 !!find查看帮助')


def on_load(server, old_module):
    add_help_message(Prefix, '查找物品位置')
