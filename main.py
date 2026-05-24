import data,soldier_manager,duty_manager



def show_menu() -> None:
    """

    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    והפרדה בין הצגת התפריט לבין הלוגיקה  
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("ADD SOLDIER   1\n" \
          "REMOVE SOLDIER   2\n" \
          "SHOW SOLDIERS   3\n" \
          "ADD DUTY    4\n" \
          "UPDATA DUTY TO SOLDIER   5   \n" \
          "SHOW SOLDIER DUTY   6\n" \
          "EXIT   7")



def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    get_user_choice=input("Please select an option (1-7): ").strip()
    return get_user_choice

        
    


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """

    try:
        soldier_id=int(input("please enter id: "))
        soldier_name=input("please enter name: ")
        soldier_manager.add_soldier(soldier_id,soldier_name,data.soldiers)
        print(f"Soldier {soldier_name} has been successfully added to the system!")
    except ValueError as e:
        print(f"Error input {e}")


    # pass


def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    משתמש בפונקציה remove_soldier()
    """
    try:
        soldier_id=int(input("please enter id: "))
        soldier_manager.remove_soldier(soldier_id,data.soldiers)
        print("The soldier was successfully removed from the system.")
    except ValueError as e:
        print(f"Error input {e}")
    except KeyError as e:
        print(f"ERROR {e}")
        

    # pass


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    print("\n--- List of soldiers ---")
    handle_view_soldiers=soldier_manager.get_all_soldiers(data.soldiers)
    print(handle_view_soldiers)

    # pass


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id=int(input("please enter id: "))
        duty_name=input("please enter a duty: ")
        day=input("please enter a day: ")
        duty_manager.add_duty_to_soldier(soldier_id,duty_name,day,data.soldiers)
    except ValueError as e:
        print(f" ERROR {e}")
    except KeyError as e:
        print(f"ERROR {e}")
    # pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id=int(input("please enter id: "))
        duty_name=input("please enter a duty :").strip()
        new_status=input("please enter a new status: ").strip()
        duty_manager.update_duty_status(soldier_id,duty_name,new_status,data.soldiers)
    except ValueError as e:
        print(f"error {e}")
    except KeyError as e:
        print(f" error {e}")



    # pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:

        soldier_id=int(input("please enter id: "))
        print(f"\n--- Duty for soldier {soldier_id} ---")
        print(duty_manager.get_soldier_duties(soldier_id,data.soldiers))
    
    except ValueError as e:
        print(f"error {e}")
    except KeyError as e:
        print(f" error {e}")

    # pass


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while True:
        show_menu()
        user_choice=get_user_choice()
        
        if user_choice == "1":
            handle_add_soldier()
        if user_choice == "2":
            handle_remove_soldier()
        if user_choice =="3":
            handle_view_soldiers()
        if user_choice == "4":
            handle_add_duty()
        if user_choice =="5":
            handle_update_duty_status()
        if user_choice == "6":
            handle_view_soldier_duties()
        if user_choice == "7":
            print("\n Logging out")
            break
        else:
            print("invalid input please enetr number between 1-7 ")

if __name__ == "__main__":
    main()
    # pass