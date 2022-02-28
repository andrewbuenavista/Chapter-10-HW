class Procedure:

    def __init__(self,name,date,practitioner,charge,patient_id):

        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        self.__patient_id = patient_id
    
    def get_name(self):
        return self.__name
    
    def get_date(self):
        return self.__date
    
    def get_practitioner(self):
        return self.__practitioner
    
    def get_chrage(self):
        return self.__charge

    def get_id(self):
        return self.__patient_id