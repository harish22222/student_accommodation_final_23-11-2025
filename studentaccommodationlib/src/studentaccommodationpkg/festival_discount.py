class FestivalDiscountLib:
    
    def apply_discount(self, amount, discount_percentage):
        
        try:
            
            amount = float(amount)
            discount_percentage = float(discount_percentage)

        
            if not (0 <= discount_percentage <= 100):
                raise ValueError("Discount percentage must be between 0 and 100.")

            # Apply discount
            discount = (discount_percentage / 100) * amount
            final_amount = round(amount - discount, 2)

            return final_amount

        except Exception as e:
            print(f"❌ Error applying discount: {e}")
            return amount  