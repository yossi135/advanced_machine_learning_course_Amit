def read_text_file (file_path):
    try:
      with open(file_path,'r') as file :
         return file.read()
    except FileNotFoundError:
        print('this file is not found') 
    except IOError:
        print('Error: An I/O error occurred while reading the file.')    
class extractor:
    
    def __init__(self,file_path):
        self.file_path=file_path
        self.usernames={}
        
    def extractor_username(self):
        content=read_text_file(self.file_path)
        
        if "Error" in content:
          return content  # إعادة رسالة الخطأ مباشرةً
        
        # تقسيم المحتوى إلى أسطر
        lines = content.splitlines()
        
        # تكرار لكل سطر في المحتوى
        for line in lines:
            if ':' in line:
                # تقسيم السطر إلى اسم المستخدم وكلمة المرور بناءً على النقطتين
                username, _ = line.split(":", 1)
                # إضافة اسم المستخدم كقيمة فريدة في القاموس
                self.usernames[username] = None

        return self.usernames         