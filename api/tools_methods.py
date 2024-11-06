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
def generate_ddl_from_java_bean(java_bean_code):
    """
    Generates MySQL DDL from a given Java Bean code.
    """
    import re
    import textwrap

    # Extract class name from Java Bean code
    class_name_match = re.search(r"public class (\w+)", java_bean_code)
    if class_name_match:
        class_name = class_name_match.group(1)
    else:
        raise ValueError("Failed to extract class name from Java Bean code.")

    # Convert camel case to underscore for table name
    table_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()

    # Initialize DDL
    ddl = f"CREATE TABLE IF NOT EXISTS {table_name} (\n    id BIGINT PRIMARY KEY AUTO_INCREMENT\n);\n\n"

    # Extract fields and their comments from Java Bean code
    # 使用正则表达式匹配注释和字段
    field_pattern = r"/\*\*\s*\*\s*(.*?)\s*\*/\s*private\s+(\w+)\s+(\w+);"
    fields = re.findall(field_pattern, java_bean_code, re.DOTALL)

    # Generate ALTER TABLE statements for each field
    for comment, field_type, field_name in fields:
        # Clean up comment by removing * and extra spaces
        comment = comment.strip().replace('*', '').strip()
        if not comment:
            comment = "123"  # 如果没有注释就使用默认值
            
        # Convert field name to underscore
        field_name_underscore = re.sub(r'(?<!^)(?=[A-Z])', '_', field_name).lower()
        
        # Map Java types to MySQL types
        if field_type in ["String"]:
            mysql_type = "VARCHAR(64)"
        elif field_type == "BigDecimal":
            mysql_type = "DECIMAL(10, 4)"
        else:
            mysql_type = field_type.lower()
            
        # Add ALTER TABLE statement
        ddl += f"ALTER TABLE {table_name} ADD COLUMN {field_name_underscore} {mysql_type} NULL COMMENT '{comment}';\n"

    return textwrap.dedent(ddl)



ToolMethods=[
    ToolMethod("MpDebug","mybatisDebug",translate_sql),
    ToolMethod("JSON2JAVABEAN","JSON转javaBean",json2javabean),
    ToolMethod("JAVABEAN TO DDL","java Bean 转 DDL",generate_ddl_from_java_bean),

]
__all__ = ['ToolMethods']
