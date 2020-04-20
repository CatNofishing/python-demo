import os,shutil
import sqlite3

class edit:
    def __init__(self,txt_path,new_dirname,origion_dirname,database_name):
        print('开始')
        if os.path.isdir(new_dirname):
            pass
        else:
            os.mkdir(new_dirname)
        self.data=self.get_data(txt_path)
        self.create_database(database_name,self.data)
        self.initial_dir(new_dirname,database_name)
        self.copy_file_newpath(origion_dirname,new_dirname,database_name)
        print('数据处理完毕！')


    #根据txt文件获取文件路径数据
    def get_data(self,filepath):
        with open(filepath,'r') as f:
            data=f.readlines()
            print('总长是',len(data))
            for i in range(len(data)):
                data[i]=data[i].strip().split()
        del_index=[]
        for i in range(len(data)):
            try:
                id=int(data[i][0])
                dirpath=os.path.dirname(data[i][1])
                filename=os.path.basename(data[i][1])
                data[i]=[id,dirpath,filename]
            except:
                del_index.append(data[i])
        for i in del_index:
            data.remove(i)
        print('去重后总长是',len(data))
        return data

    #将文件路径数据存储到数据库
    def create_database(self,database_name,data):
        if os.path.isfile(database_name):
            print('数据库已经存在！')
            return
        else:
            conn=sqlite3.connect(database_name)
            cursor=conn.cursor()
            sql1='''
            create table filepath(
                id int,
                dirpath varchar,
                filename varchar
            );
            '''
            cursor.execute(sql1)
            sql='''insert into filepath values (?,?,?)'''
            for i in range(len(data)):
                cursor.execute(sql,(data[i][0],data[i][1],data[i][2]))
            conn.commit()
            cursor.close()
            conn.close()
            print('数据库创建成功！')


    #创建文件夹目录
    def initial_dir(self,dirname,database_name):
        conn=sqlite3.connect(database_name)
        cursor=conn.cursor()
        sql="select distinct dirpath from filepath"
        count=cursor.execute(sql)
        dirpath=count.fetchall()
        cursor.close()
        conn.close()
        dirpath=list(map(lambda x:x[0],dirpath))
        dirpath.sort(key=lambda x:len(x))
        error=0
        for i in range(len(dirpath)):
            try:
                os.makedirs(os.path.join(dirname,dirpath[i]))
            except:
                error+=1
        print('错误次数',error)

    #复制文件到指定目录并更改名称
    def copy_file_newpath(self,origion_dirname,new_dirname,database_name):
        file_list=os.listdir(origion_dirname)
        file_list=list(map(lambda x:int(x),file_list))
        conn=sqlite3.connect(database_name)
        cursor=conn.cursor()
        sql='select distinct dirpath,filename from filepath where id=?'
        for id in file_list:
            count=cursor.execute(sql,(id,))
            new_path=count.fetchone()
            shutil.copy(os.path.join(origion_dirname,str(id)),os.path.join(new_dirname,new_path[0]+'/'+new_path[1]))
        cursor.close()
        conn.close()

if __name__=='__main__':
    egg=edit('1.txt','新数据','FL','data.db')