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
        t = parms[i]
        if t.endswith("(String)"):
            sql = sql.replace("?", f"'{t[:-len('(String)')]}'", 1)
        
        if t.endswith("(Integer)"):
            sql = sql.replace("?", t[:-len('(Integer)')], 1)
        
        if t.endswith("(LocalDateTime)"):
            sql = sql.replace("?", f"'{t[:-len('(LocalDateTime)')]}'", 1)
        
        i += 1
    
    return sql

ToolMethods=[
    ToolMethod("md5","md5转换",lambda x: x+"md5"),
    ToolMethod("MpDebug","mybatisDebug",translate_sql),
    ToolMethod("大写","大写",lambda x: x.upper())
]
__all__ = ['ToolMethods']
