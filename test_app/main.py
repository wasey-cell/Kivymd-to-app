from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog  
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton,MDFillRoundFlatIconButton
from kivymd.toast import toast
import random 

#this will inherit properties of button and extend the function of image 
class CllickableImage(ButtonBehavior, Image):
    #This is for the deck cards to call deck_press
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (150, 130)
        self.keep_ratio = False
        
    def on_press(self):
        app = MDApp.get_running_app()
        app.deck_pressed(self)

class ClickableImage(ButtonBehavior, Image):
    #this is for the pyramid to call image_press
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (150, 130)
        self.keep_ratio = False
        
    def on_press(self):
        app = MDApp.get_running_app()
        app.image_pressed(self)

kv="""
Screen:
    #set the bg of whole screen to this image 
    Image:
        source: "img/1751873573054.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #Make all 28 images for pyramids
    ClickableImage:
        id:i0
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.20, "center_y": 0.949}
    ClickableImage:
        id:i1
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.5, "center_y": 0.949}
    ClickableImage:
        id:i2
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.80, "center_y": 0.949}
    ClickableImage:
        id:i3
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.16, "center_y": 0.9}
    ClickableImage:
        id:i4
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.25, "center_y": 0.9}   
    ClickableImage:
        id:i5
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.46, "center_y": 0.9}
    ClickableImage:
        id:i6
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.55, "center_y": 0.9}   
    ClickableImage:
        id:i7
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.76, "center_y": 0.9}     
    ClickableImage:
        id:i8
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.85, "center_y": 0.9}
    ClickableImage:
        id:i9
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.10, "center_y": 0.85}
    ClickableImage:
        id:i10
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.20, "center_y": 0.85}
    ClickableImage:
        id:i11
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.30, "center_y": 0.85}
    ClickableImage:
        id:i12
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.40, "center_y": 0.85}
    ClickableImage:
        id:i13
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.50, "center_y": 0.85}          
    ClickableImage:
        id:i14
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.60, "center_y": 0.85}
    ClickableImage:
        id:i15
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.70, "center_y": 0.85}
    ClickableImage:
        id:i16
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.80, "center_y": 0.85}          
    ClickableImage:
        id:i17
        source: "img/bg.png"
        pos_hint:{ "center_x": 0.90, "center_y": 0.85}        
    ClickableImage:
        id:i18
        source: app.card_images[18]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.05, "center_y": 0.8}
    ClickableImage:
        id:i19
        source: app.card_images[19]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.15, "center_y": 0.8}            
    ClickableImage:
        id:i20
        source: app.card_images[20]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.25, "center_y": 0.8}   
    ClickableImage:
        id:i21
        source: app.card_images[21]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.35, "center_y": 0.8}              
    ClickableImage:
        id:i22
        source: app.card_images[22]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.45, "center_y": 0.8}
    ClickableImage:
        id:i23
        source: app.card_images[23]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.55, "center_y": 0.8}            
    ClickableImage:
        id:i24
        source: app.card_images[24]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.65, "center_y": 0.8}   
    ClickableImage:
        id:i25
        source: app.card_images[25]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.75, "center_y": 0.8} 
    ClickableImage:
        id:i26
        source: app.card_images[26]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.85, "center_y": 0.8}   
    ClickableImage:
        id:i27
        source: app.card_images[27]
        size_hint:(None,None)
        size:(70,120)
        pos_hint:{ "center_x": 0.95, "center_y": 0.8}
    Image:
        id:deck
        source: app.card_images[28]
        size_hint:(None,None)
        size:(400,300)
        pos_hint:{ "center_x": 0.75, "center_y": 0.3}
      #all the remaining cards as deck
    CllickableImage:
        id:i29
        source: "img/bg.png"
        size_hint:(None,None)
        size:(400,300)
        pos_hint:{ "center_x": 0.23, "center_y": 0.29}
    CllickableImage:
        id:i30
        source: "img/bg.png"
        size_hint:(None,None)
        size:(400,300)
        pos_hint:{ "center_x": 0.24, "center_y": 0.29}
    CllickableImage:
        id:i31
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.25, "center_y": 0.29 }
    CllickableImage:
        id: i32
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.26, "center_y": 0.29 }
    CllickableImage:
        id: i33
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.27, "center_y": 0.29 }
    CllickableImage:
        id: i34
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.28, "center_y": 0.29 }
    CllickableImage:
        id: i35
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.29, "center_y": 0.29 }
    CllickableImage:
        id: i36
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.30, "center_y": 0.29 }
    CllickableImage:
        id: i37
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.31, "center_y": 0.29 }
    CllickableImage:
        id: i38
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.32, "center_y": 0.29 }
    CllickableImage:
        id: i39
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.33, "center_y": 0.29 }
    CllickableImage:
        id: i40
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.34, "center_y": 0.29 }
    CllickableImage:
        id: i41
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.35, "center_y": 0.29 }
    CllickableImage:
        id: i42
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.36, "center_y": 0.29 }
    CllickableImage:
        id: i43
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.37, "center_y": 0.29 }
    CllickableImage:
        id: i44
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.38, "center_y": 0.29 }
    CllickableImage:
        id: i45
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.39, "center_y": 0.29 }
    CllickableImage:
        id: i46
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.40, "center_y": 0.29 }
    CllickableImage:
        id: i47
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.41, "center_y": 0.29 }
    CllickableImage:
        id: i48
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.42, "center_y": 0.29 }
    CllickableImage:
        id: i49
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.43, "center_y": 0.29 }
    CllickableImage:
        id: i50
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.44, "center_y": 0.29 }
    CllickableImage:
        id: i51
        source: "img/bg.png"
        size_hint: (None, None)
        size: (400, 300)
        pos_hint: { "center_x": 0.45, "center_y": 0.29 }
    MDIconButton:
        icon:"undo"
        size_hint: (None, None)
        size: (200, 100)
        icon_size:"70sp"
        pos_hint: { "center_x": 0.55, "center_y": 0.45 }
        on_press:app.undo()
"""

