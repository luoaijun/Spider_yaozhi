from hospital_yaozhi.common import Bean
from hospital_yaozhi.common import Dao

i = 0


def save(dao: Dao.Hospital):
    global i
    i+=1
    cursor = Bean.MYSQLCONN.cursor()
    sql = "insert into pachong.HospitalsInfo(HospitalName,HosAliasName,HospitalLevel,HospitalType,Provice,City,Count,HospitalAdress,HospitalCreateYear,HospitalCharer,HospitalMethod,OutpatientVolume,HospitalDepartments,Email,ZipCode,HospitalWebsite) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    try:
        cursor.execute(
            'INSERT INTO pachong.HospitalsInfo (HospitalName,'
            'HosAliasName,'
            'HospitalLevel,'
            'HospitalType,'
            'Provice,'
            'City,'
            'Count,'
            'HospitalAdress,'
            'HospitalCreateYear,'
            'HospitalCharer,'
            'HospitalMethod,'
            'OutpatientVolume,'
            'HospitalDepartments,'
            'Email,'
            'ZipCode,'
            'HospitalWebsite)'
            'VALUES(%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)'
            % (dao.HospitalName,
               dao.HosAliasName,
               dao.HospitalLevel,
               dao.HospitalType,
               dao.Provice,
               dao.City,
               dao.Count,
               dao.HospitalAdress,
               dao.HospitalCreateYear,
               dao.HospitalCharer,
               dao.HospitalMethod,
               dao.OutpatientVolume,
               dao.HospitalDepartments,
               dao.Email,
               dao.ZipCode,
               dao.HospitalWebsite))
        Bean.MYSQLCONN.commit()  # 不执行不能插入数据
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()

