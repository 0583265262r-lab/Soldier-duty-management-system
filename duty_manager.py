import utils
def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str,soldiers) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    exist_soldier=utils.find_soldier_by_id(soldier_id,soldiers)
    if exist_soldier == None:
        raise KeyError(f"the soldier not exist")
    exist_duty=utils.find_duty_by_name(exist_soldier["duties"],duty_name)
    if exist_duty != None:
        raise ValueError(f"the duty already exist")
    valid_day= utils.is_valid_day(day,utils.VALID_DAYS)
    if not valid_day:
        raise ValueError(f"Error illegal day")
    exist_soldier["duties"].append({"name":duty_name,"day":day,"status":"pending"})
    index_current_soldier=soldiers.index(exist_soldier)
    soldiers[index_current_soldier]=exist_soldier
    
    
    
    
        
    
    
    


def update_duty_status(soldier_id: int, duty_name: str, new_status: str,soldiers) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    exist_soldier=utils.find_soldier_by_id(soldier_id,soldiers)
    if exist_soldier == None:
        raise KeyError(f"the soldier not exist")
    exist_duty=utils.find_duty_by_name(exist_soldier["duties"],duty_name)
    if exist_duty == None:
        raise ValueError(f"the duty already exist")
    valid_status= utils.is_valid_status(new_status,utils.VALID_STATUS)
    if not valid_status:
        raise ValueError(f"Error illegal new status")
    for d in exist_soldier["duties"]:
        if d["name"]==duty_name:
           d["status"]=new_status
    index_current_soldier=soldiers.index(exist_soldier)
    soldiers[index_current_soldier]=exist_soldier 

    


def get_soldier_duties(soldier_id: int,soldiers) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    exist_soldier=utils.find_soldier_by_id(soldier_id,soldiers)
    if exist_soldier == None:
        raise KeyError(f"the soldier not exist")
    return exist_soldier["duties"]
    pass