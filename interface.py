import tkinter as tk
from tkinter import ttk
import blackjack
import pokergame

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)
FONT_HEL = ("Helvetica", 14)
amount_of_funds = 10

class Interface(tk.Tk):
    # make an interface; a list of all frames, that are made elsewhere
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Casino")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NextPage, OtherPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    # frame of the start page:
    # background image <= doesn't work yet
    # send to Next page or other page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # background_image = tk.PhotoImage(file="aces.png")
        # #background_image.resize((400,400))
        # background_label = tk.Label(self, image=background_image) # .grid() #row=0,column=0,sticky=w)
        # background_label.place(relwidth=1, relheight=1)  # Place it to cover the whole window
        # background_label.background_image = background_image #
        # # <-- solution for bug: https://stackoverflow.com/questions/46624594/python-tkinter-photoimage-not-working-correctly

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=30, padx=10)

        button1 = ttk.Button(self, text="Poker", command=lambda: controller.show_frame(NextPage))
        button1.pack(pady=20) # place(x=250, y=100)

        button2 = ttk.Button(self, text="Blackjack", command=lambda: controller.show_frame(OtherPage))
        button2.pack(pady=20) # .grid(row=0, column=0, padx=20, pady=10)

        button3 = ttk.Button(self, text="Quit", command=lambda: controller.destroy())
        button3.pack(pady=20)

        self.update_amount_of_money()
        #number_label = tk.Label(self, text="Player balance: " + str(amount_of_funds), font=FONT_HEL)
        #number_label.place(relx=1.0, rely=0.0, anchor="ne")

    def update_amount_of_money(self):
        number_label = tk.Label(self, text="Player balance: " + str(amount_of_funds), font=FONT_HEL)
        number_label.place(relx=1.0, rely=0.0, anchor="ne")

