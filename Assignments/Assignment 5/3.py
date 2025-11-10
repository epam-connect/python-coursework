
class UserNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
    

class NoOrdereFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeTotalException(Exception):
    def __init__(self, message):
        super().__init__(message)
    

class UserReportController: 
    def __init__(self): 
        self._user_report_builder = None 
    
    @property 
    def user_report_builder(self): 
        return self._user_report_builder 
    
    @user_report_builder.setter 
    def user_report_builder(self, value): 
        self._user_report_builder = value
    
    def get_user_total_order_amount_view(self, user_id, model): 
        total_message = self.get_user_total_message(user_id) 
        if total_message is None: 
            return "technicalError" 
        
        model.add_attribute("userTotalMessage", total_message) 
        
        return "userTotal" 
    
    def get_user_total_message(self, user_id): 
        amount = self._user_report_builder.get_user_total_order_amount(user_id) 
        
        return "User Total: {0}$".format(amount)
    

class UserReportBuilder: 
    def __init__(self): 
        self._user_dao = None 

    @property 
    def user_dao(self): 
        return self._user_dao 
    
    @user_dao.setter 
    def user_dao(self, value): 
        self._user_dao = value 
    
    def get_user_total_order_amount(self, user_id): 
        if self.user_dao is None: 
            return None 
        user = self.user_dao.get_user(user_id) 
            
        if user is None: 
            raise UserNotFoundException("WARNING: User ID doesn't exist.") 
            
        orders = user.get_all_orders() 
        if len(orders) == 0: 
            raise NoOrdereFoundException("WARNING: User have no submitted orders.")
        
        result = 0.0 

        for order in orders: 
            if order.is_submitted(): 
                total = order.total()  
                if total < 0: 
                    raise NegativeTotalException("ERROR: Wrong order amount.")
                
            result += total

        return result