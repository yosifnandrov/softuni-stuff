from typing import List


class Gym:
    customers: List
    trainers: List
    equipment: List
    plans: List
    subscriptions: List

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self,customer: "Customer"):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self,trainer: "Trainer"):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_plan(self,plan:"ExercisePlan"):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_equipment(self,equipment: "Equipment"):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_subscription(self,subscription: "Subscription"):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id:int):
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                for customer in self.customers:
                    if customer.id == subscription.customer_id:
                        for trainer in self.trainers:
                            if trainer.id == subscription.trainer_id:
                                for plan in self.plans:
                                    if plan.trainer_id == trainer.id:
                                        for equipment in self.equipment:
                                            if equipment.id == plan.equipment_id:
                                                return f"{str(subscription)}\n" \
                                                       f"{str(customer)}\n" \
                                                       f"{str(trainer)}\n" \
                                                       f"{str(equipment)}\n" \
                                                       f"{str(plan)}"




