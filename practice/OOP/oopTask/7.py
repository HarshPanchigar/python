class UPIPayment:
    def pay(self):
        print("Paid using UPI")
class CardPayment:
    def pay(self):
        print("Paid using Card")
class NetBankingPayment:
    def pay(self):
        print("Paid using Net Banking")

# upi = UPIPayment()
# card = CardPayment()
# netBank = NetBankingPayment()

# payments = [upi,card,netBank]
payments = [UPIPayment(), CardPayment(), NetBankingPayment()]


for payment in payments:
    payment.pay()