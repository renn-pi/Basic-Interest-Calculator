from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.graphics import Color, Rectangle


KV = '''
<FamilySavingScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 227/255,237/255,246/255, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        MDToolbar:
            title: "Family Saving Certificate"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(100)
            spacing: dp(10)
            MDTextField:
                id: amount_input
                hint_text: 'Enter deposit amount'
                input_filter: 'int'
                mode: "rectangle"
            MDRaisedButton:
                text: "Calculate"
                size_hint: None, None
                #52,29,159
                #md_bg_color: 227/255,237/255,246/255, 1
                size: dp(200), dp(50) #2nd dp is the width of button
                pos_hint: {"center_x": .5}
                on_release: root.calculate_interest()
            MDLabel:
                id: result_label
                size_hint_y: None
                height: dp(250)
#                halign: 'center'

<FiveYearScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 212/255,244/255,243/255, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        MDToolbar:
            title: "Five-Year BD Saving Certificate"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(100)
            spacing: dp(10)
            MDTextField:
                id: amount_input
                hint_text: 'Enter deposit amount'
                input_filter: 'int'
                mode: "rectangle"
            MDRaisedButton:
                text: "Calculate"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.calculate_interest()
            MDLabel:
                id: result_label
                size_hint_y: None
#                height: self.texture_size[1]
                valign: 'top'
                text_size: self.width, None
                font_size: '14sp'
                height: dp(250)
#                halign: 'center'

<QuarterlySavingScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 212/255,244/255,243/255, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        MDToolbar:
            title: "Three-Month Profit-Bearing Certificate"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(100)
            spacing: dp(10)
            MDTextField:
                id: amount_input
                hint_text: 'Enter deposit amount'
                input_filter: 'int'
                mode: "rectangle"
            MDRaisedButton:
                text: "Calculate"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.calculate_interest()
            MDLabel:
                id: result_label
                size_hint_y: None
                valign: 'top'
                text_size: self.width, None
                font_size: '14sp'
                height: dp(250)

<PensionerSavingScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 212/255,244/255,243/255, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        MDToolbar:
            title: "Pensioner Saving Certificate"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(100)
            spacing: dp(10)
            MDTextField:
                id: amount_input
                hint_text: 'Enter deposit amount'
                input_filter: 'int'
                mode: "rectangle"
            MDRaisedButton:
                text: "Calculate"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.calculate_interest()
            MDLabel:
                id: result_label
                size_hint_y: None
                valign: 'top'
                text_size: self.width, None
                font_size: '14sp'
                height: dp(250)


<InterestCalculatorMenuScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 212/255,244/255,243/255, 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        MDToolbar:
            title: "Interest Calculator"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(200)
            spacing: dp(20)
            MDRaisedButton:
                text: "             Family Saving Certificate             "
                size_hint: None, None
                size: dp(300), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.go_to_family_saving()
            MDRaisedButton:
                text: "       Five-Year BD Saving Certificate       "
                size_hint: None, None
                size: dp(300), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.go_to_five_year_saving()
            MDRaisedButton:
                text: "Three-Month Profit-Bearing Certificate"
                size_hint: None, None
                size: dp(300), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.go_to_quarterly_saving()
            MDRaisedButton:
                text: "          Pensioner Saving Certificate          "
                size_hint: None, None
                size: dp(300), dp(50)
                pos_hint: {"center_x": .5}
                on_release: root.go_to_pensioner_saving()

<MainScreen>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 212/255,244/255,243/255, 1
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        MDToolbar:
            title: "Sanchay Calculator"
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(180)
            spacing: dp(10)
            MDLabel:
                text: "Welcome to Sanchay Calculator!"
                theme_text_color: 'ContrastParentBackground'
                text_color: 1,1,1, 1
                size_hint: None, None
                pos_hint: {"center_x": .5}
#                halign: 'center'
                font_style: 'H6'
            MDRaisedButton:
                text: "Calculate Interest"
                size_hint: None, None
                size: dp(200), dp(50)
                #md_bg_color: 147/255.0, 205/255.0, 211/255.0, 1
                #md_bg_color: 227/255,237/255,246/255, 1
                pos_hint: {"center_x": .5}
                on_release: root.go_to_interest_calculator()
'''

class FamilySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_interest(self):
        amount_input = self.ids.amount_input
        result_label = self.ids.result_label
        try:
            amount = int(amount_input.text)
            result = self.calculate_family_saving_interest(amount)
            result_label.text = result
        except ValueError:
            result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_family_saving_interest(self, amount):
        def calculate_interest_family(amount, rate):
            yearly = amount * rate
            monthly = yearly / 12
            rate_src = .05 if amount <= 500000 else .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest_family(1500000, .1152)
        second_half_interest = calculate_interest_family(1500000, .1050)

        if amount <= 500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)} taka"
        elif amount <= 1500000:
            rate = .1152
            return f"Receive interest per month: {calculate_interest_family(amount, rate)} taka"
        elif amount <= 3000000:
            rate = .1050
            rest = amount - 1500000
            second_interest = calculate_interest_family(rest, rate)
            total_interest = first_half_interest + second_interest
            return ("Receive interest:\n"
                    f"on the first 15,00,000 taka: {first_half_interest}\n"
                    f"on the rest {rest} taka: {second_interest}\n"
                    "__________________\n"
                    f"Total interest per month: {total_interest} taka")
        elif amount <= 4500000:
            rate = .0950
            rest_over = amount - 3000000
            third_interest = calculate_interest_family(rest_over, rate)
            total_interest = first_half_interest + second_half_interest + third_interest
            return ("Receive interest:\n"
                    f"on the first 15,00,000 taka: {first_half_interest}\n"
                    f"on the second 15,00,000 taka: {second_half_interest}\n"
                    f"on the rest {rest_over} taka: {third_interest}\n"
                    "___________________\n"
                    f"Total interest per month: {total_interest} taka")
        else:
            return ("Individual deposit amount exceeded for this scheme.\n"
                    "Please input any amount up to 45,00,000 taka and try again.")

    def go_back(self):
        self.manager.current = 'interest_calculator_menu'

class FiveYearScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_interest(self):
        amount_input = self.ids.amount_input
        result_label = self.ids.result_label
        try:
            amount = int(amount_input.text)
            result = self.calculate_five_year_interest(amount)
            result_label.text = result
        except ValueError:
            result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_five_year_interest(self, amount):
        def calculate_interest_yearly(amount, rate):
            yearly_interest = amount * rate
            if amount <= 500000:
                rate_src = .05
            elif amount > 500000 :
                rate_src = .10
            tax = yearly_interest * rate_src
            interest = yearly_interest - tax
            return interest

        first_half_interest = calculate_interest_yearly(1500000, .1128)
        second_half_interest = calculate_interest_yearly(1500000, .1030)

        if amount <= 500000 :
            rate = .1128
            return f"Receive interest per year: {calculate_interest_yearly(amount, rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1128
            return f"Receive interest per year: {calculate_interest_yearly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 : # up to 3 lacs
            rate = .1030
            rest = amount - 1500000
            second_interest = calculate_interest_yearly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    "______________\n"
                    f"Total interest every year: {first_half_interest + second_interest}\n")

        elif amount > 3000000 and amount <= 6000000:
            rate = .0930

            rest_1 = amount - 3000000
            third_interest = calculate_interest_yearly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    "________________\n"
                    f"Total interest every year: {first_half_interest + second_half_interest + third_interest}\n"
                    f"_______________\n"
                    f" Note:Individual deposit limit exceeded.\n")

        elif amount > 6000000 and amount <= 500000000:
            rate = .0930

            rest_1 = amount - 3000000
            third_interest = calculate_interest_yearly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    "_______________\n"
                    f"Total interest every year: {first_half_interest + second_half_interest + third_interest}\n"
                    f"_______________\n"
                    f"Note: Individual and Joint deposit amount exceeded for this scheme.\n")

        else:
            return ("Investment amount exceeded for this scheme.\n"
                    "Please input any amount up to 3,000,000 taka for individual,\n"
                    "or up to 6,000,000 taka for joint investments,\n"
                    "or up to 50,000,000 taka for companies and try again.\n")

    def go_back(self):
        self.manager.current = 'interest_calculator_menu'

class QuarterlySavingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_interest(self):
        amount_input = self.ids.amount_input
        result_label = self.ids.result_label
        try:
            amount = int(amount_input.text)
            result = self.calculate_quarterly_interest(amount)
            result_label.text = result
        except ValueError:
            result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_quarterly_interest(self, amount):
        def calculate_interest_quarterly(amount, rate):
            yearly = amount * rate
            monthly = yearly / 4
            if amount <= 500000:
                rate_src = .05
            elif amount > 500000 :
                rate_src = .10
            tax = monthly * rate_src
            interest = monthly - tax
            return interest

        first_half_interest = calculate_interest_quarterly (1500000,.1104)
        second_half_interest = calculate_interest_quarterly (1500000,.10)


        if amount <= 500000 :
            rate = .1104
            return f"Receive interest every three months: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1104
            return f"Receive interest every three months: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 :
            rate = .10
            #return
            rest = amount - 1500000
            second_interest = calculate_interest_quarterly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    "_________________\n"
                    f"Total interest every three months: {first_half_interest + second_interest}\n")

        elif amount > 3000000 and amount <= 6000000 :
                rate = .09
                rest_1 = amount - 3000000
                third_interest = calculate_interest_quarterly(rest_1,rate)
                return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                        f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                        f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                        "________________\n"
                        f"Total interest every three months: {first_half_interest + second_half_interest + third_interest}\n"
                        f"________________\n"
                        f"Note:Individual deposit limit exceeded.\n")

        elif amount > 6000000 and amount <= 500000000:
            rate = .09
            rest_1 = amount - 3000000
            third_interest = calculate_interest_quarterly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                    f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                    "_________________\n"
                    f"Total interest every three months: {first_half_interest + second_half_interest + third_interest}\n"
                    f"_________________\n"
                    f"Note: Individual and Joint deposit amount exceeded for this scheme.\n")

        else:
            return ("Investment amount exceeded for this scheme.\n"
                    "Please input any amount up to 3,000,000 taka for individual,\n"
                    "or up to 6,000,000 taka for joint investments,\n"
                    "or up to 50,000,000 taka for companies and try again.\n")

    def go_back(self):
        self.manager.current = 'interest_calculator_menu'

class PensionerSavingScreen(Screen): #same as QuarterlySavingScreen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_interest(self):
        amount_input = self.ids.amount_input
        result_label = self.ids.result_label
        try:
            amount = int(amount_input.text)
            result = self.calculate_pensioner_interest(amount)
            result_label.text = result
        except ValueError:
            result_label.text = "Invalid input. Please enter a valid amount."

    def calculate_pensioner_interest(self, amount):
        def calculate_interest_quarterly(amount, rate): #kept same as quarterly
            yearly = amount * rate
            three_months = yearly / 4
            if amount <= 500000:
                interest = three_months #[no tax taken for amount up to 5,00,000 taka]
                return interest
            elif amount > 500000 :
                rate_src = .10
            tax = three_months * rate_src
            interest = three_months - tax
            return interest

        first_half_interest = calculate_interest_quarterly (1500000,.1176)
        second_half_interest = calculate_interest_quarterly (1500000,.1075)


        if amount <= 500000 :
            rate = .1176
            return f"Receive interest every three months: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 500000 and amount <= 1500000 :
            rate = .1176
            return f"Receive interest every three months: {calculate_interest_quarterly(amount,rate)}"

        elif amount > 1500000 and amount <= 3000000 :
            rate = .1075
            #
            rest = amount - 1500000
            second_interest = calculate_interest_quarterly(rest,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                    f"Receive interest on the rest {rest} taka: {second_interest}\n"
                    "_______________\n"
                    f"Total interest every three months: {first_half_interest + second_interest}\n")

        elif amount > 3000000 and amount <= 5000000 :
            rate = .0975
            #
            rest_1 = amount - 3000000
            third_interest = calculate_interest_quarterly(rest_1,rate)
            return (f"Receive interest on the first 15,00,000 taka: {first_half_interest}\n"
                   f"Receive interest on the second 15,00,000 taka: {second_half_interest}\n"
                   f"Receive interest on the rest {rest_1} taka: {third_interest}\n"
                   "_________________\n"
                   f"Total interest every three months: {first_half_interest + second_half_interest + third_interest}\n")

        elif amount > 5000000 :
            return ("Deposit limit exceeded.\n"
                   "Please input any amount up to 5000000 taka and try again.\n")

    def go_back(self):
        self.manager.current = 'interest_calculator_menu'

class InterestCalculatorMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_family_saving(self):
        self.manager.current = 'family_saving'

    def go_to_five_year_saving(self):
        self.manager.current = 'five_year_saving'

    def go_to_quarterly_saving(self):
        self.manager.current = 'quarterly_saving'

    def go_to_pensioner_saving(self):
        self.manager.current = 'pensioner_saving'

    def go_back(self):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_interest_calculator(self):
        self.manager.current = 'interest_calculator_menu'

class SavingsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo" #'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
        #'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        #'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Light"
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(InterestCalculatorMenuScreen(name='interest_calculator_menu'))
        sm.add_widget(FamilySavingScreen(name='family_saving'))
        sm.add_widget(FiveYearScreen(name='five_year_saving'))
        sm.add_widget(QuarterlySavingScreen(name='quarterly_saving'))
        sm.add_widget(PensionerSavingScreen(name='pensioner_saving'))
        return sm

if __name__ == '__main__':
    SavingsApp().run()