class MainApp(MDApp):
    def build(self):
        #good approach help on playagain
        self.initialize_game()
        return Builder.load_string(kv)
    
    def initialize_game(self):
        #store all card images 52 in a list
        self.card_images = [
            "img/clubs_a.png", "img/clubs_2.png", "img/clubs_3.png", "img/clubs_4.png", "img/clubs_5.png", "img/clubs_6.png",
            "img/clubs_7.png", "img/clubs_8.png", "img/clubs_9.png", "img/clubs_10.png", "img/clubs_j.png", "img/clubs_q.png", "img/clubs_k.png",
            
            "img/diamonds_a.png", "img/diamonds_2.png", "img/diamonds_3.png", "img/diamonds_4.png", "img/diamonds_5.png", "img/diamonds_6.png",
            "img/diamonds_7.png", "img/diamonds_8.png", "img/diamonds_9.png", "img/diamonds_10.png", "img/diamonds_j.png", "img/diamonds_q.png", "img/diamonds_k.png",
            
            "img/hearts_a.png", "img/hearts_2.png", "img/hearts_3.png", "img/hearts_4.png", "img/hearts_5.png", "img/hearts_6.png",
            "img/hearts_7.png", "img/hearts_8.png", "img/hearts_9.png", "img/hearts_10.png", "img/hearts_j.png", "img/hearts_q.png", "img/hearts_k.png",
            
            "img/spades_a.png", "img/spades_2.png", "img/spades_3.png", "img/spades_4.png", "img/spades_5.png", "img/spades_6.png",
            "img/spades_7.png", "img/spades_8.png", "img/spades_9.png", "img/spades_10.png", "img/spades_j.png", "img/spades_q.png", "img/spades_k.png",
        ]
        #To keep track of remaining cards on pyramids 
        self.remaining = list(range(28))
        self.match = {
            "2": ["a", "3"],
            "3": ["2", "4"],
            "4": ["3", "5"],
            "5": ["4", "6"],
            "6": ["5", "7"],
            "7": ["6", "8"],
            "8": ["7", "9"],
            "9": ["8", "10"],
            "10": ["9", "j"],
            "j": ["10", "q"],
            "q": ["j", "k"],
            "k": ["q", "a"],
            "a": ["k", "2"]
        }
        
        random.shuffle(self.card_images)
        self.dec = 51
        self.move_history = []
        self.removed_widget = {}
        self.current = self.card_images[28]
    
    def reset_game_ui(self):
        if not self.root:
            return
        self.root.ids.deck.source = self.card_images[28]
        for i in range(3):
            self.root.ids[f"i{i}"].source = "img/bg.png"
            self.root.ids[f"i{i}"].size = (150, 130)
        for i in range(3, 9):
            self.root.ids[f"i{i}"].source = "img/bg.png"
            self.root.ids[f"i{i}"].size = (150, 130)
        for i in range(9, 18):
            self.root.ids[f"i{i}"].source = "img/bg.png"
            self.root.ids[f"i{i}"].size = (150, 130)
        for i in range(18, 28):
            self.root.ids[f"i{i}"].source = self.card_images[i]
            self.root.ids[f"i{i}"].size = (70, 120)
        for i in range(29, 52):
            self.root.ids[f"i{i}"].source = "img/bg.png"
            self.root.ids[f"i{i}"].size = (400, 300)
    
    def play_again(self):
        if hasattr(self, 'toss_dialog'):
            self.toss_dialog.dismiss()
        for widget_id in range(28):  
            widget_id_str = f"i{widget_id}"
            if widget_id_str in self.removed_widget:
                widget = self.removed_widget[widget_id_str]
                try:
                    if hasattr(widget, 'parent') and widget.parent is not None:
                        widget.parent.remove_widget(widget)
                except (ReferenceError, AttributeError):
                    pass
        for widget_id in range(29, 52):
            widget_id_str = f"i{widget_id}"
            if widget_id_str in self.removed_widget:
                widget = self.removed_widget[widget_id_str]
                try:
                    if hasattr(widget, 'parent') and widget.parent is not None:
                        widget.parent.remove_widget(widget)
                except (ReferenceError, AttributeError):
                    pass
        self.removed_widget.clear()
        for widget_id in range(28):
            widget_id_str = f"i{widget_id}"
            try:
                widget = self.root.ids.get(widget_id_str)
                if widget and hasattr(widget, 'parent') and widget.parent is None:
                    self.root.add_widget(widget)
            except (ReferenceError, AttributeError):
                pass
        for widget_id in range(29, 52): 
            widget_id_str = f"i{widget_id}"
            try:
                widget = self.root.ids.get(widget_id_str)
                if widget and hasattr(widget, 'parent') and widget.parent is None:
                    self.root.add_widget(widget)
            except (ReferenceError, AttributeError):
                pass
        self.initialize_game()
        self.reset_game_ui()
        toast("New game started!")
    def image_pressed(self, imgg_widget):
        if imgg_widget.source == "img/bg.png":
            return
        select = self.extract_number(imgg_widget.source)
        to_match = self.extract_number(self.current)
        if select in self.match[to_match]:
            widget_id = None
            for id_name, widget in self.root.ids.items():
                if widget == imgg_widget:
                    widget_id = id_name
                    break 
            if widget_id is not None:
                move_info = {
                    'type': 'pyramid',
                    'widget_id': widget_id,
                    'card_source': imgg_widget.source,
                    'previous_current': self.current,
                    'previous_remaining': self.remaining.copy(),
                    'widget': imgg_widget
                }
                self.move_history.append(move_info) 
                self.remaining.remove(int(widget_id[1:]))  # Remove 'i' and convert to int
                self.current = imgg_widget.source
                self.root.ids.deck.source = self.current         
                self.removed_widget[widget_id] = imgg_widget
                if imgg_widget.parent is not None:
                    imgg_widget.parent.remove_widget(imgg_widget)           
                self.more()          
                if self.dec == 28:
                    has_valid_move = False
                    for card_id in self.remaining:
                        if f"i{card_id}" in self.root.ids and self.root.ids[f"i{card_id}"].source != "img/bg.png":
                            select = self.extract_number(self.root.ids[f"i{card_id}"].source)
                            to_match = self.extract_number(self.current)
                            if select in self.match[to_match]:
                                has_valid_move = True
                                break
                    if not has_valid_move:
                        self.lose_popup("You lost")
                        toast("You lost")            
                if self.remaining == []:
                    self.lose_popup("You Won")
                    toast("you won")
    def deck_pressed(self, img_widget):
        if self.dec >= 29:
            move_info = {
                'type': 'deck',
                'widget_id': f"i{self.dec}",
                'card_source': self.card_images[self.dec],
                'previous_current': self.current,
                'previous_dec': self.dec,
                'widget': img_widget
            }
            self.move_history.append(move_info)            
            self.current = self.card_images[self.dec]
            self.root.ids.deck.source = self.card_images[self.dec]
            widget_id = f"i{self.dec}"
            if widget_id in self.root.ids:
                widget = self.root.ids[widget_id]
                if widget.parent is not None:
                    self.removed_widget[widget_id] = widget
                    widget.parent.remove_widget(widget)         
            self.dec -= 1         
        if self.dec == 28:
            has_valid_move = False
            for card_id in self.remaining:
                if f"i{card_id}" in self.root.ids and self.root.ids[f"i{card_id}"].source != "img/bg.png":
                    select = self.extract_number(self.root.ids[f"i{card_id}"].source)
                    to_match = self.extract_number(self.current)
                    if select in self.match[to_match]:
                        has_valid_move = True
                        break    
            if not has_valid_move:
                self.lose_popup("You lost")
                toast("You lost")
    def extract_number(self, filename):
        return str(filename.split('_')[1].split('.')[0])
    def more(self):
        a = self.remaining
        conditions = [
            (27, 26, "i17"),
            (25, 26, "i16"),
            (24, 25, "i15"),
            (23, 24, "i14"),
            (22, 23, "i13"),
            (22, 21, "i12"),
            (21, 20, "i11"),
            (20, 19, "i10"),
            (18, 19, "i9"),
            (9, 10, "i3"),
            (10, 11, "i4"),
            (13, 12, "i5"),
            (13, 14, "i6"),
            (15, 16, "i7"),
            (16, 17, "i8"),
            (3, 4, "i0"),
            (5, 6, "i1"),
            (8, 7, "i2")
        ]   
        for check1, check2, target_id in conditions:
            if target_id in self.root.ids:
                if check1 not in a and check2 not in a:
                    self.root.ids[target_id].source = self.card_images[int(target_id[1:])]  # Remove 'i' and convert to int
                    self.root.ids[target_id].size = (70, 120)
                else:
                    self.root.ids[target_id].source = "img/bg.png"
                    self.root.ids[target_id].size = (150, 130)
    def restore_removed_widget(self, widget_id):
        if widget_id in self.removed_widget:
            try:
                widget = self.removed_widget[widget_id]
                if hasattr(widget, 'parent'):
                    if widget.parent is None:
                        self.root.add_widget(widget)
                    if widget_id.startswith('i') and int(widget_id[1:]) < 28:  # Check if ID starts with 'i' and is pyramid card
                        card_num = int(widget_id[1:])
                        if card_num not in self.remaining:
                            self.remaining.append(card_num)
                del self.removed_widget[widget_id]
            except (ReferenceError, AttributeError):
                if widget_id in self.removed_widget:
                    del self.removed_widget[widget_id]
    def undo(self):
        if not self.move_history:
            toast("No moves to undo")
            return
        if self.dec == 28 and len([x for x in self.move_history if x['widget_id'].startswith('i') and int(x['widget_id'][1:]) >= 29]) == 0:
            toast("Cannot undo - deck is at original state")
            return
        last_move = self.move_history.pop()
        last_widget_id = last_move['widget_id']
        self.restore_removed_widget(last_widget_id)
        if last_widget_id.startswith('i') and int(last_widget_id[1:]) >= 29:
            self.dec += 1
        if self.move_history:
            prev_move = self.move_history[-1]
            prev_widget_id = prev_move['widget_id']
            if prev_widget_id.startswith('i'):
                card_num = int(prev_widget_id[1:])
                self.current = self.card_images[card_num]
        else:
            self.current = self.card_images[28]

        self.root.ids.deck.source = self.current
        toast(f"Undid move")
        self.more()
    def lose_popup(self, text):
        btn_play_again = MDFillRoundFlatIconButton(
            text='Play Again', 
            icon='refresh',
            on_press=lambda inst: self.play_again()
        )
        btn_quit = MDFillRoundFlatIconButton(
            text='Quit', 
            icon='logout',
            on_press=lambda inst: self.quit_game()
        )        
        self.toss_dialog = MDDialog(
            title='Game Over',
            auto_dismiss=False,
            text=f'{text}',
            buttons=[btn_play_again, btn_quit]
        )
        self.toss_dialog.open()  
    def quit_game(self):
        if hasattr(self, 'toss_dialog'):
            self.toss_dialog.dismiss()
        Window.close()
MainApp().run()