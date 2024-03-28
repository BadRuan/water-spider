from tool.apiTool import ApiTool 

if __name__ == '__main__':
    api = ApiTool()
    l = api.getData('GetLyOrProviceSQBriefing', '202403270800')
    print(l)