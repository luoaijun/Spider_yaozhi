class Hospital(object):
    def __init__(self):
        self.HospitalName = ""
        self.HosAliasName = ""
        self.HospitalLevel = ""
        self.HospitalType = ""
        self.Provice = ""
        self.City = ""
        self.Count = ""
        self.HospitalAdress = ""
        self.HospitalCreateYear = ""
        self.HospitalCharer = ""
        self.HospitalMethod = ""
        self.OutpatientVolume = ""
        self.HospitalDepartments = ""
        self.Email = ""
        self.ZipCode = ""
        self.HospitalWebsite = ""

    def __str__(self) -> str:
        return "医院名称:" + self.HospitalName + "\n医院别名:" + self.HosAliasName + "\n医院等级" + self.HospitalLevel + "\n医院类型" + self.HospitalType + "\n省" + self.Provice + "\n市" + self.City + "\n县" + self.Count + "\n医院地址" + str(self.HospitalAdress)
