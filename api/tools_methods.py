class ToolMethod:
    def __init__(self,code,name,func) -> None:
        self.code=code
        self.name=name
        self.func=func

    def run(self,params):
        return self.func(params)

def translate_sql(sql_input):
    
    translated_sql = sql_input
    
    ss = sql_input.split("\n")
    i = 0
    sql = ""
    parms = []
    
    while i < len(ss):
        if ss[i].startswith("==>  Preparing:"):
            sql = ss[i][ss[i].index(":") + 1:]
        
        if ss[i].startswith("==> Parameters:"):
            p = ss[i][ss[i].index(":") + 1:]
            parms = p.split(",")
            break
        
        i += 1
    
    # 替换 SQL 中的 ? 为 parms 中的参数
    i = 0
    while i < len(parms):
        t = parms[i][1:]
        if t.endswith("(String)"):
            sql = sql.replace("?", f"'{t[:-len('(String)')]}'", 1)
        
        if t.endswith("(Integer)"):
            sql = sql.replace("?", t[:-len('(Integer)')], 1)
        
        if t.endswith("(LocalDateTime)"):
            sql = sql.replace("?", f"'{t[:-len('(LocalDateTime)')]}'", 1)
        
        i += 1
    # SQL 格式化
    import sqlparse
    
    # 格式化 SQL
    formatted_sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
    
    # 如果需要，可以在这里添加更多的格式化逻辑
    
    return formatted_sql



def json2javabean(jsonInput):

    def map_type(json_type):
        print(json_type)
        if json_type == str:
            return "String"
        elif json_type == int:
            return "int"
        elif json_type == float:
            return "double"
        elif json_type == bool:
            return "boolean"
        elif json_type == list:
            return "List"
        elif json_type == dict:
            return "Map"
        else:
            return "Object"
    import json
    data = json.loads(jsonInput)
    
    java_class = f"import lombok.Data;\n\n@Data\npublic class FuckBean '{'{'}\n"
    
    for key, value in data.items():
        java_class += f"    private {map_type(type(value))} {key};\n"
    
    java_class += "}"
    
    return java_class
    

ToolMethods=[
    ToolMethod("MpDebug","mybatisDebug",translate_sql),
    ToolMethod("JSON2JAVABEAN","JSON转javaBean",json2javabean)

]
__all__ = ['ToolMethods']
