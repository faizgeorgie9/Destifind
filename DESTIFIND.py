import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from customtkinter import *
import csv 
import textwrap
from functools import partial
from chart_binary import char_to_binary
from tkcalendar import *
from datetime import datetime, timedelta 
import pickle
from tree import TreeNode
import re
from tkinter.messagebox import showinfo
import ast


class DestifindApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1366x768')
        self.title('Destifind')
        self.state("zoomed")
        self.iconbitmap("media/landscape.ico")

        bg_image = Image.open("media/image/landscape.png")
        desired_width = 100
        desired_height = 100
        bg_image = bg_image.resize((desired_width, desired_height), Image.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(bg_image)
        self.bg_image = ctk.CTkImage(bg_image, size=(desired_width, desired_height))

        self.background_image = Image.open("media/image/bgph.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = CTkLabel(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_frame  = CTkFrame(master=self, fg_color="white")
        self.main_frame.place(x=502.9, y=68)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=274, height=480)


        self.bg_label = ctk.CTkLabel(self.main_frame, text_color="#526D82", wraplength=0, corner_radius=20, text="Destifind", fg_color="#FFFFFF",  font=("Sitka Small Semibold", 20, 'bold'), width=100, height=50, anchor="center")
        self.bg_label.place(x=70, y=210)

        self.bg_label1 = ctk.CTkLabel(self.main_frame, text="", image=self.bg_image)
        self.bg_label1.place(x=90, y=70)

        self.selected_times = []
        self.selected_dates = []
        self.selected_destination = []
        self.selected_harga = []

        self.after(2000, self.appear)
    
    def appear(self):
        self.bg_label = ctk.CTkLabel(self.main_frame, text_color="#526D82", wraplength=0, corner_radius=20, text="Your Travel Guide", fg_color="#FFFFFF", font=("Sitka Small Semibold", 20, 'bold'), width=100, height=50, anchor="center")
        self.bg_label.place(x=25, y=250)
        self.after(2000, self.main_menu)

    def main_menu(self):
        self.main_frame_login  = CTkFrame(self.main_frame, fg_color="white")
        self.main_frame_login.place(x=546, y=93)

        def cek_in():
            global usr 
            global pw
            global ac
            global pwd
            global usn
            usr = self.entry1.get()
            pw = self.entry2.get()
      
            data_akun = open("data/data_akun.csv",'r').read().split('\n')
            cekin = 0
            for akun in data_akun :
             if akun == "" :
                continue 
             acpw = akun.split(',')
       
             ac = acpw[0]
             pwd = acpw[1]
             usn = acpw[2]

             if ( usr == ac and pw == pwd ) :
                    cekin += 1
                    self.setup_ui()
                    break
             else :
                pass
             
             if cekin == 0 :
                showinfo(title="Info", message="Wrong Email and Password !")
        self.bg_label1.place_forget()
        self.bg_label.place_forget()
        self.main_frame.pack_forget()

        self.main_frame1  = CTkFrame(master=self, fg_color="white")
        self.main_frame1.place(x=502.9, y=68)
        self.main_frame1.pack_propagate(False)
        self.main_frame1.configure(width=274, height=480)

        self.label1 = ctk.CTkLabel(self.main_frame1, text_color="#C38154", wraplength=0, corner_radius=20, text="Login", bg_color="transparent", font=("Sitka Small Semibold", 35, 'bold'), width=100, height=20, anchor="center")
        self.label1.place(x=35, y=900)

        self.entry1 = ctk.CTkEntry(self.main_frame1,  text_color="black", corner_radius=10, placeholder_text="✉ Email", fg_color="transparent", font=("Sitka Small Semibold", 15, 'bold'), width=246, height=40)
        self.entry1.place(x=35, y=900)

        self.entry2 = ctk.CTkEntry(self.main_frame1, show='*', text_color="black",   corner_radius=10, placeholder_text="🔒 Password", fg_color="transparent", font=("Sitka Small Semibold", 14, 'bold'), width=246, height=40)
        self.entry2.place(x=35, y=900)
        
        self.bttn_lgn = ctk.CTkButton(self.main_frame1,command=cek_in,  text_color="#526D82", fg_color="white", text="Login →", font=("Sitka Small Semibold", 13, 'bold'), width=17, height=20, hover_color="#F8E8EE")
        self.bttn_lgn.place(x=70, y=900)

       

        self.imgs = ImageTk.PhotoImage(Image.open("media/image/show.png"), size=(5,3))
        self.imgh = ImageTk.PhotoImage(Image.open("media/image/hide.png"), size=(5,3))
       

        self.ball_y = 800
        self.ball_dy = -15

        self.ball2_y = 900  
        self.ball2_dy = -20

        self.ball3_y = 900  
        self.ball3_dy = -20

        self.ball4_y = 900  
        self.ball4_dy = -20

        self.animate()

    def animate(self):
        self.ball_y += self.ball_dy
        if self.ball_y <= 35: 
            self.ball_dy = 0 
            self.after(500,self.animate2)

        self.label1.place(x=15, y=self.ball_y)

        if self.ball_dy != 0:
            self.after(15, self.animate)
    def animate2(self):
        self.ball2_y += self.ball2_dy
        if self.ball2_y <= 219: 
            self.ball2_dy = 0 
            self.after(500, self.animate3)
            
        self.entry1.place(x=15, y=self.ball2_y)

        if self.ball2_dy != 0:
            self.after(20, self.animate2)

    def animate3(self):
        self.ball3_y += self.ball3_dy
        if self.ball3_y <= 270: 
            self.ball3_dy = 0 
            self.after(500, self.animate4)
            
            
        self.entry2.place(x=15, y=self.ball3_y)

        if self.ball3_dy != 0:
            self.after(20, self.animate3)

    
    def animate4(self):
        self.ball4_y += self.ball4_dy
        if self.ball4_y <= 350: 
            self.ball4_dy = 0   
            self.after(500, self.lbl2)
            
        self.bttn_lgn.place(x=190, y=self.ball4_y)

        if self.ball4_dy != 0:
            self.after(20, self.animate4)

    def lbl2(self):
        self.label2 = ctk.CTkLabel(self.main_frame1, text_color="grey", wraplength=0, corner_radius=20, text="Dont Have An Account ?", bg_color="transparent", font=("Sitka Small Semibold", 13, 'bold'), width=100, height=20,)
        self.label2.place(x=45, y=430)

        self.bttn1 = ctk.CTkButton(self.main_frame1,command=self.signup,  text_color="#526D82", fg_color="white", text="Sign Up", font=("Sitka Small Semibold", 13, 'bold'), width=17, height=20, hover_color="#F8E8EE")
        self.bttn1.place(x=101, y=455)

        def button_show():
                if self.entry2.cget('show')=='*':
                    self.entry2.configure(show='')
                    toggle_btn.config(image=self.imgs)
                else:
                    self.entry2.configure(show='*')
                    toggle_btn.config(image=self.imgh)
                    
        toggle_btn = Button(self.main_frame1, command=button_show, width=5, height=3, bg="white", border=0, fg="black", font=("Sitka Small Semibold",22, 'bold'), activebackground="white") 
        toggle_btn.config(image=self.imgh)
        toggle_btn.place(relwidth=0.2, relheight=0.07, relx=0.75, rely=0.55)


    def placeholder_handler(event):
        if event.widget.get() == "✉ Email":
            event.widget.delete(0, 'end')

    def placeholder_restore(event):
        if event.widget.get() == "":
            event.widget.insert(0, "✉ Email")

    def signup(self):
        def cek():
            def cek2():
                if len(b) < 6 :
                    showinfo(title="Info", message="Password Salah !")
                    self.entry1_sign.delete(0, 'end')
                
                    self.entry2_sign.delete(0, 'end')
                

                    self.entry3_sign.delete(0, 'end')

                
            global a
            global b 
            global c
            a = self.entry2_sign.get()
            b = self.entry3_sign.get()
            c = self.entry1_sign.get()
            if a[-1:-10:-1][::-1] != '@nesa.com':
                showinfo(title="Info", message="Format Email Salah !")
                self.entry1_sign.delete(0, 'end')
                
                self.entry2_sign.delete(0, 'end')
               

                self.entry3_sign.delete(0, 'end')
                

            if a[-1:-10:-1][::-1] == '@nesa.com' :
             global d
             d = False
             akun_pw = data_akun_text.split('\n')
             for akun in akun_pw:
              email = akun.split(",")
              if email[0] == a :
                d = True
                showinfo(title="Info", message="Email Sudah Dipakai !")
                self.entry1_sign.delete(0, 'end')
                    
                self.entry2_sign.delete(0, 'end')
                                
                self.entry3_sign.delete(0, 'end') 
                
                           
                            
             else :   
               if len(b) > 5 :
                self.data_akun.write(f"{a},{b},{c}\n")
                self.data_akun.close()
                self.back_mainmenu()
                                
                                                
               else :
                d = cek2()         


        self.data_akun = open("data/data_akun.csv",'a+')
        self.data_akun_r = open("data/data_akun.csv", 'r')
        data_akun_text = self.data_akun_r.read()
        self.main_frame1.pack_forget()

        self.main_frame2  = CTkFrame(master=self, fg_color="white")
        self.main_frame2.place(x=502.9, y=68)
        self.main_frame2.pack_propagate(False)
        self.main_frame2.configure(width=274, height=480)


        self.label_sign = ctk.CTkLabel(self.main_frame2, text_color="#C38154", wraplength=0, corner_radius=20, text="Create Account", bg_color="transparent", font=("Sitka Small Semibold", 25, 'bold'), width=100, height=20, anchor="center")
        self.label_sign.place(x=35, y=900)

        self.entry1_sign = ctk.CTkEntry(self.main_frame2, placeholder_text_color="black",  text_color="black", corner_radius=10, placeholder_text="👤 Full Name", fg_color="transparent", font=("Sitka Small Semibold", 15, 'bold'), width=246, height=40)
        self.entry1_sign.place(x=35, y=900)

        self.entry2_sign = ctk.CTkEntry(self.main_frame2,  placeholder_text_color="black", text_color="black", corner_radius=10, placeholder_text="✉ Email (..@nesa.com)", fg_color="transparent", font=("Sitka Small Semibold", 15, 'bold'), width=246, height=40)
        self.entry2_sign.place(x=35, y=900)

        self.entry3_sign = ctk.CTkEntry(self.main_frame2, placeholder_text_color="black",  text_color="black", corner_radius=10, placeholder_text="🔒 Password ( 6 digit )", fg_color="transparent", font=("Sitka Small Semibold", 15, 'bold'), width=246, height=40)
        self.entry3_sign.place(x=35, y=900)

        self.bttn3_sign = ctk.CTkButton(self.main_frame2,command=cek,  text_color="#526D82", fg_color="white", text="Sign Up →", font=("Sitka Small Semibold", 13, 'bold'), width=17, height=20, hover_color="#F8E8EE")
        self.bttn3_sign.place(x=-20, y=900)

        self.ball_ysign = 900
        self.ball_dysign = -15

        self.ball2_ysign = 900  
        self.ball2_dysign = -20

        self.ball3_ysign = 900  
        self.ball3_dysign = -20

        self.ball4_ysign = 900  
        self.ball4_dysign = -20

        self.ball5_ysign = 900  
        self.ball5_dysign = -20

        self.animate_sign()

    def animate_sign(self):
        self.ball_ysign += self.ball_dysign
        if self.ball_ysign <= 35: 
            self.ball_dysign = 0 
            self.after(500,self.animate2_sign)

        self.label_sign.place(x=15, y=self.ball_ysign)

        if self.ball_dysign != 0:
            self.after(15, self.animate_sign)

    def animate2_sign(self):
        self.ball2_ysign += self.ball2_dysign
        if self.ball2_ysign <= 200: 
            self.ball2_dysign = 0 
            self.after(500, self.animate3_sign)
            
        self.entry1_sign.place(x=15, y=self.ball2_ysign)

        if self.ball2_dysign != 0:
            self.after(20, self.animate2_sign)

    def animate3_sign(self):
        self.ball3_ysign += self.ball3_dysign
        if self.ball3_ysign <= 270: 
            self.ball3_dysign = 0   
            self.after(500, self.animate4_sign)
            
        self.entry2_sign.place(x=15, y=self.ball3_ysign)

        if self.ball3_dysign != 0:
            self.after(20, self.animate3_sign)

    def animate4_sign(self):
        self.ball4_ysign += self.ball4_dysign
        if self.ball4_ysign <= 320: 
            self.ball4_dysign = 0   
            self.after(500, self.animate5_sign)
            
        self.entry3_sign.place(x=15, y=self.ball4_ysign)

        if self.ball4_dysign != 0:
            self.after(20, self.animate4_sign)

    def animate5_sign(self):
        self.ball5_ysign += self.ball5_dysign
        if self.ball5_ysign <= 380: 
            self.ball5_dysign = 0   
            self.after(1000, self.bttn_bck)
            
        self.bttn3_sign.place(x=190, y=self.ball5_ysign)

        if self.ball5_dysign != 0:
            self.after(20, self.animate5_sign)

    def bttn_bck(self):
        self.bttn2_sign = ctk.CTkButton(self.main_frame2,command=self.back_mainmenu,  text_color="#526D82", fg_color="white", text="Back", font=("Sitka Small Semibold", 13, 'bold'), width=17, height=20, hover_color="#F8E8EE")
        self.bttn2_sign.place(x=120, y=450)
    
    def back_mainmenu(self):
        self.main_frame2.pack_forget()
        self.main_menu()

# class DestifindApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.geometry('1280x720')
#         self.title('Destifind')  
#         self.state("zoomed")

#         self.load_background_image()
#         self.setup_ui()

#         self.selected_times = []
#         self.selected_dates = []
#         self.selected_destination = []
#         self.selected_harga = []

    def load_background_image(self):
        background_image = Image.open('media/image/bgph.png')
        self.background_photo = ImageTk.PhotoImage(background_image)

    def setup_ui(self):
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_fm  = CTkFrame(master=self, fg_color="white")
        self.main_fm.place(x=502.9, y=68)
        self.main_fm.pack_propagate(False)
        self.main_fm.configure(width=274, height=480)

        self.options_fm  = CTkFrame(master=self, fg_color="white")
        self.options_fm.place(x=502.9, y=550)
        self.options_fm.pack_propagate(False)
        self.options_fm.configure(width=274, height=40)

        self.homep = CTkImage(Image.open("media/image/homebttndn.png"), size=(42, 42))
        self.destip = CTkImage(Image.open("media/image/destibttndn.png"), size=(40, 40))
        self.guidep = CTkImage(Image.open("media/image/guidebttndn.png"), size=(40, 40))
        self.articlep = CTkImage(Image.open("media/image/articlebttndn.png"), size=(40, 40))
        self.homeb = CTkImage(Image.open("media/image/homebttncl.png"), size=(42, 42))
        self.destib = CTkImage(Image.open("media/image/destibttncl.png"), size=(40, 40))
        self.guideb = CTkImage(Image.open("media/image/guidebttncl.png"), size=(40, 40))
        self.articleb = CTkImage(Image.open("media/image/articlebttn.png"), size=(40, 40))

        self.home_btn = CTkButton(self.options_fm, image=self.homep, width=67.5, height=40, fg_color="white", hover_color="#FFFFFF", text="", command=lambda: self.switch(self.home_page, self.home_btn, self.homeb))
        self.home_btn.place(x=0, y=0)
        self.AI_btn = CTkButton(self.options_fm, image=self.destip, width=67.5, height=40, fg_color="white", hover_color="#FFFFFF", text="", command=lambda: self.switch(self.AI_page, self.AI_btn, self.destib))
        self.AI_btn.place(x=70, y=0)
        self.guide_btn = CTkButton(self.options_fm, image=self.guidep, width=67.5, height=40, fg_color="white", hover_color="#FFFFFF", text="", command=lambda: self.switch(self.guide_page, self.guide_btn, self.guideb))
        self.guide_btn.place(x=140, y=0)
        self.article_btn = CTkButton(self.options_fm, image=self.articlep, width=67.5, height=40, fg_color="white", hover_color="#FFFFFF", text="", command=lambda: self.switch(self.article_page, self.article_btn, self.articleb))
        self.article_btn.place(x=210, y=0)

        self.home_page()  # Tampilkan halaman utama saat aplikasi dijalankan

    def switch(self, page, button, new_button):
        for child in self.options_fm.winfo_children():
            if isinstance(child, CTkButton):
                self.switch_image(button, new_button)
        for fm in self.main_fm.winfo_children():
            # fm.destroy()
            fm.forget()
            self.update()
        page()

    def switch_image(self, button, new_button):
        # Kembalikan semua gambar ke gambar asli
        self.home_btn.configure(image=self.homep)
        self.AI_btn.configure(image=self.destip)
        self.guide_btn.configure(image=self.guidep)
        self.article_btn.configure(image=self.articlep)
        # Ganti gambar pada tombol yang diklik dengan gambar baru
        button.configure(image=new_button)

    def home_page(self):
        # global sc
        self.home_btn.configure(state=ACTIVE)
        self.AI_btn.configure(state=ACTIVE)
        self.guide_btn.configure(state=ACTIVE)
        self.article_btn.configure(state=ACTIVE)

        self.home_bg = CTkImage(Image.open('media/image/home_bg.png'), size=(274, 480))
        self.home_bg_label = CTkLabel(self.main_fm, image=self.home_bg, text='', width=27, height=480)
        self.home_bg_label.pack(fill=tk.BOTH, expand=True)

        #ISISNYA
        self.entry = CTkEntry(self.home_bg_label,  placeholder_text="Enter a Destination City", placeholder_text_color="#A9A9A9", text_color="#A9A9A9", corner_radius=16, width=188, height=32.1, font=("Poppins Bold", 11), fg_color="transparent")
        self.entry.place(x=19.6767578125, y=95.6751708984375)

        self.search1 =  CTkImage(Image.open("media/image/search_button.png"), size=(33, 33))
        self.search_btn = CTkButton(self.home_bg_label, image=self.search1, command=self.search, hover_color="#FFFFFF", text = '', fg_color="white", width=33, height=33)
        self.search_btn.place(x=211, y=94)

        self.scroll_frame_r = CTkScrollableFrame(self.home_bg_label, width=260, height=100, fg_color='white', orientation=HORIZONTAL, scrollbar_button_color="white", scrollbar_button_hover_color="white")
        self.scroll_frame_r.place(x=0, y=160)
    
        self.scroll_frame_k = CTkScrollableFrame(self.home_bg_label, width=265, height=50, fg_color='white')
        self.scroll_frame_k.place(x=0, y=299)

        self.malang = CTkImage(Image.open("media/image/malang.png"), size=(227, 89))
        self.malang_btn = CTkButton(self.scroll_frame_k, image=self.malang, fg_color="white", hover_color="#80B8F8", text="",command=partial(self.search_page, 'malang'))
        self.malang_btn.grid(row=0, padx=8, pady=0)

        self.surabaya = CTkImage(Image.open("media/image/surabaya.png"), size=(227, 89))
        self.surabaya_btn = CTkButton(self.scroll_frame_k, image=self.surabaya,  fg_color="white", hover_color="#80B8F8", text="", command=partial(self.search_page, 'surabaya'))
        self.surabaya_btn.grid(row=1, padx=8, pady=10)

        self.banyuwangi = CTkImage(Image.open("media/image/banyuwangi.png"), size=(227, 89))
        self.banyuwangi_btn = CTkButton(self.scroll_frame_k, image=self.banyuwangi, fg_color="white", hover_color="#80B8F8", text="", command=partial(self.search_page, 'banyuwangi'))
        self.banyuwangi_btn.grid(row=2, padx=8, pady=10)

        self.t_btn = CTkLabel(self.scroll_frame_k, fg_color="white", text="")
        self.t_btn.grid(row=3, pady=10)

        with open("data/tree.pickle", 'rb') as file :
            tree = pickle.load(file)
        def create_node_widgets( node, row=0, column=0):
                    global ao
                    if node.children:
                        next_row = row + 1
                        next_column = column
                        for child in node.children:
                            ao = child.data
                   
                            foto= child.children[4].data
                            ft = Image.open(foto)
                            fro = CTkImage(ft, size=(75, 90))
                            child_button = ctk.CTkButton(self.scroll_frame_r, hover_color='#80B8F8', fg_color='white', image=fro, text='', width=75, height=10, command=partial(self.artikel_awal, ao))
                            child_button.grid(row=next_row, column=next_column, padx=0, pady=0, sticky="w")
                            next_column += 1
        create_node_widgets(node=tree)
        
    #binary search
    def search(self):
            entry = self.entry.get()
            if not entry:
                messagebox.showwarning("Warning", "Please enter name of city!")
                return
            sc = self.entry.get()
        
            def string_to_binary(sc):
                binary_string = ''
                for char in sc:
                    binary_string += char_to_binary[char.lower()] + ' '
                return binary_string.strip()
            scc = string_to_binary(sc)
            wisata_data = []
            with open('data/wisata.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    nama_wisata = row[1]
                  
                    binary_wisata = string_to_binary(nama_wisata)
                    wisata_data.append((binary_wisata, nama_wisata))

            wisata_data.sort(key=lambda x: x[0])
              
            def binary_search(data, target_binary):
               
                left = 0
                right = len(data) -1
                
                while left <= right:
                    mid = (left + right) // 2
                    fc = data[mid][0] 
                    
                    if data[mid][0] == target_binary:
                        return mid
                    elif data[mid][0] < target_binary:
                        left = mid + 1
                    else:
                        right = mid - 1
                 
                return -1
            
            index = binary_search(wisata_data, scc)

            if index != -1:
                print(f"Destinasi '{wisata_data[index][1]}' ditemukan.")
                self.search_page(sc)
            else:
                print(f"Destinasi '{sc}' tidak ditemukan dalam data wisata.")
                messagebox.showwarning("Warning", f"Destination city '{sc}' is not found in the data.")

    def artikel_awal(self, name):
        if name == "pantai kenjeran lama" :
            self.clear_widgets()
            self.frame_isi_artikel1 = CTkFrame(self.main_fm, fg_color="White", width=50, height=55)
            self.frame_isi_artikel1.pack()
            
            image_isi_artikel1 = CTkImage(Image.open("media/image/ARTIKEL WR2.png"), size=(270, 480))
            Label_isi_artikel1 = CTkLabel(self.frame_isi_artikel1 , text="", image=image_isi_artikel1, compound="top", font=("Sitka Small", 11), fg_color="white")
            Label_isi_artikel1.pack()

            back_artikel1 = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
            button_back_artikel1 = CTkButton(self.frame_isi_artikel1, text="", image=back_artikel1, fg_color="white", hover_color="#FFFFFF", command=self.backh_artikel,  width=12, height=13)
            button_back_artikel1.place(x=14, y=10)

        elif name == "pantai trianggulasi" :
            self.clear_widgets()
            self.frame_isi_artikel2 = CTkFrame(self.main_fm, fg_color="White", width=50, height=55)
            self.frame_isi_artikel2.pack()
            
            image_isi_artikel2 = CTkImage(Image.open("media/image/ARTIKEL WR1.png"), size=(270, 480))
            Label_isi_artikel2 = CTkLabel(self.frame_isi_artikel2 , text="", image=image_isi_artikel2, compound="top", font=("Sitka Small", 11), fg_color="white")
            Label_isi_artikel2.pack()

            back_artikel2 = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
            button_back_artikel2 = CTkButton(self.frame_isi_artikel2, text="", image=back_artikel2, fg_color="white", hover_color="#FFFFFF", command=self.backh_artikel, width=12, height=13)
            button_back_artikel2.place(x=14, y=10)
        elif name == "kawah ijen" :
            self.clear_widgets()
            self.frame_isi_artikel3 = CTkFrame(self.main_fm, fg_color="White", width=50, height=55)
            self.frame_isi_artikel3.pack()
            
            image_isi_artikel3 = CTkImage(Image.open("media/image/ARTIKEL WR3.png"), size=(270, 480))
            Label_isi_artikel3 = CTkLabel(self.frame_isi_artikel3 , text="", image=image_isi_artikel3, compound="top", font=("Sitka Small", 11), fg_color="white")
            Label_isi_artikel3.pack()

            back_artikel3 = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
            button_back_artikel3 = CTkButton(self.frame_isi_artikel3, text="", image=back_artikel3, fg_color="white", hover_color="#FFFFFF", command=self.backh_artikel, width=12, height=13)
            button_back_artikel3.place(x=14, y=10)
        elif name == "hawai waterpark" :
            self.clear_widgets()
            self.frame_isi_artikel4 = CTkFrame(self.main_fm, fg_color="White", width=50, height=55)
            self.frame_isi_artikel4.pack()
            
            image_isi_artikel4 = CTkImage(Image.open("media/image/ARTIKEL WR4.png"), size=(270, 480))
            Label_isi_artikel4 = CTkLabel(self.frame_isi_artikel4 , text="", image=image_isi_artikel4, compound="top", font=("Sitka Small", 11), fg_color="white")
            Label_isi_artikel4.pack()

            back_artikel4 = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
            button_back_artikel4 = CTkButton(self.frame_isi_artikel4, text="", image=back_artikel4,  fg_color="white", hover_color="#FFFFFF", command=self.backh_artikel, width=12, height=13)
            button_back_artikel4.place(x=14, y=10)

    def backh_artikel(self):
        self.clear_widgets()
        self.home_page()

    def search_page(self, city):
        #nonaktifin button
        self.selected_wisata = []
        self.home_btn.configure(state=DISABLED)
        self.AI_btn.configure(state=DISABLED)
        self.guide_btn.configure(state=DISABLED)
        self.article_btn.configure(state=DISABLED)

        self.current_city = city
        self.home_bg_label.destroy()

        self.search_bg = CTkImage(Image.open('media/image/search_bg.png'), size=(274, 480))
        self.search_bg_label = CTkLabel(self.main_fm, image=self.search_bg, text='', width=27, height=480)
        self.search_bg_label.pack(fill=tk.BOTH, expand=True)

        #ISINYA
        self.back = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
        self.back_btn = CTkButton(self.search_bg_label, image=self.back, corner_radius=10, hover_color="#FFFFFF", text='',  command=self.destroy_search_lb, fg_color="white", width=12, height=13)
        self.back_btn.place(x=14, y=10)

        self.label_kota = CTkLabel(self.search_bg_label, text=f'Here is a list of tours in {city}',text_color="black", corner_radius=16, width=130, height=20, font=("Poppins ExtraBold", 12), fg_color="transparent")
        self.label_kota.place(x=15, y=102)
        
        self.create_btn = CTkButton(self.search_bg_label, text='Create', command=self.create_confirm, text_color="#FFFFFF", font=("Poppins ExtraBold", 8), fg_color="#0373F3", hover_color="#E9E9E9", corner_radius=4 ,width=37, height=17)
        self.create_btn.place(x=214, y=154)

        self.labelp = CTkLabel(self.search_bg_label, text='', width=235, height=70, fg_color='#FFFFFF')
        self.labelp.place(x=14, y=175)

        #Frame scrollbar
        scrollableframe = CTkScrollableFrame(master=self.search_bg_label, fg_color="#FFFFFF", corner_radius=0, width=275, height=305)
        scrollableframe.place(x=0, y=175)
        self.scrollableframe1 = tk.Canvas(scrollableframe, bg="#FFFFFF",  width=275, height=305)
        self.scrollableframe1.pack(fill=tk.BOTH, expand=True)

        #munculin gambar dari csv
        self.load_images_from_csv('data/data/wisata.csv', city)

        #Filter
        def toggle_menu():
            def collapse_toggle_menu():
                toggle_menu_fm.destroy()
            window_height = self.search_bg_label.winfo_height()
            window_width = self.search_bg_label.winfo_width()
            toggle_menu_fm = CTkFrame(self.search_bg_label, fg_color="#FFFFFF", height=window_height, width=window_width)
            toggle_menu_fm.place(x=100, y=0)

            backf = CTkImage(Image.open("media/image/back_btn.png"), size=(12, 13))
            backf_btn = CTkButton(toggle_menu_fm, image=backf, corner_radius=10, hover_color="#FFFFFF", text='', command=collapse_toggle_menu, fg_color="white", width=12, height=13)
            backf_btn.place(x=0, y=0)

            filter_label = CTkLabel(toggle_menu_fm,  text='Filter', text_color="#000000", font=('Poppins Sans ExtraBold', 14), fg_color="#FFFFFF")
            filter_label.place(x=75, y=0)

            sort_label = CTkLabel(toggle_menu_fm,  text='Sort by:', text_color="#000000", font=('Poppins Sans ExtraBold', 14), fg_color="#FFFFFF")
            sort_label.place(x=20, y=30)

            sort = CTkComboBox(toggle_menu_fm, values=['Lowest Price', 'Highest Price', 'Highest Rating'], text_color="#000000", command=self.sort_and_display, border_color="#0373F3", dropdown_fg_color="#FFFFFF", font=('Poppins ExtraBold', 14), fg_color="#FFFFFF", )
            sort.place(x=20, y=60)

        self.filter =  CTkImage(Image.open("media/image/filter.png"), size=(31, 31))
        self.filter_btn = CTkButton(self.search_bg_label, image=self.filter, text='',hover_color="#FFFFFF", corner_radius=0, border_width=0, command=toggle_menu, width=32, height=32, fg_color='#FFFFFF')
        self.filter_btn.place(x=215, y=93)

    def load_images_from_csv(self, csv_file, city):
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            df_filtered = [row for row in reader if row[1] == city]
            
            for index, row in enumerate(df_filtered):
                image = CTkImage(Image.open(row[0]), size=(228, 65))
                image_label = CTkLabel(self.scrollableframe1, image=image, text='', fg_color="#FFFFFF", width=210, height=60)
                image_label.grid(column=0, row=index, padx=20, pady=5)
                button_add = CTkButton(image_label, text="+", command=lambda r=row: self.add_wisata(r), fg_color="#0373F3", text_color="#FFFFFF", font=("Nunito Sans ExtraBold", 10), hover_color="#E9E9E9", corner_radius=50, width=17, height=10)
                button_add.place(x=203, y=40)

    def add_wisata(self, row):
        if row not in self.selected_wisata:
            self.selected_wisata.append(row)
            messagebox.showinfo("Info", f"{row[2]} tour has been added to the list")
        else:
            messagebox.showwarning("Warning", f"{row[2]} tour is already in the list")

    # Penerapan quickshort dalam pengurutan wisata berdasarkan filter yang dipilih user
    def quicksort(self, arr, key1, key2, reverse_key1=False):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            if reverse_key1:
                left = [x for x in arr if (float(x[key1]) > float(pivot[key1])) or (float(x[key1]) == float(pivot[key1]) and x[key2] < pivot[key2])]
                middle = [x for x in arr if float(x[key1]) == float(pivot[key1]) and x[key2] == pivot[key2]]
                right = [x for x in arr if (float(x[key1]) < float(pivot[key1])) or (float(x[key1]) == float(pivot[key1]) and x[key2] > pivot[key2])]
            else:
                left = [x for x in arr if (float(x[key1]) < float(pivot[key1])) or (float(x[key1]) == float(pivot[key1]) and x[key2] < pivot[key2])]
                middle = [x for x in arr if float(x[key1]) == float(pivot[key1]) and x[key2] == pivot[key2]]
                right = [x for x in arr if (float(x[key1]) > float(pivot[key1])) or (float(x[key1]) == float(pivot[key1]) and x[key2] > pivot[key2])]
            return self.quicksort(left, key1, key2, reverse_key1) + middle + self.quicksort(right, key1, key2, reverse_key1)

    def sort_and_display(self, criteria):
        # Membaca file CSV dan memfilter berdasarkan kota
        df_filtered = []
        with open('data/wisata.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Mengambil header
            for row in reader:
                if row[1] == self.current_city:
                    df_filtered.append(row)

        # Menentukan indeks kolom berdasarkan header CSV
        harga_idx = headers.index('harga')
        nm_idx = headers.index('nm')
        rating_idx = headers.index('rating')

        # Pengurutan wisata berdasarkan filter yang dipilih user
        if criteria == 'Lowest Price':
            sorted_df = self.quicksort(df_filtered, key1=harga_idx, key2=nm_idx)
        elif criteria == 'Highest Price':
            sorted_df = self.quicksort(df_filtered, key1=harga_idx, key2=nm_idx, reverse_key1=True)
        elif criteria == 'Highest Rating':
            sorted_df = self.quicksort(df_filtered, key1=rating_idx, key2=nm_idx, reverse_key1=True)
        
        for widget in self.scrollableframe1.winfo_children():
            widget.destroy()

        for index, row in enumerate(sorted_df):
            image1 = CTkImage(Image.open(row[0]), size=(228, 65))
            image_label1 = CTkLabel(self.scrollableframe1, image=image1, text='', fg_color="#FFFFFF", width=210, height=60)
            image_label1.grid(column=0, row=index, padx=20, pady=5)
            button_add1 = CTkButton(image_label1, text="+", command=lambda r=row: self.add_wisata(r), fg_color="#0373F3", text_color="#FFFFFF", font=("Nunito Sans ExtraBold", 10), hover_color="#E9E9E9", corner_radius=50, width=17, height=10)
            button_add1.place(x=203, y=40)

    def destroy_search_lb(self):
        self.search_bg_label.destroy()
        self.home_page() 

    def create_confirm(self):
        if not self.selected_wisata:
            messagebox.showwarning("Warning", "Please select at least one wisata before proceeding!")
            return
        else:
            if messagebox.askyesno("Confirmation", "Are you sure of your choice?"):         
                self.create()
            else:
                messagebox.showinfo("Info", "Please review your choice.")

    def create(self):
        self.frame_create=CTkFrame(self.search_bg_label, fg_color="#FFFFFF", height=270, width=252, border_width=2, corner_radius=20)
        self.frame_create.place(x=11, y=102)

        label_create = CTkLabel(self.frame_create,  text='Input Details', text_color="black",  font=('Poppins ExtraBold', 12, 'bold'))
        label_create.place(x=15, y=10)

        label_title = CTkLabel(self.frame_create,  text='Create a title', text_color="#ADADAD",  font=('Poppins ExtraBold', 12))
        label_title.place(x=15, y=30)
        
        self.entry_title = CTkEntry(self.frame_create,placeholder_text="Title", placeholder_text_color="#ADADAD", text_color="#ADADAD", corner_radius=16, width=220, height=32,  font=('Poppins ExtraBold', 11), fg_color="transparent")
        self.entry_title.place(x=15, y=53)

        label_date1 = CTkLabel(self.frame_create,  text='Start date', text_color="#ADADAD",  font=('Poppins ExtraBold', 12))
        label_date1.place(x=15, y=87)

        label_date2 = CTkLabel(self.frame_create,  text='End date', text_color="#ADADAD",  font=('Poppins ExtraBold', 12))
        label_date2.place(x=133, y=87)

        self.date1_entry = DateEntry(self.frame_create, text_color="#ADADAD", corner_radius=16, width=15, height=32, font=('Poppins ExtraBold', 11), fg_color="#0373F3", background="#0373F3")
        self.date1_entry.place(x=27, y=170)

        self.date2_entry = DateEntry(self.frame_create, text_color="#ADADAD", corner_radius=16, width=15, height=32, font=('Poppins ExtraBold', 11), fg_color="#0373F3", background="#0373F3")
        self.date2_entry.place(x=200, y=170)
                
        button_next = CTkButton(self.frame_create,  text='Next', text_color="#FFFFFF", command=self.confirm, font= ('Poppins ExtraBold', 12),  fg_color="#0373F3", hover_color="#E9E9E9")
        button_next.place(x=57, y=232)


    #buat cek format entry jam
    def validate_time_format(self):
        time_pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        date_time_map = {}
        all_valid = True

        #tambahan biar semua tanggalnya keisi
        selected_dates_set = set(date_var.get() for date_var in self.selected_dates)
        if not selected_dates_set.issuperset(self.date_list):
            all_valid = False
            missing_dates = set(self.date_list) - selected_dates_set
            messagebox.showwarning("Missing Dates", f"The following dates are missing: {', '.join(missing_dates)}. You can edit the dates of each trip or go back to reselect your trip dates.")
            return

        for date_var, entry in zip(self.selected_dates, self.selected_times):
            date = date_var.get()
            user_input = entry.get()
            
            if not user_input:
                all_valid = False
                messagebox.showwarning("Empty Entry", "All entries must be filled.")
                break
            if not re.match(time_pattern, user_input):
                all_valid = False
                messagebox.showwarning("Invalid Time Format", f"Time '{user_input}' is not in HH:MM format.")
                break
            
            if date not in date_time_map:
                date_time_map[date] = []
            
            if user_input in date_time_map[date]:
                all_valid = False
                messagebox.showwarning("Duplicate Time", f"The time '{user_input}' has already been entered for the date {date}. Please enter a different time.")
                break

        if all_valid:
            if messagebox.askyesno("Confirmation", "Are you sure about your answers?"):
                date_time_map[date].append(user_input)
                self.switch(self.planning, self.guide_btn, self.guideb)
            else:
                messagebox.showinfo("Info", "Please review your answers.")

    def planning(self, judul, sd,ed, wst, dl):
        for fm in self.main_fm.winfo_children():
            # fm.destroy()
            fm.forget()

        self.judul = judul
        self.sd = sd
        self.ed = ed
        self.wsta = wst
        self.list_date = dl
        self.list_date2 = dl
 
        
        self.planning_bg = CTkImage(Image.open('media/image/planning_bg.png'), size=(274, 480))
        self.planning_bg_label = CTkLabel(self.main_fm, image=self.planning_bg, text='', width=274, height=480)
        self.planning_bg_label.pack(fill=tk.BOTH, expand=True)

        with open('data/d2.csv', 'r') as fel :
            fd = csv.reader(fel)
          

            for i in fd :
                next_column = 0

                jadol= i[0]
                wstt = i[1]
                sdate = i[2]
                stime = i[3]
                hrg = i[4]

                if self.judul == jadol :

                    label_tittle = CTkLabel(self.planning_bg_label,  text=self.judul, text_color="White", fg_color='#0373F3', bg_color='#0373F3', font=('Poppins ExtraBold', 16, 'bold'))
                    label_tittle.place(x=25, y=60)

                    label_start = CTkLabel(self.planning_bg_label, text=f'{self.sd} - {self.ed}', text_color="White", fg_color='#0373F3', font=('Poppins ExtraBold', 12, 'bold'))
                    label_start.place(x=180, y=60)

                    scroll_frame1 = CTkScrollableFrame(self.planning_bg_label, width=260, height=40, fg_color='white', orientation=HORIZONTAL,  scrollbar_button_color="white", scrollbar_button_hover_color="white")
                    scroll_frame1.place(x=0, y=105)

                    save_btn=CTkButton(self.planning_bg_label, text='Done',  text_color="#FFFFFF", font=('Poppins ExtraBold', 14), fg_color="#0373F3", corner_radius=4, hover_color="#E9E9E9", width=234,  command=lambda: self.switch(self.guide_page, self.guide_btn, self.guideb))
                    save_btn.place(x=20, y=445)

                    for i in self.list_date :
                        day_text = f"Day {next_column + 1}\n{i}"
                        button_date = CTkButton(scroll_frame1, text=day_text, text_color="black", fg_color='white', hover_color="#E9E9E9", font=('Poppins ExtraBold', 12), width=67, command=partial(self.check_date,i, jadol,wstt, sdate, stime, hrg ))
                        button_date.grid(row =0, padx=10, column = next_column)
                        next_column += 1
                    
        self.day_frame = CTkScrollableFrame(self.planning_bg_label, width=252, height=265, fg_color='#F4F4F4', scrollbar_button_color='#F4F4F4', scrollbar_button_hover_color='#F4F4F4')
        self.day_frame.place(x=0, y=165)

        self.label_wisata = CTkLabel(self.day_frame, text='', text_color="black", font=('Poppins ExtraBold', 14), wraplength=270, justify='left')

    def check_date(self,i,jadol, wstt, sdate, edate, hrg):
        for wg in self.day_frame.winfo_children() :
            wg.forget()

        self.day_date(i,jadol, wstt, sdate, edate, hrg)  

    def day_date(self, date, judul, wistaa, sdatee, edatee, hrgg):
        a = 0
        data = []
        
        with open("data/d2.csv", 'r') as file:
            fl2 = csv.reader(file)
            for i in fl2:
                jadil = i[0]
                wst2 = i[1]
                slct_tanggal = i[2]
                slct_times = i[3]
                prc = i[4]
                if jadil == judul and slct_tanggal == date:
                    data.append((wst2, slct_times, prc))
        
        # Sort the data by time using quicksort2
        sorted_data = self.quicksort2(data)
        
        for wst2, slct_times, prc in sorted_data:
            label_wisata = CTkLabel(self.day_frame, text=f"⚫️ {wst2} \n      {slct_times} | IDR {prc}k", text_color="black", font=('Poppins ExtraBold', 14), wraplength=270, justify='left')
            label_wisata.pack(pady=5, padx=7, anchor='w')
            a += 1
        
        if not sorted_data:
            for i in self.day_frame.winfo_children():
                i.destroy()

    def confirm (self):
        title = self.entry_title.get()
        startdate = self.date1_entry.get()
        enddate = self.date2_entry.get()
        # self.frame_create.place_forget()

        if not title :
            messagebox.showwarning("Warning", "Please enter the title!")
            return
        if len(title) > 12:
            messagebox.showwarning("Warning", "Title cannot exceed 12 characters!")
            return
        try:
            start_date_obj = datetime.strptime(startdate, '%m/%d/%y')
            end_date_obj = datetime.strptime(enddate, '%m/%d/%y')
            
            if start_date_obj > end_date_obj:
                messagebox.showwarning("Warning", "The start date must be earlier than the end date!")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Invalid date format!")
            return
        
        with open('data/data/d1.csv', 'r') as file :
            fds = csv.reader(file)
            for i in fds :
                jadiul = i[0]
                if i :
                 if title in jadiul :
                    messagebox.showwarning("Invalid", f"Judul {title} Sudah ada.")
                    return
                
        try :
            self.sd = datetime.strptime(startdate, '%m/%d/%y')
            self.ed = datetime.strptime(enddate, '%m/%d/%y')

            if self.ed < self.sd :
                messagebox.showwarning("Warning", "The start date must be earlier than the end date!")
                return
            
        except ValueError:
            messagebox.showwarning("Warning", "Invalid date format!")
            return
        
        self.frame_create1=CTkFrame(self.search_bg_label, fg_color="#FFFFFF", height=270, width=252, border_width=2, corner_radius=20)
        self.frame_create1.place(x=11, y=102)

        label_set_data = CTkLabel(self.frame_create1,  text='Set date and time', text_color="black",  font=('Poppins ExtraBold', 12, 'bold'))
        label_set_data.place(x=45, y=10)

        button_back_set_date = CTkButton(self.frame_create1,  text='←', width=4, text_color="black", fg_color="#FFFFFF", hover_color="#E9E9E9", font=('Poppins ExtraBold', 12, 'bold'),command=self.create)
        button_back_set_date.place(x=15, y=10)

        self.scrollframe_create=CTkScrollableFrame(self.frame_create1,  fg_color="#FFFFFF", width=230, height=80, border_width=0, corner_radius=0, scrollbar_button_color="white", scrollbar_button_hover_color="white")
        self.scrollframe_create.place(x=3, y=37)

        start_date2 = self.date1_entry.get_date()
        end_date2 = self.date2_entry.get_date()

        self.date_list = [(start_date2 + timedelta(days=x)).strftime('%d-%m') for x in range((end_date2 - start_date2).days + 1)]  
            
        with open("data/d1.csv", '+a', newline='') as file :
            fl = csv.writer(file)
            fl.writerow((title, startdate, enddate, self.selected_wisata, self.date_list))

        with open('data/d1.csv', 'r') as file :
            fr = csv.reader(file)
            data = list(fr)
            self.index = 0
            self.selected_dates_all = []
            self.selected_times_all = []
            self.selected_destination_all = []
            self.selected_harga_all = []

            for i in data :
                judul = i[0]
                self.judull = judul
                wst = ast.literal_eval(i[3])
                date_list = ast.literal_eval(i[4])
                if judul == title :
                    for j in wst :
                        if len(j) >= 3 :
                            self.destination = j[2]
                            self.harga = j[3]
                            self.selected_destination.append(self.destination)
                            self.selected_harga.append(self.harga)
                            self.frame_g2 = CTkFrame(self.scrollframe_create, fg_color='white')
                            self.frame_g2.grid(row=self.index)
                            self.index += 1

                            self.wrapped_text = "\n".join(textwrap.wrap(self.destination, width=20))
                            self.label_wisata = CTkLabel(self.frame_g2, text=self.wrapped_text, text_color="black", fg_color='white', font=('Poppins ExtraBold', 12), width=120, justify='left', anchor='w')
                            self.label_wisata.pack(side='left', fill='y', padx=15)

                            self.sub_frame = CTkFrame(self.frame_g2, fg_color='white')
                            self.sub_frame.pack(side='right', fill='y', padx=0)

                            date_var = StringVar(value=date_list[0])
                            self.selected_dates.append(date_var)

                            date_combobox = CTkComboBox(self.sub_frame, values=date_list, text_color="#000000", width=70, dropdown_fg_color="#FFFFFF", font=('Poppins ExtraBold', 11), fg_color="#FFFFFF", variable=date_var)
                            date_combobox.pack(side='top', pady=3)

                            self.time_entry = CTkEntry(self.sub_frame, placeholder_text="HH:MM", placeholder_text_color="#ADADAD", text_color="#ADADAD", corner_radius=16, width=70, height=32, font=('Poppins ExtraBold', 11), fg_color="transparent")
                            self.time_entry.pack(side='top', pady=3)
                            self.selected_times.append(self.time_entry)

        self.selected_dates_all.append(self.selected_dates)
        self.selected_times_all.append(self.selected_times)
        self.selected_destination_all.append(self.selected_destination)
        self.selected_harga_all.append(self.selected_harga)

        button_create = CTkButton(self.frame_create1,  text='Next', command=partial(self.cek_time, title), text_color="#FFFFFF", font= ('Poppins ExtraBold', 12),  fg_color="#0373F3", hover_color="#E9E9E9")
        button_create.place(x=57, y=232)


    def validate_time(self,time_str):
        time_pattern = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
        return bool(re.match(time_pattern, time_str))
    

    def cek_time(self, title):
        self.frame_create.place_forget()
        all_valid = True
        self.new_data = []
        self.date_time_map = {}

        selected_dates_set = set(date_var.get() for date_var in self.selected_dates)
        if not selected_dates_set.issuperset(self.date_list):
            all_valid = False
            missing_dates = set(self.date_list) - selected_dates_set
            messagebox.showwarning("Missing Dates", f"The following dates are missing: {', '.join(missing_dates)}. You can edit the dates of each trip or go back to reselect your trip dates.")
            return

        for destinations, dates, times, prices in zip(self.selected_destination_all, self.selected_dates_all, self.selected_times_all, self.selected_harga_all):
            for destination, date_var, time_entry, harga in zip(destinations, dates, times, prices):
                date = date_var.get()
                time_str = time_entry.get()

                # Pengecekan validasi
                if not time_str:
                    all_valid = False
                    messagebox.showwarning("Empty Time Entry", f"Time entry for '{destination}' cannot be empty.")
                    break
                elif not self.validate_time(time_str):
                    all_valid = False
                    messagebox.showwarning("Invalid Time Format", f"Time entry '{time_str}' for '{destination}' is not in HH:MM format (00:00 - 23:59).")
                   
                if date not in self.date_time_map:
                    self.date_time_map[date] = []
                
                if time_str in self.date_time_map[date]:
                    all_valid = False
                    messagebox.showwarning("Duplicate Time", f"The time '{time_str}' has already been entered for the date {date}. Please enter a different time.")
                    return

                elif (destination, date, time_str) in self.new_data:
                     continue
            
                else:
                    self.new_data.append((title, destination, date, time_str, harga))
                    self.date_time_map[date].append(time_str)

        self.selected_dates_all = []
        self.selected_times_all = []
        self.selected_destination_all = []
        self.selected_harga_all = []
        self.selected_destination = []
        self.selected_harga = []
        self.selected_dates = []
        self.selected_times = []

        if all_valid:
            if messagebox.askyesno("Confirmation", "Are you sure about your answers?"):
                self.nulis(self.new_data)
                self.switch(self.guide_page, self.guide_btn, self.guideb)
            else:
                messagebox.showinfo("Info", "Please review your answers.")
        else:
            messagebox.showinfo("Info", "Please fix the invalid entries.")

    def nulis(self, new_data):
        with open('data/d2.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows((new_data))
                self.new_data.clear()
                self.selected_dates_all.clear()
                self.selected_destination_all.clear()
                self.selected_harga_all.clear()
                self.selected_times_all.clear()
                self.selected_wisata.clear()

    # Penerapan quickshort dalam pengurutan wisata berdasarkan input jam oleh user
    def quicksort2(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2][1]  # Use time as the pivot
        left = [x for x in arr if x[1] < pivot]
        middle = [x for x in arr if x[1] == pivot]
        right = [x for x in arr if x[1] > pivot]
        return self.quicksort2(left) + middle + self.quicksort2(right)

    def show_day_frame(self, day):
        for frame in self.day_frames.values():
            frame.place_forget()
        self.day_frames[day].place(x=0, y=165)

    def show_date_frame(self, date):
        # Hapus frame tanggal sebelumnya jika ada
        if hasattr(self, 'date_frame1'):
            self.date_frame1.destroy()
        # Buat frame baru untuk menampilkan tanggal
        self.date_frame1 = ctk.CTkFrame(self.planning_bg_label, fg_color='red', width=275, height=313)
        self.date_frame1.place(x=0, y=165)
        label1 = ctk.CTkLabel(self.date_frame1, text=f"Selected Date: {date}", font=('Poppins ExtraBold', 16), width=254, height=313)
        label1.grid(row =0, padx=10)

    def AI_page(self):
        self.ai_bg = CTkImage(Image.open('media/image/ai_bg.png'), size=(274, 480))
        self.AI_page_fm = CTkLabel(self.main_fm, image=self.ai_bg, text='', width=27, height=480)
        self.AI_page_fm.pack(fill=tk.BOTH, expand=True)

        self.scrollableframe = ctk.CTkScrollableFrame(self.AI_page_fm, fg_color="#FFFFFF", corner_radius=0, width=273, height=400)
        self.scrollableframe.place(x=0, y=51)

        self.entry_frame = ctk.CTkFrame(self.AI_page_fm, fg_color="#FFFFFF",  width=200, height=37,)
        self.entry_frame.place(relx=0.5, rely=1.0, anchor="s", relwidth=1.0)

        self.entry_field = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter your question", placeholder_text_color="#A9A9A9", text_color="#ADADAD", corner_radius=16, font=("Poppins Bold", 11), width=205, height=31, fg_color="transparent")
        self.entry_field.place(x=15, y=3)
        self.entry_field.bind("<Return>", self.send_message)

        self.kirim =  CTkImage(Image.open("media/image/send.png"), size=(31, 31))
        self.send_btn = CTkButton(self.entry_frame, image=self.kirim, command=self.send_message, text='',hover_color="#FFFFFF", corner_radius=0, border_width=0, width=32, height=32, fg_color='#FFFFFF')
        self.send_btn.place(x=223, y=0)

    def send_message(self, event=None):
        global user_message
        user_message = self.entry_field.get()
        self.display_message(f"{user_message}\n", "user")
        self.entry_field.delete(0, tk.END)

        self.get_response(user_message)

    def display_message(self, message, sender):
        label = ctk.CTkLabel(self.scrollableframe, text=message, anchor="w", justify="left", fg_color="#0373F3",  text_color="#FFFFFF" , wraplength=230, corner_radius=16)
        label.update_idletasks() 
        self.text_width = label.winfo_reqwidth()

        if sender == "user":
            label.configure(anchor="e", justify="right",  width=self.text_width)
            label.pack(anchor="e", padx=10, pady=5)
        else:
            label.configure(width=self.text_width) 
            label.pack(anchor="w", padx=10, pady=5)
        self.scrollableframe.update_idletasks()
        self.scrollableframe._parent_canvas.yview_moveto(1.0)

    def get_response(self, user_message):
        wisata_dict = ["rekomendasi", 'saran']
        keyword = ["termurah", 'murah', 'gratis', 'rendah', 'tinggi', 'mahal']
        ai = user_message
        ai.lower()
        self.key1 = ""
        self.key2 = ""
        self.key3 = ''

        for i in wisata_dict :
            if i in ai :
                self.key1 = "tujuan"
            elif "malang" in ai :
                self.key2 = "malang"
                if 'murah' in ai :
                    self.key3 = 'murah'
                elif 'termurah' in ai :
                    self.key3 = 'termurah'
                elif 'murah' in ai:
                    self.key3 = 'murah'
                elif 'gratis' in ai:
                    self.key3 ='gratis'
                elif 'rendah' in ai:
                    self.key3 = "rendah"
                elif 'tinggi' in ai:
                    self.key3 = "tinggi"
                elif 'mahal' in ai:
                    self.key3 = 'mahal'
                else:
                    self.key3 = ''
            elif "surabaya" in ai :
                self.key2 = "surabaya"
                if 'murah' in ai :
                    self.key3 = 'murah'
                elif 'termurah' in ai :
                    self.key3 = 'termurah'
                elif 'murah' in ai:
                    self.key3 = 'murah'
                elif 'gratis' in ai:
                    self.key3 ='gratis'
                elif 'rendah' in ai:
                    self.key3 = "rendah"
                elif 'tinggi' in ai:
                    self.key3 = "tinggi"
                elif 'mahal' in ai:
                    self.key3 = 'mahal'
                else:
                    self.key3 = ''
            elif "banyuwangi" in ai :
                self.key2 = "banyuwangi"
                if 'murah' in ai :
                    self.key3 = 'murah'
                elif 'termurah' in ai :
                    self.key3 = 'termurah'
                elif 'murah' in ai:
                    self.key3 = 'murah'
                elif 'gratis' in ai:
                    self.key3 ='gratis'
                elif 'rendah' in ai:
                    self.key3 = "rendah"
                elif 'tinggi' in ai:
                    self.key3 = "tinggi"
                elif 'mahal' in ai:
                    self.key3 = 'mahal'
                else:
                    self.key3 = ''

        res = self.berikan_saran(self.key1,self.key2, self.key3)
        res = textwrap.wrap(res, width =self.text_width)
        res = '\n'.join(res)
        self.display_message(f"{res}\n", "bot")

    def berikan_saran(self, key1, key2, key3) :
        if key1 == "tujuan":
            if key2 == "surabaya" :
                if key3 == "murah" :
                    return("Pantai Kenjeran Lama, Monumen Kapal Selam dan Wisata Perahu Kalimas")
                if key3 == "termurah" :
                    return("Monumen Tugu Pahlawan,Kampung Bulak dan Kelenteng Sanggar Agung Kenjeran")
                if key3 == "gratis" :
                    return("Taman Bungkul, Pelabuhan Tanjung Perak, Kebun Bibit Wonorejo, Taman Lanjut Usia dan Taman Mozaik")
                if key3 == "rendah" :
                    return("House of Sampoerna, Kampung Bulak dan Hutan Bambu Keputih")
                if key3 == "tinggi" :
                    return("Taman Bungkul, Balai Pemuda Surabaya, Patung Buddha Empat Wajah, dan Wisata Perahu Kalimas")
                if key3 == "mahal" :
                    return("Kebun Binatang Surabaya, Blockbuster Museum Surabaya dan Atlantis Land Kenjeran")
                if key3 =='':
                    return("Monumen Tugu Pahlawan, Kebun Binatang Surabaya, Food Junction Surabaya, Taman Bungkul dan Kampoeng Arab Indonesiaa")              
            elif key2 == "malang" :
                if key3 == "murah" :
                    return("Dairyland Farm Theme Park Prigen, Florawisata Santerra de Laponte dan Lembah Indah Malang")
                if key3 == "termurah" :
                    return("Sumber Sira Putukrejo, Agrowisata Teh Wonosari dan Air Terjun Coban Rondo")
                if key3 == "gratis" :
                    return("Alun Alun Kota Malang dan Taman Kunang Kunang")
                if key3 == "rendah" :
                    return("Kusuma Waterpark, Predator Fun Park Batu dan Taman Kunang Kunang")
                if key3 == "tinggi" :
                    return("Pantai Batu Bengkung, Museum Angkut, Bromo, Cycling and Village Tour in Malang dan Jatim Park 2")
                if key3 == "mahal" :
                    return("Jatim Park 3, Museum Angkut, Batu Night Spectacular, Bromo dan Hawai Waterpark") 
                if key3 =='':
                    return("Bromo, Hawai Waterpark, Jatim Park, Pantai Batu Bengkung dan Taman Langit Gunung Banyak")  
            elif key2 == "banyuwangi":
                if key3 == "murah" :
                    return("Pantai Ngagelan, Pantai Trianggulasi dan Pulau Merah")
                if key3 == "termurah" :
                    return("Pantai Rajegwesi, Air Terjun Lider dan Taman Nasional Alas Purwo")
                if key3 == "gratis" :
                    return("Pantai Parang Kursi")
                if key3 == "rendah" :
                    return("Waduk Sidodadi, Panorama Pantai Cacalan dan Banyuwangi Park")
                if key3 == "tinggi" :
                    return("Kawah Ijen, Pulau Merah dan Wedi Ireng")
                if key3 == "mahal" :
                    return("Taman Gandrung Terakota, Pantai Trianggulasi dan Pantai Ngagelan")
                if key3 =='':
                    return("Kawah Ijen, Wedi Ireng, Pulau Merah, Pulau Tabuhan dan Padang Savana")
            elif not key2:  
                return("DESTI AI dapat merekomendasikan wisata jika anda menyebutkan kota Surabaya, Malang, atau Banyuwangi")
        
        else:
            return("Maaf, saya belum memahami pertanyaan Anda. Bisakah Anda coba dengan pertanyaan lain?")
        
    def guide_page(self):
        
        self.home_btn.configure(state=ACTIVE)
        self.AI_btn.configure(state=ACTIVE)
        self.guide_btn.configure(state=ACTIVE)
        self.article_btn.configure(state=ACTIVE)

        with open("data/d2.csv", 'r' ) as fer :
            fr = csv.reader(fer)
            for i in fr:
                if not i :
                    self.guide_bgb = CTkImage(Image.open('media/image/guide_bgb.png'), size=(274, 480))
                    self.guide_bgb_label = CTkLabel(self.main_fm, image=self.guide_bgb, text='', width=274, height=480)
                    self.guide_bgb_label.pack(fill=tk.BOTH, expand=True)

                    create_g_btn=CTkButton(self.guide_bgb_label, text='Create',  text_color="black", font=('Poppins Bold', 14), fg_color="white", corner_radius=5, hover_color="white", width=70, command=lambda: self.switch(self.home_page, self.home_btn, self.homeb))
                    create_g_btn.place(x=102, y=261)
                    return
                
                else :
                    
                    self.guide_bg = CTkImage(Image.open('media/image/guide_bg.png'), size=(274, 480))
                    self.guide_bg_label = CTkLabel(self.main_fm, text='', width=274, height=480, image=self.guide_bg)
                    self.guide_bg_label.pack(fill=tk.BOTH, expand=True)
                    self.scrl_frm = CTkScrollableFrame(self.guide_bg_label,  width=274, fg_color="white", orientation=VERTICAL, height=370)
                    self.scrl_frm.place(x=10, y=100)

                    with open("data/d1.csv", 'r') as file :
                                f = csv.reader(file)
                                data = list(f)
                                next_row = 0
                                
                                with open('data/d2.csv', 'r') as file :
                                    f2 = csv.reader(file)
                                    data2 = list(f2)
                                    for i in data :
                                        judul = i[0]
                                        sd = i[1]
                                        ed = i[2]
                                        wst2 = ast.literal_eval(i[3])
                                        date_list2 = ast.literal_eval(i[4])

                                        found_match = False
                                        for j in data2:
                                            judul2 = j[0]
                                            if judul == judul2:
                                                found_match = True
                                                self.plan_lb = CTkButton(self.scrl_frm, text=f'{judul} \n  {sd} - {ed}', command=partial(self.planning, judul, sd, ed, wst2, date_list2), width=240, height=75, text_color="#FFFFFF", font=('Poppins ExtraBold', 16), fg_color="#0373F3", corner_radius=4, hover_color="#0373F3")
                                                self.plan_lb.grid(row=next_row, pady=10)
                                                next_row += 1
                                                break

    def article_page(self):
        self.clear_widgets()

        scrollableframe = CTkScrollableFrame(master=self.main_fm, fg_color="#FFFFFF", corner_radius=0, width=275, height=445)
        scrollableframe.place(x=0, y=40)
        self.scrollableframe1 = tk.Canvas(scrollableframe, bg="#FFFFFF",  width=275, height=0)
        self.scrollableframe1.pack(fill=tk.BOTH, expand=True)

        Judul_artikel = CTkLabel(self.main_fm, text="Article", compound="top", font=("Poppins", 14, "bold"), text_color="Black", fg_color="White")
        Judul_artikel.pack(padx=100, pady=5)

        frame_artikel1 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel1.pack()

        image_artikel1_path = "media/image/Judul Artikel1.png"
        image_artikel1 = Image.open(image_artikel1_path)
        image_artikel1_width = 220
        image_artikel1_height = 65
        image_artikel1 = image_artikel1.resize((image_artikel1_width, image_artikel1_height), Image.LANCZOS)  
        image_artikel1 = CTkImage(image_artikel1, size=(image_artikel1_width, image_artikel1_height))

        judul_artikel1 = ctk.CTkButton(frame_artikel1, text="", image=image_artikel1, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel1)
        judul_artikel1.image = image_artikel1 
        judul_artikel1.pack(padx=20, pady=1)

        
        #####################

        frame_artikel2 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel2.pack()

        image_artikel2_path = "media/image/Judul Artikel2.png"
        image_artikel2 = Image.open(image_artikel2_path)
        
        image_artikel2_width = 220
        image_artikel2_height = 65
        image_artikel2 = image_artikel2.resize((image_artikel2_width, image_artikel2_height), Image.LANCZOS)  
        image_artikel2 = CTkImage(image_artikel2, size=(image_artikel2_width, image_artikel2_height))

        judul_artikel2 = ctk.CTkButton(frame_artikel2, text="", image=image_artikel2, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel2)
        judul_artikel2.image = image_artikel2 
        judul_artikel2.pack(padx=20, pady=1)
    
        ########################

        frame_artikel3 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel3.pack()

        image_artikel3_path = "media/image/Judul Artikel3.png"
        image_artikel3 = Image.open(image_artikel3_path)
  
        image_artikel3_width = 220
        image_artikel3_height = 65
        image_artikel3 = image_artikel3.resize((image_artikel3_width, image_artikel3_height), Image.LANCZOS)  
        image_artikel3 = CTkImage(image_artikel3, size=(image_artikel3_width, image_artikel3_height))

        judul_artikel3 = ctk.CTkButton(frame_artikel3, text="", image=image_artikel3, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel3)
        judul_artikel3.image = image_artikel3 
        judul_artikel3.pack(padx=20, pady=1)

        ##########################################
        frame_artikel4 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel4.pack()

        image_artikel4_path = "media/image/Judul Artikel4.png"
        image_artikel4 = Image.open(image_artikel4_path)

        image_artikel4_width = 220
        image_artikel4_height = 65
        image_artikel4 = image_artikel4.resize((image_artikel4_width, image_artikel4_height), Image.LANCZOS)  
        image_artikel4 = CTkImage(image_artikel4, size=(image_artikel4_width, image_artikel4_height))

        judul_artikel4 = ctk.CTkButton(frame_artikel4, text="", image=image_artikel4, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel4)
        judul_artikel4.image = image_artikel4 
        judul_artikel4.pack(padx=20, pady=1)

        ####################################
        frame_artikel5 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel5.pack()

        image_artikel5_path = "media/image/Judul Artikel5.png"
        image_artikel5 = Image.open(image_artikel5_path)
   
        image_artikel5_width = 220
        image_artikel5_height = 65
        image_artikel5 = image_artikel5.resize((image_artikel5_width, image_artikel5_height), Image.LANCZOS)  
        image_artikel5 = CTkImage(image_artikel5, size=(image_artikel5_width, image_artikel5_height))

        judul_artikel5 = ctk.CTkButton(frame_artikel5, text="", image=image_artikel5, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel5)
        judul_artikel5.image = image_artikel5
        judul_artikel5.pack(padx=20, pady=1)

        ###################
        frame_artikel6 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel6.pack()

        image_artikel6_path = "media/image/Judul artikel6.png"
        image_artikel6 = Image.open(image_artikel6_path)
   
        image_artikel6_width = 220
        image_artikel6_height = 65
        image_artikel6 = image_artikel6.resize((image_artikel6_width, image_artikel6_height), Image.LANCZOS)  
        image_artikel6 = CTkImage(image_artikel6, size=(image_artikel6_width, image_artikel6_height))

        judul_artikel6 = ctk.CTkButton(frame_artikel6, text="", image=image_artikel6, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel5)
        judul_artikel6.image = image_artikel6
        judul_artikel6.pack(padx=20, pady=1)

        #####################################

        frame_artikel7 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel7.pack()

        image_artikel7_path = "media/image/Judul artikel7.png"
        image_artikel7 = Image.open(image_artikel7_path)
   
        image_artikel7_width = 220
        image_artikel7_height = 65
        image_artikel7 = image_artikel7.resize((image_artikel7_width, image_artikel7_height), Image.LANCZOS)  
        image_artikel7 = CTkImage(image_artikel7, size=(image_artikel7_width, image_artikel7_height))

        judul_artikel7 = ctk.CTkButton(frame_artikel7, text="", image=image_artikel7, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel5)
        judul_artikel7.image = image_artikel7
        judul_artikel7.pack(padx=20, pady=1)

        ########################################
        frame_artikel8 = ctk.CTkFrame(scrollableframe, fg_color="white")
        frame_artikel8.pack()

        image_artikel8_path = "media/image/Judul artikel8.png"
        image_artikel8 = Image.open(image_artikel8_path)
   
        image_artikel8_width = 220
        image_artikel8_height = 65
        image_artikel8 = image_artikel8.resize((image_artikel8_width, image_artikel8_height), Image.LANCZOS)  
        image_artikel8 = CTkImage(image_artikel8, size=(image_artikel8_width, image_artikel8_height))

        judul_artikel8 = ctk.CTkButton(frame_artikel8, text="", image=image_artikel8, compound="top", font=("Sitka Small", 11), fg_color="white", command=self.isi_artikel5)
        judul_artikel8.image = image_artikel8
        judul_artikel8.pack(padx=20, pady=1)
    ####################################################

    def clear_widgets(self):
        for widget in self.main_fm.winfo_children():
            widget.pack_forget()

    def create_back_button(self, frame, command):
        back_artikel_path = "media/image/back artikel.png"
        back_artikel = Image.open(back_artikel_path)
        back_artikel = back_artikel.resize((34, 30), Image.LANCZOS)
        back_artikel = CTkImage(back_artikel, size=(34, 30))
        button_back = CTkButton(frame, text="", image=back_artikel, font=("Sitka Small", 11), fg_color="white", command=command, width=3, height=20)
        button_back.image = back_artikel
        button_back.place(x=1, y=1)

    def create_article_frame(self, article_image_path, article_image_height):
        self.clear_widgets()

        frame_back = CTkFrame(self.main_fm, fg_color="white", width=280, height=43)
        frame_back.pack()
        
        frame_article = CTkFrame(self.main_fm, fg_color="White", width=274, height=480)
        frame_article.pack()

        canvas = CTkCanvas(frame_article, bg="white", width=274, height=480)
        canvas.pack(side="left", fill="both", expand=True)
        canvas.config(height=960, width=549)

        scrollbar = CTkScrollbar(frame_article, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame_image = CTkFrame(canvas)
        canvas.create_window((0, 0), window=frame_image, anchor='nw')

        article_image = CTkImage(Image.open(article_image_path), size=(270, article_image_height))
        label_article = CTkLabel(frame_image, text="", image=article_image, compound="top", font=("Sitka Small", 11), fg_color="white")
        label_article.image = article_image
        label_article.pack()

        frame_image.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        return frame_back

    def isi_artikel(self, article_image_path, article_image_height, back_command):
        frame_back = self.create_article_frame(article_image_path, article_image_height)
        self.create_back_button(frame_back, back_command)

    def isi_artikel1(self):
        self.isi_artikel("media/image/isi artikel1.png", 1985, self.article_page)

    def isi_artikel2(self):
        self.isi_artikel("media/image/isi artikel2.png", 2760, self.article_page)

    def isi_artikel3(self):
        self.isi_artikel("media/image/isi artikel3.png", 2585, self.article_page)

    def isi_artikel4(self):
        self.isi_artikel("media/image/isi artikel4.png", 700, self.article_page)

    def isi_artikel5(self):
        self.isi_artikel("media/image/isi artikel5.png", 2540, self.article_page)

    def artikel_R1(self):
        self.isi_artikel("media/image/ARTIKEL WR1.png", 2540, self.article_page)


if __name__ == "__main__":
    app = DestifindApp()
    app.mainloop()


