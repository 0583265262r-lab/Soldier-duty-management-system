#------utils.py---------
def valid_id():
    # input of id number
    # exception of ValueError
    # use function unique_id()
    # return id
    pass

def valid_name():
    # input privet name
    # exception of ValueError if name ia empty 
    # return name
    pass

def unique_id(id,soldiers):

    # arg id: valid_id()
    # arg soldiers: all soldiers id
    # return True if id exists 
    #        else False
    pass

# ---------soldiers_manager.py-------
def add_soldiers():
    # call: input id:valid_id()
    #       input name:valid_name()
    # return dictionary {soldier_id:{name:soldier_name,duties:{name_duty:{day:day, status:status}}} }
    pass

def remove_soldier():
    # input id
    # call func unique_id()
    # in not exists exception KeyError
    # if exists del soldiers from soldiers list
    pass

def print_soldiers(soldiers):
    # print soldiers
    pass


# ---------duty_manager.py---------

def input_valid_day(days:list):
    # input:day
    # arg:list of days
    # check if day not in days 
            # exception ValueError
            # else return day 
    pass
def input_valid_duty_name():
    # input duty
    # check if not srt 
            # exception ValueError
            # else return duty name

    pass
def existing_duty(soldier_id,soldiers:dict,duty_name):
    # arg:soldier_id:id
    #     soldiers:dict of all soldiers
    #     duty_name:name of duty
    # check if not exist return False
    #       else return True
    pass
def add_duty():
    # call: func valid_id()
    #       func input_valid_duty_name()
    #       func input_valid_day()
    #       func existing_duty()
    #            if True update 
    #            else ValueError
    # default status : "pending"
    pass
def input_valid_status(available_status:list):
    # arg: list of available status
    # input status
    # check if in available_status
    #       return name of status
    #       else ValueError
    pass
def update_status(soldiers:dict):
    # arg:  soldiers:dict of all soldiers
    # call: func valid_id()
    # call: func input_valid_duty_name()
    # call: func existing_duty()
            # if True call func input_valid_status() and update the status
            # if False KeyError
    pass
def view_soldier_duties(soldiers:dict):
    # arg:  soldiers:dict of all soldiers
    # call: func valid_id()
    # print: soldier info of is duties
    pass
# =============main.py==========
def main_menu():
    '''
    print:
    1) ADD SOLDIER TO SYSTEM
    2) REMOVE SOLDIER FROM SYSTEM
    3) SHOW ALL SOLDIER
    4) ADD DUTY TO SOLDIER
    5) AUPDATE DUTY STATUS
    6) SHOW ALL SOLDIER DUTIES
    input: user choice
    call all functions by user choice 
    '''
    pass
    
    
    








