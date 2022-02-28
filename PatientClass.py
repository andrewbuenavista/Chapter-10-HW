class Patient:
    def __init__(self,ID,name,address,phone,veteran_status):

        self.__id = ID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__vet = veteran_status
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def get_vet(self):
        return self.__vet
    
    