class NextPage(tk.Frame):
    # frame for poker <= to do
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Under construction")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Go back", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class OtherPage(tk.Frame):
    # frame of the blackjack: import blackjack
    # make tk.Frame, buttons and labels
    def __init__(self, parent, controller):
        self.numb_play = 1
        self.game = blackjack.BlackJackGame()
        self.game_on = False
        self.player_on = [False, False, False, False]

        tk.Frame.__init__(self, parent)
        self.configure(bg="green")  # Set the background to green

        go_back_button = ttk.Button(self, text="Go back", command=lambda: [controller.show_frame(StartPage), self.update_amount_of_money()])
        go_back_button.place(x=10, y=10)  # Place the button in the top-left corner
        start_button = ttk.Button(self, text="Start", command=lambda: self.popup_msg())
        start_button.place(x=10, y=40)

        self.update_amount_of_money()

        self.update_mid_disp()

        bottom_labels = ["Bet 1", "Bet 2", "Bet 3", "Bet 4"]

        for i, label_text in enumerate(bottom_labels):
            label = ttk.Label(self, text=label_text) #, bg="green", fg="white")
            label.place(x=int(i*155+20), y=150, height=80, width=150)

        # Create a button for each
        button11 = ttk.Button(self, text=f"More", command=lambda l=label_text: self.pressed_more(0))
        button11.place(x=20, y=240, height=40, width=75)
        button12 = ttk.Button(self, text=f"More", command=lambda l=label_text: self.pressed_more(1))
        button12.place(x=int(1 * 155 + 20), y=240, height=40, width=75)
        button13 = ttk.Button(self, text=f"More", command=lambda l=label_text: self.pressed_more(2))
        button13.place(x=int(2 * 155 + 20), y=240, height=40, width=75)
        button14 = ttk.Button(self, text=f"More", command=lambda l=label_text: self.pressed_more(3))
        button14.place(x=int(3 * 155 + 20), y=240, height=40, width=75)

        button21 = ttk.Button(self, text=f"Done", command=lambda l=label_text: self.pressed_done(0))
        button21.place(x=95, y=240, height=40, width=75)
        button22 = ttk.Button(self, text=f"Done", command=lambda l=label_text: self.pressed_done(1))
        button22.place(x=int(1*155+95), y=240, height=40, width=75)
        button23 = ttk.Button(self, text=f"Done", command=lambda l=label_text: self.pressed_done(2))
        button23.place(x=int(2*155+95), y=240, height=40, width=75)
        button24 = ttk.Button(self, text=f"Done", command=lambda l=label_text: self.pressed_done(3))
        button24.place(x=int(3*155+95), y=240, height=40, width=75)

    # pop up to decide number of bets
    def popup_msg(self):
        if not self.game_on:
            popup = tk.Tk()
            popup.wm_title("Amount of players")
            label = ttk.Label(popup, text="How many bets?")
            label.grid(column=0, row=0, sticky='w')

            slider = tk.Scale(popup, from_=1, to=4, orient='horizontal', resolution=1, command=self.update_numb_play)
            slider.set(self.numb_play)
            slider.grid(column=1, row=0, sticky='we')

            button1 = ttk.Button(popup, text="Okay", command = lambda: [self.start_game(), popup.destroy()])
            button1.grid(column=2, row=1, sticky='n')
            popup.mainloop()

    # commands when a button was pressed:
    # get an extra card and be done getting cards
    def pressed_more(self, i):
        if int(self.numb_play) > i and self.player_on[i]:
            card = self.game.deck.deal_card()
            self.game.players[i].receive_card(card)
            self.update_one_label(i, self.game.players[i].show_hand())

    def pressed_done(self, i):
        self.player_on[i] = False
        if not any(self.player_on):
            self.end_game()

    # update labels
    def update_numb_play(self, n):
        self.numb_play = int(n)

    def update_mid_disp(self):
        if not self.game_on:
            text_disp = "Press start, to start"
        else:
            text_disp = "   Game on             "
        middle_string_label = tk.Label(self, text=text_disp, font=("Helvetica", 16), bg="green", fg="white")
        middle_string_label.place(x=100, y=20)

    def update_host_disp(self, host_text):
        host_label1 = tk.Label(self, text="House cards:", font=("Helvetica", 11), bg="green", fg="white")
        host_label1.place(x=100, y=80, width=100)
        host_text = host_text.replace(",", "\n")
        temp_eval = blackjack.evaluate_bj(self.game.host.string_hand()[0])
        host_text = host_text.replace(",", "\n")
        host_text = str(temp_eval) + "\n " + host_text
        host_label2 = tk.Label(self, text=host_text, font=("Helvetica", 10), bg="green", fg="white")
        host_label2.place(x=250, y=50, height=80, width=150)

    def update_amount_of_money(self): #, num):
        number_label = tk.Label(self, text="Player balance: " + str(amount_of_funds), font=FONT_HEL, bg="green", fg="white")
        number_label.place(relx=1.0, rely=0.0, anchor="ne")#, padx=10, pady=10)  # Top-right corner

    def update_label(self):
        bottom_labels = ["Bet 1", "Bet 2", "Bet 3", "Bet 4"]
        for i, (label_text) in enumerate(bottom_labels):
            label = ttk.Label(self, text=label_text, font=SMALL_FONT)
            label.place(x=int(i*155+20), y=150, height=80, width=150)

    def update_one_label(self, label_nmr = 1, text="hmm"):
        if "," in text:
            temp_eval = blackjack.evaluate_bj(self.game.players[label_nmr].string_hand()[0])
            text = text.replace(",", "\n")
            text = str(temp_eval) + "\n " + text
            if temp_eval < 21:
                label = tk.Label(self, text=text, fg="white", bg="blue", font=SMALL_FONT)
                label.place(x=int(label_nmr * 155 + 20), y=150, height=80, width=150)
            elif temp_eval == 21:
                label = tk.Label(self, text=text, fg="yellow", bg="blue", font=SMALL_FONT)
                label.place(x=int(label_nmr * 155 + 20), y=150, height=80, width=150)
                self.pressed_done(label_nmr)
            else:
                label = tk.Label(self, text=text, fg="red", bg="blue", font=SMALL_FONT)
                label.place(x=int(label_nmr * 155 + 20), y=150, height=80, width=150)
                self.pressed_done(label_nmr)
        else:
            label = tk.Label(self, text=text, fg="black", bg="white", font=SMALL_FONT)
            label.place(x=int(label_nmr * 155 + 20), y=150, height=80, width=150)

    # game itself:
    # game starts: players are made, state game == True and update labels
    # game ends when all bets are done, next host receives cards and is evaluated
    # update labels and state game is of
    def start_game(self):
        global amount_of_funds
        zzz = int(self.numb_play)
        amount_of_funds = amount_of_funds - zzz
        self.update_label()
        self.game_on = True
        self.update_mid_disp()
        self.update_amount_of_money()
        self.player_on = [True for i in range(zzz)] + [False for i in range(4-zzz)]
        self.game.deck.reset()
        self.game.deck.shuffle()
        self.game.host.hand = []
        self.game.host.receive_card(self.game.deck.deal_card())
        self.update_host_disp(self.game.host.show_hand())
        self.game.players = [pokergame.Player(i) for i in range(zzz)]
        for i, player in enumerate(self.game.players):
            card = self.game.deck.deal_card()
            player.receive_card(card)
            card = self.game.deck.deal_card()
            player.receive_card(card)
            self.update_one_label(i, player.show_hand())

    def end_game(self):
        if self.game_on:
            global amount_of_funds
            count_wins = 0
            self.game.host.receive_card(self.game.deck.deal_card())
            to_beat = int(blackjack.evaluate_bj(self.game.host.string_hand()[0]))
            while to_beat < 16:
                self.game.host.receive_card(self.game.deck.deal_card())
                to_beat = int(blackjack.evaluate_bj(self.game.host.string_hand()[0]))
            self.update_amount_of_money() #to_beat
            self.update_host_disp(self.game.host.show_hand())
            if to_beat>21:
                to_beat=0
            for i, player in enumerate(self.game.players):
                ev_bj = blackjack.evaluate_bj(player.string_hand()[0])
                if ev_bj == 21:
                    self.update_one_label(i, "Blackjack!")
                    count_wins += 3
                elif to_beat < ev_bj < 22:
                    self.update_one_label(i, "You won")
                    count_wins += 2
                else:
                    self.update_one_label(i, "You lost")
            amount_of_funds += count_wins
        self.game_on = False
        self.update_mid_disp()
        self.update_amount_of_money()


if __name__ == "__main__":
    app = Interface()
    app.geometry("650x350")
    app.mainloop()
