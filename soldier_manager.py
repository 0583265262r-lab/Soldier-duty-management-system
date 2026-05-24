import utils,data


def add_soldier(soldier_id: int, name: str,soldiers) -> None:
    """
    מוסיפה חייל חדש למערכת.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        name (str): שם החייל
    
    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception
    
    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין
    
    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    unique_id=utils.find_soldier_by_id(soldier_id,soldiers)
    if unique_id is not None:
         raise ValueError(f"ERROR the ID is already exist")
    if not utils.is_valid_name(name):
         raise  ValueError(f"ERROR the name is not valid ")
         


  
                
    soldiers.append({"id":soldier_id,"name":name.strip(),"duties":[]})

        
        
        




def remove_soldier(soldier_id: int,soldiers) -> None:
    """
    מסירה חייל מהמערכת לפי id.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    unique_id=utils.find_soldier_by_id(soldier_id,soldiers)
    if unique_id is None:
         raise KeyError(f"ERROR the ID is not exist")
    soldiers.remove(unique_id)
    


def get_all_soldiers(soldiers) -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת: כלום
    
    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים
    
    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)
    
    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    return soldiers
